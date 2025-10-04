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

class GooeyImage(ctypes.Structure): pass
GooeyImageCallback = ctypes.CFUNCTYPE(None)

# GooeyImage_Create
c_lib.GooeyImage_Create.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, GooeyImageCallback]
c_lib.GooeyImage_Create.restype = ctypes.POINTER(GooeyImage)

def GooeyImage_Create(image_path: str, x: int, y: int, width: int, height: int, callback: GooeyImageCallback):
    """
    Creates a GooeyImage and adds it to the window at the specified position and dimensions.
    """

    return c_lib.GooeyImage_Create(image_path.encode('utf-8'), x, y, width, height, callback)

# GooeyImage_SetImage
c_lib.GooeyImage_SetImage.argtypes = [ctypes.POINTER(GooeyImage), ctypes.c_char_p]
c_lib.GooeyImage_SetImage.restype = None

def GooeyImage_SetImage(image: ctypes.POINTER(GooeyImage), image_path: str):
    """
    Sets a new image for an existing GooeyImage.
    """
    c_lib.GooeyImage_SetImage(image, image_path.encode('utf-8'))

# GooeyImage_Damage
c_lib.GooeyImage_Damage.argtypes = [ctypes.POINTER(GooeyImage)]
c_lib.GooeyImage_Damage.restype = None

def GooeyImage_Damage(image: ctypes.POINTER(GooeyImage)):
    """
    Marks the image as damaged and triggers a redraw.
    """
    c_lib.GooeyImage_Damage(image)
