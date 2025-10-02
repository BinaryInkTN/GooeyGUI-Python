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

class GooeyCheckbox(ctypes.Structure): pass

GooeyCheckboxCallback = ctypes.CFUNCTYPE(None, ctypes.c_bool)

# GooeyCheckbox_Create
c_lib.GooeyCheckbox_Create.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p, GooeyCheckboxCallback]
c_lib.GooeyCheckbox_Create.restype = ctypes.POINTER(GooeyCheckbox)

def GooeyCheckbox_Create(x: int, y: int, label: str, callback: GooeyCheckboxCallback):
    """
    Creates a new checkbox in the specified window with the given label.
    The callback is called when the checkbox is clicked, receiving a boolean indicating
    whether the checkbox is checked (True) or unchecked (False).
    """
    label_bytes = label.encode('utf-8')
    
    return c_lib.GooeyCheckbox_Create(x, y, label_bytes, callback)
