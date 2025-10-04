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

class GooeyProgressBar(ctypes.Structure): pass

# GooeyProgressBar_Create
c_lib.GooeyProgressBar_Create.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_long]
c_lib.GooeyProgressBar_Create.restype = ctypes.POINTER(GooeyProgressBar)

def GooeyProgressBar_Create(x: int, y: int, width: int, height: int, initial_value: int):
    """
    Creates a new GooeyProgressBar widget and attaches it to a window.
    """
    return c_lib.GooeyProgressBar_Create(x, y, width, height, initial_value)

# GooeyProgressBar_Update
c_lib.GooeyProgressBar_Update.argtypes = [ctypes.POINTER(GooeyProgressBar), ctypes.c_long]
c_lib.GooeyProgressBar_Update.restype = None

def GooeyProgressBar_Update(progressbar: ctypes.POINTER(GooeyProgressBar), new_value: int):
    """
    Updates the value of the GooeyProgressBar widget.
    """
    c_lib.GooeyProgressBar_Update(progressbar, new_value)
