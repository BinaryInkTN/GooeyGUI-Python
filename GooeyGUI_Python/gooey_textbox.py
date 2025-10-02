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

class GooeyWindow(ctypes.Structure): pass
class GooeyTextbox(ctypes.Structure):   pass

GooeyTextboxCallback = ctypes.CFUNCTYPE(None, ctypes.c_char_p)

# GooeyTextBox_Create
c_lib.GooeyTextBox_Create.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.c_bool, GooeyTextboxCallback]
c_lib.GooeyTextBox_Create.restype = ctypes.POINTER(GooeyTextbox)

def GooeyTextBox_Create(x: int, y: int, width: int, height: int, placeholder: str, is_password: bool, callback: GooeyTextboxCallback):
    """
    Creates a new GooeyTextbox widget at the specified position and dimensions with optional placeholder text.
    """
    c_placeholder = placeholder.encode('utf-8')
    return c_lib.GooeyTextBox_Create(x, y, width, height, c_placeholder, is_password, callback)

# GooeyTextbox_Draw
c_lib.GooeyTextbox_Draw.argtypes = [ctypes.POINTER(GooeyWindow)]
c_lib.GooeyTextbox_Draw.restype = None

def GooeyTextbox_Draw(window):
    """
    Renders the textbox on the window.
    """
    c_lib.GooeyTextbox_Draw(window)

# GooeyTextbox_HandleClick
c_lib.GooeyTextbox_HandleClick.argtypes = [ctypes.POINTER(GooeyWindow), ctypes.c_int, ctypes.c_int]
c_lib.GooeyTextbox_HandleClick.restype = ctypes.c_bool

def GooeyTextbox_HandleClick(window, x: int, y: int):
    """
    Handles click events on the textbox.
    """
    return c_lib.GooeyTextbox_HandleClick(window, x, y)

# GooeyTextbox_HandleKeyPress
c_lib.GooeyTextbox_HandleKeyPress.argtypes = [ctypes.POINTER(GooeyWindow), ctypes.c_void_p]
c_lib.GooeyTextbox_HandleKeyPress.restype = None

def GooeyTextbox_HandleKeyPress(window, event):
    """
    Handles key press events for the textbox.
    """
    c_lib.GooeyTextbox_HandleKeyPress(window, event)

# GooeyTextbox_GetText
c_lib.GooeyTextbox_GetText.argtypes = [ctypes.POINTER(GooeyTextbox)]
c_lib.GooeyTextbox_GetText.restype = ctypes.c_char_p

def GooeyTextbox_GetText(textbox):
    """
    Retrieves the current text from the textbox.
    """
    return c_lib.GooeyTextbox_GetText(textbox).decode('utf-8')

# GooeyTextbox_SetText
c_lib.GooeyTextbox_setText.argtypes = [ctypes.POINTER(GooeyTextbox), ctypes.c_char_p]
c_lib.GooeyTextbox_setText.restype = None

def GooeyTextbox_SetText(textbox, text: str):
    """
    Sets the text of the textbox.
    """
    c_text = text.encode('utf-8')
    c_lib.GooeyTextbox_setText(textbox, c_text)
