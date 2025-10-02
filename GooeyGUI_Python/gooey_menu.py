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

# Define opaque pointer types
class GooeyMenu(ctypes.Structure): pass
class GooeyMenuChild(ctypes.Structure): pass

GooeyMenuPtr = ctypes.POINTER(GooeyMenu)
GooeyMenuChildPtr = ctypes.POINTER(GooeyMenuChild)

GooeyMenuCallback = ctypes.CFUNCTYPE(None)

# GooeyMenu_Set
c_lib.GooeyMenu_Set.argtypes = [ctypes.c_void_p] 
c_lib.GooeyMenu_Set.restype = GooeyMenuPtr

def GooeyMenu_Set(window: ctypes.c_void_p) -> GooeyMenuPtr:
    """
    Sets the menu for the given Gooey window.
    """
    return c_lib.GooeyMenu_Set(window)

# GooeyMenu_AddChild
c_lib.GooeyMenu_AddChild.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
c_lib.GooeyMenu_AddChild.restype = GooeyMenuChildPtr

def GooeyMenu_AddChild(window: ctypes.c_void_p, title: str) -> GooeyMenuChildPtr:
    """
    Adds a child menu (submenu) to the window's menu.
    """
    return c_lib.GooeyMenu_AddChild(window, ctypes.c_char_p(title.encode('utf-8')))

# GooeyMenuChild_AddElement
c_lib.GooeyMenuChild_AddElement.argtypes = [GooeyMenuChildPtr, ctypes.c_char_p, GooeyMenuCallback]
c_lib.GooeyMenuChild_AddElement.restype = None

def GooeyMenuChild_AddElement(child: GooeyMenuChildPtr, title: str, callback: GooeyMenuCallback):
    """
    Adds an item to the given child menu. Callback will be invoked when the item is selected.
    """
    c_lib.GooeyMenuChild_AddElement(child,  ctypes.c_char_p(title.encode('utf-8')), callback)
