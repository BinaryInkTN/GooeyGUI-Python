
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

class GooeyWindow(ctypes.Structure): pass

# GooeyMessageBox_Create
c_lib.GooeyMessageBox_Create.argtypes = [ctypes.c_char_p, ctypes.c_char_p, MSGBOX_TYPE, ctypes.CFUNCTYPE(None, ctypes.c_int)]
c_lib.GooeyMessageBox_Create.restype = ctypes.POINTER(GooeyWindow)

def GooeyMessageBox_Create(title: str, message: str, msg_type: int, callback):
    """
    Creates a message box with a given title, message, type, and callback to handle user input.
    The callback is triggered when the user interacts with the message box.
    """
    title_bytes = title.encode('utf-8')
    message_bytes = message.encode('utf-8')
    
    c_callback = ctypes.CFUNCTYPE(None, ctypes.c_int)(callback)
    
    return c_lib.GooeyMessageBox_Create(title_bytes, message_bytes, msg_type, c_callback)

# GooeyMessageBox_Show
c_lib.GooeyMessageBox_Show.argtypes = [ctypes.POINTER(GooeyWindow)]
c_lib.GooeyMessageBox_Show.restype = None

def GooeyMessageBox_Show(msgBoxWindow):
    """
    Displays the specified message box window.
    """
    c_lib.GooeyMessageBox_Show(msgBoxWindow)
