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

class GooeyLayout(ctypes.Structure): pass

GOOEY_LAYOUT_HORIZONTAL = 0
GOOEY_LAYOUT_VERTICAL = 1
GOOEY_LAYOUT_GRID = 2

GooeyLayoutType = ctypes.c_int

# GooeyLayout_Create
c_lib.GooeyLayout_Create.argtypes = [GooeyLayoutType, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
c_lib.GooeyLayout_Create.restype = ctypes.POINTER(GooeyLayout)

def GooeyLayout_Create(layout_type: GooeyLayoutType, x: int, y: int, width: int, height: int):
    """
    Creates a new layout of the specified type with the given position and size.
    """
    return c_lib.GooeyLayout_Create(layout_type, x, y, width, height)

# GooeyLayout_AddChild
c_lib.GooeyLayout_AddChild.argtypes = [ctypes.POINTER(GooeyLayout), ctypes.c_void_p]
c_lib.GooeyLayout_AddChild.restype = None

def GooeyLayout_AddChild(layout: ctypes.POINTER(GooeyLayout), widget: ctypes.c_void_p):
    """
    Adds a child widget to the specified layout.
    """
    c_lib.GooeyLayout_AddChild(layout, widget)

# GooeyLayout_Build
c_lib.GooeyLayout_Build.argtypes = [ctypes.POINTER(GooeyLayout)]
c_lib.GooeyLayout_Build.restype = None

def GooeyLayout_Build(layout: ctypes.POINTER(GooeyLayout)):
    """
    Arranges all child widgets within the layout.
    """
    c_lib.GooeyLayout_Build(layout)
