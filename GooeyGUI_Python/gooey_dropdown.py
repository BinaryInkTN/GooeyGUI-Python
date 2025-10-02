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

class GooeyDropdown(ctypes.Structure): pass

GooeyDropdownCallback = ctypes.CFUNCTYPE(None, ctypes.c_int)

# GooeyDropdown_Create
c_lib.GooeyDropdown_Create.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.c_int, GooeyDropdownCallback]
c_lib.GooeyDropdown_Create.restype = ctypes.POINTER(GooeyDropdown)

def GooeyDropdown_Create(x: int, y: int, width: int, height: int, options: list, callback: GooeyDropdownCallback):
    """
    Creates a new GooeyDropdown menu at the specified position and dimensions.
    The dropdown is populated with the provided list of options. The callback 
    function is called when an option is selected, and it receives the index 
    of the selected option.
    """
    c_options_array = (ctypes.c_char_p * len(options))()
    for i, option in enumerate(options):
        c_options_array[i] = ctypes.c_char_p(option.encode('utf-8'))
    
    c_options = ctypes.cast(c_options_array, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)))
    return c_lib.GooeyDropdown_Create(x, y, width, height, c_options, len(options), callback)

# GooeyDropdown_Update
c_lib.GooeyDropdown_Update.argtypes = [ctypes.POINTER(GooeyDropdown), ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.c_int]
c_lib.GooeyDropdown_Update.restype = None

def GooeyDropdown_Update(dropdown: ctypes.POINTER(GooeyDropdown), new_options: list, num_options: int):
    """
    Updates the options of an existing dropdown menu. The dropdown's appearance 
    and configuration remain unchanged.
    """
    c_options_array = (ctypes.c_char_p * len(new_options))()
    for i, option in enumerate(new_options):
        c_options_array[i] = ctypes.c_char_p(option.encode('utf-8'))
    
    c_options = ctypes.cast(c_options_array, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)))
    c_lib.GooeyDropdown_Update(dropdown, c_options, num_options)
