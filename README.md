# pyrav4l2 - Pythonic, Really Awesome V4L2 utility

Copyright (c) 2022 [Antmicro](https://www.antmicro.com)

pyrav4l2 is a library that lets you easily control V4L2 devices inside python scripts.
It provides a high level API for controlling camera parameters and streaming frames.

# Installation
`pip install git+https://github.com/antmicro/pyrav4l2.git`

# Examples
## Creating device
You can create a device instance using the path of the V4L2 device:
```python
from pyrav4l2 import Device

dev = Device("/dev/video0")
```

or by using its ID number:
```python
from pyrav4l2 import Device

dev = Device.with_id(0)
```

## Getting information about the device
You can easily get device and driver names and check if the selected device supports video capturing
```python
from pyrav4l2 import Device

dev = Device("/dev/video0")
print(f"Device name: {dev.device_name}")
print(f"Driver name: {dev.driver_name}")
if dev.is_video_capture_capable:
    print(f"Device supports video capturing")
else:
    print(f"Device does not support video capturing")
```

## Getting information about currently used color format and frame size
This example shows you how to check what color format and frame size is currently used by the device
```python
from pyrav4l2 import Device

dev = Device("/dev/video0")
color_format, frame_size = dev.get_format()
print(f"Color format: {color_format}")
print(f"Frame size: {frame_size}")
```

## Frame format enumeration and configuration
Here you can see how to get all supported color formats and frame sizes, and configure the device to use the first one of each.
```python
from pyrav4l2 import Device

dev = Device("/dev/video0")
available_formats = dev.available_formats

for color_format in available_formats.keys():
    print(f"{color_format}:")
    for frame_size in available_formats[color_format]:
        print(f"    {frame_size}")
    print()

color_format = list(available_formats.keys())[0]
frame_size = available_formats[color_format][0]
dev.set_format(color_format, frame_size)
```

## Device controls enumeration and configuration
This example shows how to get a list of supported controls and iterate over it.
It prints the names of all controls and resets their values to the default ones.
```python
from pyrav4l2 import Device

dev = Device("/dev/video0")
available_controls = dev.controls

for control in available_controls:
    print(control.name)
    dev.reset_control_to_default(control)
```

## Streaming frames
Here you can see how to stream frame from the camera.
The script below captures 10 frames and prints their lengths.
```python
from pyrav4l2 import Device, Stream

dev = Device("/dev/video0")
for (i, frame) in enumerate(Stream(dev)):
    print(f"Frame {i}: {len(frame)} bytes")

    if i >= 9:
        break
```

# License
[Apache 2.0](LICENSE)
