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

from libgooey import *

# void* GooeyButton_Create(const char* label, int x, int y, int width, int height, void (*callback)());
c_lib.GooeyButton_Create.argtypes = [
    ctypes.c_char_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_void_p
]
c_lib.GooeyButton_Create.restype = ctypes.c_void_p

def GooeyButton_Create(label: str, x: int, y: int, width: int, height: int, callback: ctypes.c_void_p) -> ctypes.c_void_p:
    """
    Create a new Gooey button.
    """
    return c_lib.GooeyButton_Create(label.encode('utf-8'), x, y, width, height, callback)


