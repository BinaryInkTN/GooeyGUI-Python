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

class GooeyButton(ctypes.Structure):
    pass

GooeyButtonPtr = ctypes.POINTER(GooeyButton)

GooeyButtonCallback = ctypes.CFUNCTYPE(None)

# GooeyButton_Create
c_lib.GooeyButton_Create.argtypes = [
    ctypes.c_char_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    GooeyButtonCallback
]
c_lib.GooeyButton_Create.restype = GooeyButtonPtr

def GooeyButton_Create(label: str, x: int, y: int, width: int, height: int,
                       callback: GooeyButtonCallback) -> GooeyButtonPtr:
    """
    Create a new Gooey button.
    """
    return c_lib.GooeyButton_Create(label.encode('utf-8'), x, y, width, height, callback)


# GooeyButton_SetText
c_lib.GooeyButton_SetText.argtypes = [GooeyButtonPtr, ctypes.c_char_p]
c_lib.GooeyButton_SetText.restype = None

def GooeyButton_SetText(button: GooeyButtonPtr, text: str):
    """
    Set the text label of a Gooey button.
    """
    c_lib.GooeyButton_SetText(button, text.encode('utf-8'))


# GooeyButton_SetHighlight
c_lib.GooeyButton_SetHighlight.argtypes = [GooeyButtonPtr, ctypes.c_bool]
c_lib.GooeyButton_SetHighlight.restype = None

def GooeyButton_SetHighlight(button: GooeyButtonPtr, is_highlighted: bool):
    """
    Highlight or unhighlight a Gooey button.
    """
    c_lib.GooeyButton_SetHighlight(button, is_highlighted)
    
# GooeyButton_SetEnabled
c_lib.GooeyButton_SetEnabled.argtypes = [GooeyButtonPtr, ctypes.c_bool]
c_lib.GooeyButton_SetEnabled.restype = None

def GooeyButton_SetEnabled(button: GooeyButtonPtr, is_enabled: bool):
    """
    Enable or Disable a Gooey button.
    """
    c_lib.GooeyButton_SetEnabled(button, is_enabled)
