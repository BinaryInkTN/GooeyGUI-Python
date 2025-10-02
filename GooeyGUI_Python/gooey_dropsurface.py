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

class GooeyDropSurface(ctypes.Structure): pass

# GooeyDropSurface_Create
c_lib.GooeyDropSurface_Create.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_char_p)]
c_lib.GooeyDropSurface_Create.restype = ctypes.POINTER(GooeyDropSurface)

def GooeyDropSurface_Create(x: int, y: int, width: int, height: int, default_message: str, callback):
    """
    Creates a new GooeyDropSurface that allows users to drop files onto it.
    The callback is triggered with the MIME type and file path of the dropped file.
    """
    default_message_bytes = default_message.encode('utf-8')
    c_callback = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_char_p)(callback)
    
    return c_lib.GooeyDropSurface_Create(x, y, width, height, default_message_bytes, c_callback)

# GooeyDropSurface_Clear
c_lib.GooeyDropSurface_Clear.argtypes = [ctypes.POINTER(GooeyDropSurface)]
c_lib.GooeyDropSurface_Clear.restype = None

def GooeyDropSurface_Clear(drop_surface):
    """
    Clears the content of the drop surface, restoring the default message.
    """
    c_lib.GooeyDropSurface_Clear(drop_surface)
