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


import ctypes
import pathlib
from pathlib import Path
import os 

current_dir = Path(__file__).parent
lib_path = current_dir / "lib" / "libGooeyGUI-1.so"


# Load the shared library libname = "/usr/local/lib/libGooeyGUI.so"
c_lib = ctypes.CDLL(str(lib_path))


# void Gooey_Init(void);
c_lib.Gooey_Init.argtypes = []
c_lib.Gooey_Init.restype = None

# --- Python wrappers ---


def Gooey_Init():
    """
    Initialize the Gooey GUI library.
    """
    c_lib.Gooey_Init()
