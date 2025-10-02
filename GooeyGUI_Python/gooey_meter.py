"""
Copyright (c) 2025 Yassine Ahmed Ali

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import ctypes
from .libgooey import *

# Define opaque pointer type
class GooeyMeter(ctypes.Structure): pass
GooeyMeterPtr = ctypes.POINTER(GooeyMeter)

# GooeyMeter_Create
c_lib.GooeyMeter_Create.argtypes = [
    ctypes.c_int,  # x
    ctypes.c_int,  # y
    ctypes.c_int,  # width
    ctypes.c_int,  # height
    ctypes.c_long,  # initial_value
    ctypes.c_char_p,  # label
    ctypes.c_char_p   # icon_path
]
c_lib.GooeyMeter_Create.restype = GooeyMeterPtr

def GooeyMeter_Create(x: int, y: int, width: int, height: int,
                      initial_value: int, label: str, icon_path: str) -> GooeyMeterPtr:
    """
    Create a new Gooey meter.
    """
    return c_lib.GooeyMeter_Create(x, y, width, height, initial_value,
                                   label.encode('utf-8'), icon_path.encode('utf-8'))

# GooeyMeter_Update
c_lib.GooeyMeter_Update.argtypes = [GooeyMeterPtr, ctypes.c_long]
c_lib.GooeyMeter_Update.restype = None

def GooeyMeter_Update(meter: GooeyMeterPtr, new_value: int):
    """
    Update the value of the Gooey meter.
    """
    c_lib.GooeyMeter_Update(meter, new_value)
