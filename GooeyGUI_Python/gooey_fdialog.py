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
import typing

#list
GooeyFDialogCallback = ctypes.CFUNCTYPE(ctypes.c_char_p)

# GooeyFDialog_Open
c_lib.GooeyFDialog_Open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p), ctypes.c_int, GooeyFDialogCallback]
c_lib.GooeyFDialog_Open.restype = None
#         GooeyFDialog_Open(current_path, [["All Files (*.*)"], ["*.*"]], 1, file_dialog_callback)
def GooeyFDialog_Open(path: str, filters: list[list[str]], callback):
    """
    Opens a file dialog with the specified title and message.
    filters: List of two lists: [descriptions], [extensions]
    """
    c_callback = GooeyFDialogCallback(callback)
    path_bytes = path.encode('utf-8')
    descriptions = filters[0]
    extensions = filters[1]
    filters_bytes = []
    for desc, ext in zip(descriptions, extensions):
        filters_bytes.append(desc.encode('utf-8'))
        filters_bytes.append(ext.encode('utf-8'))
    filters_array = (ctypes.c_char_p * len(filters_bytes))(*filters_bytes)
    c_lib.GooeyFDialog_Open(path_bytes, filters_array, 2, c_callback)
