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

class GooeyPlot(ctypes.Structure): pass

# GooeyPlot_Create
c_lib.GooeyPlot_Create.argtypes = [ctypes.c_int, ctypes.POINTER(GooeyPlotData), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
c_lib.GooeyPlot_Create.restype = ctypes.POINTER(GooeyPlot)

def GooeyPlot_Create(plot_type: int, data: GooeyPlotData, x: int, y: int, width: int, height: int):
    """
    Creates a new plot widget in the given window at the specified position and dimensions.
    Supports various plot types such as LINE and BAR.
    """
    return c_lib.GooeyPlot_Create(plot_type, ctypes.byref(data), x, y, width, height)

# GooeyPlot_Update
c_lib.GooeyPlot_Update.argtypes = [ctypes.POINTER(GooeyPlot), ctypes.POINTER(GooeyPlotData)]
c_lib.GooeyPlot_Update.restype = None

def GooeyPlot_Update(plot: ctypes.POINTER(GooeyPlot), new_data: GooeyPlotData):
    """
    Updates the data of an existing plot. The plot's appearance and configuration remain unchanged.
    """
    c_lib.GooeyPlot_Update(plot, ctypes.byref(new_data))
