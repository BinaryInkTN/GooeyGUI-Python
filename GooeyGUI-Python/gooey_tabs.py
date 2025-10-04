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

class GooeyTabs(ctypes.Structure): pass

# GooeyTabs_Create
c_lib.GooeyTabs_Create.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
c_lib.GooeyTabs_Create.restype = ctypes.POINTER(GooeyTabs)

def GooeyTabs_Create(x: int, y: int, width: int, height: int):
    """
    Creates a new GooeyTabs widget at the specified position and dimensions.
    """
    return c_lib.GooeyTabs_Create(x, y, width, height)

# GooeyTabs_InsertTab
c_lib.GooeyTabs_InsertTab.argtypes = [ctypes.POINTER(GooeyTabs), ctypes.c_char_p]
c_lib.GooeyTabs_InsertTab.restype = None

def GooeyTabs_InsertTab(tabs, tab_name: str):
    """
    Inserts a new tab with the specified name into the GooeyTabs widget.
    """
    c_tab_name = tab_name.encode('utf-8')
    c_lib.GooeyTabs_InsertTab(tabs, c_tab_name)

# GooeyTabs_AddWidget
c_lib.GooeyTabs_AddWidget.argtypes = [ctypes.POINTER(GooeyTabs), ctypes.c_size_t, ctypes.c_void_p]
c_lib.GooeyTabs_AddWidget.restype = None

def GooeyTabs_AddWidget(tabs, tab_id: int, widget):
    """
    Adds a widget to a specific tab in the GooeyTabs widget.
    """
    c_lib.GooeyTabs_AddWidget(tabs, tab_id, widget)

# GooeyTabs_SetActiveTab
c_lib.GooeyTabs_SetActiveTab.argtypes = [ctypes.POINTER(GooeyTabs), ctypes.c_size_t]
c_lib.GooeyTabs_SetActiveTab.restype = None

def GooeyTabs_SetActiveTab(tabs, tab_id: int):
    """
    Sets the active tab in the GooeyTabs widget.
    """
    c_lib.GooeyTabs_SetActiveTab(tabs, tab_id)
