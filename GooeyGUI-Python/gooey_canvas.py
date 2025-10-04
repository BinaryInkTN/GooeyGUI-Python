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

class GooeyCanvas(ctypes.Structure): pass

GooeyCanvasPtr = ctypes.POINTER(GooeyCanvas)

GooeyCanvasCallback = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

# GooeyCanvas_Create
c_lib.GooeyCanvas_Create.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, GooeyCanvasCallback]
c_lib.GooeyCanvas_Create.restype = GooeyCanvasPtr

from typing import Any

def GooeyCanvas_Create(x: int, y: int, width: int, height: int, callback) -> GooeyCanvasPtr:
    """
    Creates a new GooeyCanvas.
    """
    return c_lib.GooeyCanvas_Create(x, y, width, height, callback)

# GooeyCanvas_DrawRectangle
c_lib.GooeyCanvas_DrawRectangle.argtypes = [
    ctypes.POINTER(GooeyCanvas),
    ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.c_ulong, ctypes.c_bool, ctypes.c_float, ctypes.c_bool, ctypes.c_float
]
c_lib.GooeyCanvas_DrawRectangle.restype = None

def GooeyCanvas_DrawRectangle(canvas: ctypes.POINTER(GooeyCanvas), x: int, y: int, width: int, height: int,
                              color_hex: int, is_filled: bool, thickness: float, is_rounded: bool, corner_radius: float):
    """
    Draws a rectangle on the canvas.
    """
    c_lib.GooeyCanvas_DrawRectangle(canvas, x, y, width, height, color_hex, is_filled, thickness, is_rounded, corner_radius)

# GooeyCanvas_DrawLine
c_lib.GooeyCanvas_DrawLine.argtypes = [
    ctypes.POINTER(GooeyCanvas),
    ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.c_ulong
]
c_lib.GooeyCanvas_DrawLine.restype = None

def GooeyCanvas_DrawLine(canvas: ctypes.POINTER(GooeyCanvas), x1: int, y1: int, x2: int, y2: int, color_hex: int):
    """
    Draws a line on the canvas.
    """
    c_lib.GooeyCanvas_DrawLine(canvas, x1, y1, x2, y2, color_hex)

# GooeyCanvas_DrawArc
c_lib.GooeyCanvas_DrawArc.argtypes = [
    ctypes.POINTER(GooeyCanvas),
    ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.c_int, ctypes.c_int
]
c_lib.GooeyCanvas_DrawArc.restype = None

def GooeyCanvas_DrawArc(canvas: ctypes.POINTER(GooeyCanvas), x_center: int, y_center: int, width: int, height: int, angle1: int, angle2: int):
    """
    Draws an arc on the canvas.
    """
    c_lib.GooeyCanvas_DrawArc(canvas, x_center, y_center, width, height, angle1, angle2)

# GooeyCanvas_SetForeground
c_lib.GooeyCanvas_SetForeground.argtypes = [ctypes.POINTER(GooeyCanvas), ctypes.c_ulong]
c_lib.GooeyCanvas_SetForeground.restype = None

def GooeyCanvas_SetForeground(canvas: ctypes.POINTER(GooeyCanvas), color_hex: int):
    """
    Sets the foreground color of the canvas.
    """
    c_lib.GooeyCanvas_SetForeground(canvas, color_hex)