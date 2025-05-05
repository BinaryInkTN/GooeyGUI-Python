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


from libgooey import *  # Assuming c_lib is defined in libgooey.py

# void GooeyMenu_Set(void* window);
c_lib.GooeyMenu_Set.argtypes = [ctypes.c_void_p]
c_lib.GooeyMenu_Set.restype = ctypes.c_void_p

def GooeyMenu_Set(window: ctypes.c_void_p) -> ctypes.c_void_p:
    """
    Sets a new Gooey menu.
    """
    return c_lib.GooeyMenu_Set(window)

# GooeyMenuChild *GooeyMenu_AddChild(GooeyWindow *win, char *title)
c_lib.GooeyMenu_AddChild.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
c_lib.GooeyMenu_AddChild.restype = ctypes.c_void_p

def GooeyMenu_AddChild(window: ctypes.c_void_p, title: str) -> ctypes.c_void_p:
    """
    Adds a child to the Gooey menu.
    """
    return c_lib.GooeyMenu_AddChild(window, title.encode('utf-8'))

# void GooeyMenuChild_AddElement(GooeyMenuChild *child, char *title, void (*callback)())
c_lib.GooeyMenuChild_AddElement.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.CFUNCTYPE(None)]
c_lib.GooeyMenuChild_AddElement.restype = None

def GooeyMenuChild_AddElement(child: ctypes.c_void_p, title: str, callback: callable):
    """
    Adds an element to the Gooey menu child.
    """
    if not callable(callback):
        raise TypeError("The callback must be a callable function.")
    
    # TODO: FIX THIS ASAP
    c_callback = ctypes.CFUNCTYPE(None)(callback)
    c_lib.GooeyMenuChild_AddElement(child, title.encode('utf-8'), c_callback)