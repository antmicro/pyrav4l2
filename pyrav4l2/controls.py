from __future__ import annotations
from abc import ABC
from typing import Type, List
from .v4l2 import *


class Control:

    def __init__(self, control: v4l2_query_ext_ctrl) -> None:
        self.id = control.id
        self.type = control.type
        self.name = control.name.decode()
        self.minimum = control.minimum
        self.maximum = control.maximum
        self.step = control.step
        self.default_value = control.default_value
        self.flags = control.flags

    def __eq__(self, other: Type[Control]) -> bool:
        return self.id == other.id

    @property
    def is_disabled(self) -> bool:
        return bool(self.flags & V4L2_CTRL_FLAG_DISABLED)

    @property
    def is_read_only(self) -> bool:
        return bool(self.flags & V4L2_CTRL_FLAG_READ_ONLY)

    @property
    def is_inactive(self) -> bool:
        return bool(self.flags & V4L2_CTRL_FLAG_INACTIVE)

    @property
    def is_volatile(self) -> bool:
        return bool(self.flags & V4L2_CTRL_FLAG_VOLATILE)


class Menu(Control):

    def __init__(self, control: v4l2_query_ext_ctrl,
                 items: List[Type[Item]]) -> None:
        super().__init__(control)
        self.items = items


class Item(ABC):

    def __init__(self, ctrl_id: int, index: int) -> None:
        self.ctrl_id = ctrl_id
        self.index = index


class MenuItem(Item):

    def __init__(self, ctrl_id: int, index: int, name: str) -> None:
        super().__init__(ctrl_id, index)
        self.name = name


class IntegerMenuItem(Item):

    def __init__(self, ctrl_id: int, index: int, value: int) -> None:
        super().__init__(ctrl_id, index)
        self.value = value
