"""
 Copyright (c) 2025 Yassine Ahmed Ali

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANContainerILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

from .libgooey import *

class GooeyContainer(ctypes.Structure): pass

# GooeyContainer_Create
c_lib.GooeyContainer_Create.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
c_lib.GooeyContainer_Create.restype = ctypes.POINTER(GooeyContainer)

def GooeyContainer_Create(x: int, y: int, width: int, height: int):
    """
    Creates a new GooeyContainer widget at the specified position and dimensions.
    """
    return c_lib.GooeyContainer_Create(x, y, width, height)

# GooeyContainer_InsertContainer
c_lib.GooeyContainer_InsertContainer.argtypes = [ctypes.POINTER(GooeyContainer)]
c_lib.GooeyContainer_InsertContainer.restype = None

def GooeyContainer_InsertContainer(Container):
    """
    Inserts a new Container with the specified name into the GooeyContainer widget.
    """
    c_lib.GooeyContainer_InsertContainer(Container)

# GooeyContainer_AddWidget
c_lib.GooeyContainer_AddWidget.argtypes = [ctypes.c_void_p, ctypes.POINTER(GooeyContainer), ctypes.c_size_t, ctypes.c_void_p]
c_lib.GooeyContainer_AddWidget.restype = None

def GooeyContainer_AddWidget(Window, Container, Container_id: int, widget):
    """
    Adds a widget to a specific Container in the GooeyContainer widget.
    """
    c_lib.GooeyContainer_AddWidget(Window, Container, Container_id, widget)

# GooeyContainer_SetActiveContainer
c_lib.GooeyContainer_SetActiveContainer.argtypes = [ctypes.POINTER(GooeyContainer), ctypes.c_size_t]
c_lib.GooeyContainer_SetActiveContainer.restype = None

def GooeyContainer_SetActiveContainer(Container, Container_id: int):
    """
    Sets the active Container in the GooeyContainer widget.
    """
    c_lib.GooeyContainer_SetActiveContainer(Container, Container_id)
