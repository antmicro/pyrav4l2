from __future__ import annotations
from pathlib import Path
from typing import Dict, List, Tuple, Type
from fcntl import ioctl
from .controls import Control, Menu, MenuItem, IntegerMenuItem, Item
from .v4l2 import *


class ColorFormat:

    def __init__(self, description: str, pixelformat: int, flags: int) -> None:
        self.description = description
        self.pixelformat = pixelformat
        self._flags = flags

    def __str__(self) -> str:
        return self.description

    def __eq__(self, other) -> bool:
        return self.pixelformat == other.pixelformat

    def __hash__(self):
        return hash(self.pixelformat)

    @property
    def is_compressed(self) -> bool:
        return bool(self._flags & V4L2_FMT_FLAG_COMPRESSED)

    @property
    def is_emulated(self) -> bool:
        return bool(self._flags & V4L2_FMT_FLAG_EMULATED)


class FrameSize:

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"{self.width} x {self.height}"

    def __eq__(self, other) -> bool:
        return self.width == other.width and self.height == other.height


class Device:
    """Class representing a v4l2 device"""

    def __init__(self, path: str | Path) -> None:
        """
        Parameters
        ----------
        path : str | Path
            The path to v4l2 device
        """

        self.path = Path(path)
        if not self.path.is_char_device():
            raise AttributeError("Provided path is not a device")

        self._get_capabilities()

        if self.is_video_capture_capable:
            self._get_available_formats()

        self._get_controls()

    @classmethod
    def with_id(self, id: int) -> Device:
        """
        Constructs Device instance based on device's id

        Parameters
        ----------
        id : int
            The id number of v4l2 device
        """

        return Device(f"/dev/video{id}")

    def get_format(self) -> Tuple[ColorFormat, FrameSize]:
        """
        Get currently used color format and frame size

        Raises
        ------
        DeviceNotSupportVideoCapture
            If this device does not support video capture
        """

        if not self.is_video_capture_capable:
            raise DeviceNotSupportVideoCapture(self.path)

        with open(self.path) as f_cam:
            fmt = v4l2_format()
            fmt.type = V4L2_BUF_TYPE_VIDEO_CAPTURE
            ioctl(f_cam, VIDIOC_G_FMT, fmt)

            frame_size = FrameSize(fmt.fmt.pix.width, fmt.fmt.pix.height)
            color_format = next(
                filter(lambda x: x.pixelformat == fmt.fmt.pix.pixelformat,
                       self._available_formats.keys()))

        return (color_format, frame_size)

    def set_format(self, color_format: ColorFormat,
                   frame_size: FrameSize) -> None:
        """
        Set color format and frame size

        Parameters
        ----------
        color_format : ColorFormat
            Color format to be used
        frame_size : FrameSize
            Frame size to be used

        Raises
        ------
        DeviceNotSupportVideoCapture
            If this device does not support video capture
        UnsupportedColorFormat
            If given color format is not supported by the device
        UnsupportedFrameSize
            If given frame size is not supported by the device
        """

        if not self.is_video_capture_capable:
            raise DeviceNotSupportVideoCapture(self.path)

        if any(color_format == available_format
               for available_format in self._available_formats.keys()):
            if any(frame_size == available_size for available_size in
                   self._available_formats[color_format]):
                with open(self.path) as f_cam:
                    fmt = v4l2_format()
                    fmt.type = V4L2_BUF_TYPE_VIDEO_CAPTURE
                    ioctl(f_cam, VIDIOC_G_FMT, fmt)

                    fmt.fmt.pix.width = frame_size.width
                    fmt.fmt.pix.height = frame_size.height
                    fmt.fmt.pix.pixelformat = color_format.pixelformat
                    fmt.fmt.pix.field = V4L2_FIELD_ANY
                    ioctl(f_cam, VIDIOC_S_FMT, fmt)
            else:
                raise UnsupportedFrameSize(self.path, color_format, frame_size)
        else:
            raise UnsupportedColorFormat(self.path, color_format)

    def set_control_value(self, control: Type[Control],
                          value: bool | int | str | Type[Item]) -> None:
        """
        Set control value

        Parameters
        ----------
        control : Type[Control]
            Control which value need to be set
        value : bool | int | str | Type[Item]
            New control value

        Raises
        ------
        UnsupportedControl
            If device does not have control with given id
        WrongValueType
            If given type of given value is not supported by control
        UnsupportedMenuItem
            If menu control does not have given item
        WrongIntValue
            If value is not in the range supported by control
        WrongStringValue
            If length of value is not in the range supported by control
        """

        if any(control == available_ctrl for available_ctrl in self._controls):
            if isinstance(control, Menu):
                if isinstance(value, Item):
                    if any(item.index == value.index
                           for item in control.items):
                        self._set_value(control, value)
                    else:
                        raise UnsupportedMenuItem(control, value)
                else:
                    raise WrongValueType(value)
            else:
                if control.type in [
                        V4L2_CTRL_TYPE_INTEGER, V4L2_CTRL_TYPE_INTEGER64
                ]:
                    if type(value) == int:
                        if value >= control.minimum and value <= control.maximum and (
                                control.minimum - value) % control.step == 0:
                            self._set_value(control, value)
                        else:
                            raise WrongIntValue(control, value)
                    else:
                        raise WrongValueType(value)
                elif control.type in [
                        V4L2_CTRL_TYPE_BOOLEAN, V4L2_CTRL_TYPE_BUTTON
                ]:
                    if type(value) == bool:
                        self._set_value(control, value)
                    else:
                        raise WrongValueType(value)
                elif control.type == V4L2_CTRL_TYPE_BITMASK:
                    if type(value) == int:
                        self._set_value(control, value)
                    else:
                        raise WrongValueType(value)
                elif control.type == V4L2_CTRL_TYPE_STRING:
                    if type(value) == str:
                        if len(value) >= control.minimum and len(
                                value) <= control.maximum and (
                                    control.minimum -
                                    len(value)) % control.step == 0:
                            self._set_value(control, value)
                        else:
                            WrongStringValue(control, value)
                    else:
                        raise WrongValueType(value)
        else:
            raise UnsupportedControl(self.path, control)

    def get_control_value(
            self, control: Type[Control]) -> bool | int | str | Type[Item]:
        """
        Get current control's value

        Parameters
        ----------
        control : Type[Control]
            Control which value shoulde be returned

        Raises
        ------
        UnsupportedControl
            If device does not have control with given id
        """

        if any(control == available_ctrl for available_ctrl in self._controls):
            ctrl = self._get_control_value(control)

            if control.type in [
                    V4L2_CTRL_TYPE_MENU, V4L2_CTRL_TYPE_INTEGER_MENU
            ]:
                return next(
                    filter(lambda x: x.index == ctrl.value, control.items))
            elif control.type in [
                    V4L2_CTRL_TYPE_BITMASK, V4L2_CTRL_TYPE_INTEGER64
            ]:
                return ctrl.value64
            elif control.type == V4L2_CTRL_TYPE_STRING:
                return ctrl.string.decode()
            else:
                return ctrl.value
        else:
            raise UnsupportedControl(self.path, control)

    def reset_control_to_default(self, control: Type[Control]) -> None:
        """
        Reset control's value to the default one

        Parameters
        ----------
        control : Type[Control]

        Raises
        ------
        UnsupportedControl
            If device does not have control with given id
        """

        if any(control == available_ctrl for available_ctrl in self._controls):
            if control.type in [
                    V4L2_CTRL_TYPE_INTEGER, V4L2_CTRL_TYPE_BOOLEAN,
                    V4L2_CTRL_TYPE_BITMASK, V4L2_CTRL_TYPE_MENU,
                    V4L2_CTRL_TYPE_INTEGER_MENU
            ]:
                default_value = control.default_value
                if control.type == V4L2_CTRL_TYPE_BOOLEAN:
                    default_value = bool(default_value)
                elif control.type in [
                        V4L2_CTRL_TYPE_MENU, V4L2_CTRL_TYPE_INTEGER_MENU
                ]:
                    default_value = next(
                        filter(lambda x: x.index == default_value,
                               control.items))
                self._set_value(control, default_value)
        else:
            raise UnsupportedControl(self.path, control)

    def update_control(self, control: Type[Control]) -> Type[Control]:
        """
        Updates given control's state

        Parameters
        ----------
        control : Type[Control]

        Raises
        ------
        UnsupportedControl
            If device does not have control with given id
        """

        if not any(control == available_ctrl
                   for available_ctrl in self._controls):
            raise UnsupportedControl(self.path, control)

        with open(self.path) as f_cam:
            ctrl = v4l2_query_ext_ctrl()
            ctrl.id = control.id
            ioctl(f_cam, VIDIOC_QUERY_EXT_CTRL, ctrl)

            if ctrl.type in [V4L2_CTRL_TYPE_MENU, V4L2_CTRL_TYPE_INTEGER_MENU]:
                items = []
                for i in range(ctrl.minimum, ctrl.maximum + 1):
                    menu = v4l2_querymenu()
                    menu.id = ctrl.id
                    menu.index = i

                    try:
                        ioctl(f_cam, VIDIOC_QUERYMENU, menu)
                    except OSError:
                        continue

                    if ctrl.type == V4L2_CTRL_TYPE_MENU:
                        items.append(MenuItem(ctrl.id, i, menu.name.decode()))
                    else:
                        items.append(IntegerMenuItem(ctrl.id, i, menu.value))
                ctrl = Menu(ctrl, items)
                ctrl_idx = next(
                    iter([
                        idx for idx, el in enumerate(self._controls)
                        if el == ctrl
                    ]), -1)
                self._controls[ctrl_idx] = ctrl
                return ctrl
            else:
                ctrl = Control(ctrl)
                ctrl_idx = next(
                    iter([
                        idx for idx, el in enumerate(self._controls)
                        if el == ctrl
                    ]), -1)
                self._controls[ctrl_idx] = ctrl
                return ctrl

    @property
    def driver_name(self) -> str:
        return self._driver

    @property
    def device_name(self) -> str:
        return self._card

    @property
    def is_video_capture_capable(self) -> bool:
        return bool(self._capabilities & V4L2_CAP_VIDEO_CAPTURE)

    @property
    def available_formats(self) -> Dict[ColorFormat, List[FrameSize]]:
        if not self.is_video_capture_capable:
            raise DeviceNotSupportVideoCapture(self.path)

        return self._available_formats

    @property
    def controls(self) -> List[Type[Control]]:
        return self._controls

    def _set_value(self, control: Type[Control],
                   value: bool | int | str | Type[Item]) -> None:
        with open(self.path) as f_cam:
            ctrl = v4l2_ext_control()
            ctrl.id = control.id
            if control.type in [
                    V4L2_CTRL_TYPE_MENU, V4L2_CTRL_TYPE_INTEGER_MENU
            ]:
                ctrl.value = value.index
            elif control.type in [
                    V4L2_CTRL_TYPE_BITMASK, V4L2_CTRL_TYPE_INTEGER64
            ]:
                ctrl.value64 = value
            elif control.type == V4L2_CTRL_TYPE_STRING:
                ctrl.string = value
                ctrl.size = len(value) + 1
            else:
                ctrl.value = value

            ectrls = v4l2_ext_controls()
            ectrls.count = 1
            ectrls.controls = ctypes.pointer(ctrl)

            try:
                ioctl(f_cam, VIDIOC_S_EXT_CTRLS, ectrls)
            except OSError:
                pass

    def _get_control_value(self, control: Type[Control]) -> v4l2_ext_control:
        ctrl = v4l2_ext_control()
        ctrl.id = control.id
        if control.type == V4L2_CTRL_TYPE_STRING:
            ctrl.size = control.maximum + 1
            ctrl.string = bytes(control.maximum + 1)

        ectrls = v4l2_ext_controls()
        ectrls.controls = ctypes.pointer(ctrl)
        ectrls.count = 1

        with open(self.path) as f_cam:
            try:
                ioctl(f_cam, VIDIOC_G_EXT_CTRLS, ectrls)
            except OSError:
                pass

        return ctrl

    def _get_capabilities(self) -> None:
        with open(self.path) as f_cam:
            caps = v4l2_capability()
            ioctl(f_cam, VIDIOC_QUERYCAP, caps)

            self._driver = caps.driver.decode()
            self._card = caps.card.decode()
            self._capabilities = caps.device_caps

    def _get_available_formats(self) -> None:
        if not self.is_video_capture_capable:
            raise DeviceNotSupportVideoCapture(self.path)

        self._available_formats = {}

        with open(self.path) as f_cam:
            fmt = v4l2_fmtdesc()
            fmt.type = V4L2_BUF_TYPE_VIDEO_CAPTURE

            while True:
                try:
                    ioctl(f_cam, VIDIOC_ENUM_FMT, fmt)
                except OSError:
                    break

                color_format = ColorFormat(fmt.description.decode(),
                                           fmt.pixelformat, fmt.flags)
                self._available_formats[color_format] = []

                frmsize = v4l2_frmsizeenum()
                frmsize.pixel_format = color_format.pixelformat

                while True:
                    try:
                        ioctl(f_cam, VIDIOC_ENUM_FRAMESIZES, frmsize)
                    except OSError:
                        break

                    if frmsize.type == V4L2_FRMSIZE_TYPE_DISCRETE:
                        self._available_formats[color_format].append(
                            FrameSize(frmsize.discrete.width,
                                      frmsize.discrete.height))

                    frmsize.index += 1

                fmt.index += 1

    def _get_controls(self) -> None:
        self._controls = []
        with open(self.path) as f_cam:
            ctrl_id = V4L2_CTRL_FLAG_NEXT_CTRL

            while True:
                ctrl = v4l2_query_ext_ctrl()
                ctrl.id = ctrl_id
                try:
                    ioctl(f_cam, VIDIOC_QUERY_EXT_CTRL, ctrl)
                except OSError:
                    break

                if ctrl.type in [
                        V4L2_CTRL_TYPE_MENU, V4L2_CTRL_TYPE_INTEGER_MENU
                ]:
                    items = []
                    for i in range(ctrl.minimum, ctrl.maximum + 1):
                        menu = v4l2_querymenu()
                        menu.id = ctrl.id
                        menu.index = i

                        try:
                            ioctl(f_cam, VIDIOC_QUERYMENU, menu)
                        except OSError:
                            continue

                        if ctrl.type == V4L2_CTRL_TYPE_MENU:
                            items.append(
                                MenuItem(ctrl.id, i, menu.name.decode()))
                        else:
                            items.append(
                                IntegerMenuItem(ctrl.id, i, menu.value))
                    self._controls.append(Menu(ctrl, items))
                else:
                    self._controls.append(Control(ctrl))

                ctrl_id = ctrl.id | V4L2_CTRL_FLAG_NEXT_CTRL


class DeviceNotSupportVideoCapture(TypeError):

    def __init__(self, device_path: str | Path) -> None:
        self.device_path = device_path

    def __str__(self) -> str:
        return f"Device '{self.device_path}' is not video capture capable"


class UnsupportedColorFormat(ValueError):

    def __init__(self, device_path: str | Path,
                 color_format: ColorFormat) -> None:
        self.device_path = device_path
        self.color_format = color_format

    def __str__(self) -> str:
        return f"Device '{self.device_path}' does not support '{self.color_format}' color format"


class UnsupportedFrameSize(ValueError):

    def __init__(self, device_path: str | Path, color_format: ColorFormat,
                 frame_size: FrameSize) -> None:
        self.device_path = device_path
        self.color_format = color_format
        self.frame_size = frame_size

    def __str__(self) -> str:
        return f"Device '{self.device_path}' does not support '{self.frame_size}' frame size for '{self.color_format}' format"


class UnsupportedControl(ValueError):

    def __init__(self, device_path: str | Path,
                 control: Type[Control]) -> None:
        self.device_path = device_path
        self.control = control

    def __str__(self) -> str:
        return f"Device '{self.device_path}' does not support control with id '{self.control.id}' ('{self.control.name}')"


class UnsupportedMenuItem(ValueError):

    def __init__(self, menu: Menu, item: Type[Item]) -> None:
        self.menu = menu
        self.item = item

    def __str__(self) -> str:
        if isinstance(self.item, MenuItem):
            return f"Menu '{self.menu.name}' does not support '{self.item.name}' menu item"
        else:
            return f"Menu '{self.menu.name}' does not support '{self.item.value}' menu item"


class WrongValueType(TypeError):

    def __init__(self, value: bool | int | str | Type[Item]) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"Value has wrong type: '{type(self.value).__name__}'"


class WrongIntValue(ValueError):

    def __init__(self, control: Control, value: int) -> None:
        self.control = control
        self.value = value

    def __str__(self) -> None:
        return f"'{self.value}' is not valid for '{self.control.name}'. Allowed values: {self.control.minimum} - {self.control.maximum} (step: {self.control.step})"


class WrongStringValue(ValueError):

    def __init__(self, control: Control, value: str) -> None:
        self.control = control
        self.value = value

    def __str__(self) -> str:
        return f"'{self.value}' is not a valid string for '{self.control.name}'. Its length should be equal to {self.control.minimum} - {self.control.maximum} (step: {self.control.step}), but it is {len(self.value)}"
