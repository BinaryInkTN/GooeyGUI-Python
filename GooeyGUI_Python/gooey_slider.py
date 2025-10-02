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

from .libgooey import *

class GooeySlider(ctypes.Structure): pass
GooeySliderCallback = ctypes.CFUNCTYPE(None, ctypes.c_long)

# GooeySlider_Create
c_lib.GooeySlider_Create.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, 
                                    ctypes.c_long, ctypes.c_long, ctypes.c_bool, 
                                   GooeySliderCallback]
c_lib.GooeySlider_Create.restype = ctypes.POINTER(GooeySlider)

def GooeySlider_Create(x: int, y: int, width: int, min_value: int, max_value: int, 
                       show_hints: bool, callback: GooeySliderCallback):
    """
    Creates a new slider at the specified position, width, and range, 
    and binds a callback function to notify when the slider value changes.
    """

    return c_lib.GooeySlider_Create(x, y, width, min_value, max_value, show_hints, callback)


"""
# GooeySlider_GetValue
c_lib.GooeySlider_GetValue.argtypes = [ctypes.POINTER(GooeySlider)]
c_lib.GooeySlider_GetValue.restype = ctypes.c_long

def GooeySlider_GetValue(slider):
  
    Returns the current value of the given slider.
  
    return c_lib.GooeySlider_GetValue(slider)

# GooeySlider_SetValue
c_lib.GooeySlider_SetValue.argtypes = [ctypes.POINTER(GooeySlider), ctypes.c_long]
c_lib.GooeySlider_SetValue.restype = None

def GooeySlider_SetValue(slider, value: int):
   
    Sets the value of the given slider to the specified value within its valid range.
  
    c_lib.GooeySlider_SetValue(slider, value)
"""