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

class GooeyRadioButton(ctypes.Structure): pass
class GooeyRadioButtonGroup(ctypes.Structure): pass
class GooeyWindow(ctypes.Structure): pass

# GooeyRadioButton_Create
c_lib.GooeyRadioButton_Create.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.CFUNCTYPE(None, ctypes.c_bool)]
c_lib.GooeyRadioButton_Create.restype = ctypes.POINTER(GooeyRadioButton)

def GooeyRadioButton_Create(x: int, y: int, label: str, callback):
    """
    Adds a radio button to the window at the specified position with a label and a callback.
    The callback is invoked when the radio button is selected.
    """
    label_bytes = label.encode('utf-8')
    c_callback = ctypes.CFUNCTYPE(None, ctypes.c_bool)(callback)
    
    return c_lib.GooeyRadioButton_Create(x, y, label_bytes, c_callback)

# GooeyRadioButtonGroup_Create
c_lib.GooeyRadioButtonGroup_Create.argtypes = []
c_lib.GooeyRadioButtonGroup_Create.restype = ctypes.POINTER(GooeyRadioButtonGroup)

def GooeyRadioButtonGroup_Create():
    """
    Creates a new radio button group, allowing only one radio button to be selected at a time.
    """
    return c_lib.GooeyRadioButtonGroup_Create()

# GooeyRadioButtonGroup_AddChild
c_lib.GooeyRadioButtonGroup_AddChild.argtypes = [ctypes.POINTER(GooeyWindow), ctypes.POINTER(GooeyRadioButtonGroup), ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.CFUNCTYPE(None, ctypes.c_bool)]
c_lib.GooeyRadioButtonGroup_AddChild.restype = ctypes.POINTER(GooeyRadioButton)

def GooeyRadioButtonGroup_AddChild(win, group, x: int, y: int, label: str, callback):
    """
    Adds a radio button to the specified radio button group within a window.
    """
    label_bytes = label.encode('utf-8')
    c_callback = ctypes.CFUNCTYPE(None, ctypes.c_bool)(callback)
    
    return c_lib.GooeyRadioButtonGroup_AddChild(win, group, x, y, label_bytes, c_callback)

# GooeyRadioButtonGroup_Draw
c_lib.GooeyRadioButtonGroup_Draw.argtypes = [ctypes.POINTER(GooeyWindow)]
c_lib.GooeyRadioButtonGroup_Draw.restype = None

def GooeyRadioButtonGroup_Draw(win):
    """
    Draws the radio button group on the window.
    This ensures that only one radio button is selected at any given time.
    """
    c_lib.GooeyRadioButtonGroup_Draw(win)
