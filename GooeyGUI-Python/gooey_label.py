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
import ctypes

class GooeyLabel(ctypes.Structure): pass

# GooeyLabel_Create
c_lib.GooeyLabel_Create.argtypes = [ctypes.c_char_p, ctypes.c_float, ctypes.c_int, ctypes.c_int]
c_lib.GooeyLabel_Create.restype = ctypes.POINTER(GooeyLabel)

def GooeyLabel_Create(text: str, font_size: float, x: int, y: int):
    """
    Creates a new GooeyLabel widget and attaches it to a window.
    """
    text_bytes = text.encode('utf-8')  
    return c_lib.GooeyLabel_Create(text_bytes, font_size, x, y)

# GooeyLabel_SetText
c_lib.GooeyLabel_SetText.argtypes = [ctypes.POINTER(GooeyLabel), ctypes.c_char_p]
c_lib.GooeyLabel_SetText.restype = None

def GooeyLabel_SetText(label: ctypes.POINTER(GooeyLabel), text: str):
    """
    Updates the text of an existing label.
    """
    text_bytes = text.encode('utf-8')  
    c_lib.GooeyLabel_SetText(label, text_bytes)

# GooeyLabel_SetColor
c_lib.GooeyLabel_SetColor.argtypes = [ctypes.POINTER(GooeyLabel), ctypes.c_ulong]
c_lib.GooeyLabel_SetColor.restype = None

def GooeyLabel_SetColor(label: ctypes.POINTER(GooeyLabel), color: int):
    """
    Sets the text color of the label.
    """
    c_lib.GooeyLabel_SetColor(label, color)
