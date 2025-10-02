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

#list
class GooeyList(ctypes.Structure): pass
GooeyListCallback = ctypes.CFUNCTYPE(ctypes.c_int)

# GooeyList_Create
c_lib.GooeyList_Create.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.CFUNCTYPE(None, ctypes.c_int)]
c_lib.GooeyList_Create.restype = ctypes.POINTER(GooeyList)

def GooeyList_Create(x: int, y: int, width: int, height: int, callback: GooeyListCallback):
    """
    Creates a new GooeyList widget and attaches it to a window.
    """
    c_callback = ctypes.CFUNCTYPE(None, ctypes.c_int)(callback)
    return c_lib.GooeyList_Create(x, y, width, height, c_callback)

# GooeyList_AddItem
c_lib.GooeyList_AddItem.argtypes = [ctypes.POINTER(GooeyList), ctypes.c_char_p, ctypes.c_char_p]
c_lib.GooeyList_AddItem.restype = None

def GooeyList_AddItem(list_widget: ctypes.POINTER(GooeyList), title: str, description: str):
    """
    Adds an item to the GooeyList widget.
    """
    title_bytes = title.encode('utf-8')
    description_bytes = description.encode('utf-8')
    c_lib.GooeyList_AddItem(list_widget, title_bytes, description_bytes)

# GooeyList_ClearItems
c_lib.GooeyList_ClearItems.argtypes = [ctypes.POINTER(GooeyList)]
c_lib.GooeyList_ClearItems.restype = None

def GooeyList_ClearItems(list_widget: ctypes.POINTER(GooeyList)):
    """
    Clears all items from the GooeyList widget.
    """
    c_lib.GooeyList_ClearItems(list_widget)

# GooeyList_ShowSeparator
c_lib.GooeyList_ShowSeparator.argtypes = [ctypes.POINTER(GooeyList), ctypes.c_bool]
c_lib.GooeyList_ShowSeparator.restype = None

def GooeyList_ShowSeparator(list_widget: ctypes.POINTER(GooeyList), state: bool):
    """
    Toggles the visibility of the separator in the GooeyList widget.
    """
    c_lib.GooeyList_ShowSeparator(list_widget, state)

# GooeyList_UpdateItem
c_lib.GooeyList_UpdateItem.argtypes = [ctypes.POINTER(GooeyList), ctypes.c_size_t, ctypes.c_char_p, ctypes.c_char_p]
c_lib.GooeyList_UpdateItem.restype = None

def GooeyList_UpdateItem(list_widget: ctypes.POINTER(GooeyList), item_index: int, title: str, description: str):
    """
    Updates a specific item in the GooeyList widget.
    """
    title_bytes = title.encode('utf-8')
    description_bytes = description.encode('utf-8')
    c_lib.GooeyList_UpdateItem(list_widget, item_index, title_bytes, description_bytes)
