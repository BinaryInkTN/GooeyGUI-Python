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


# --- Debug  ---
#void GooeyWindow_EnableDebugOverlay(GooeyWindow *win, bool is_enabled)
c_lib.GooeyWindow_EnableDebugOverlay.argtypes = [ctypes.c_void_p, ctypes.c_bool]
c_lib.GooeyWindow_EnableDebugOverlay.restype = None
def GooeyWindow_EnableDebugOverlay(window: ctypes.c_void_p, is_enabled: bool):
    """
    Enable or disable the debug overlay for the Gooey window.
    """
    c_lib.GooeyWindow_EnableDebugOverlay(window, is_enabled)

# void* GooeyWindow_Create(const char* title,int width, int height);
c_lib.GooeyWindow_Create.argtypes = [
    ctypes.c_char_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_bool
]
c_lib.GooeyWindow_Create.restype = ctypes.c_void_p

def GooeyWindow_Create(title: str, width: int, height: int, visibiliy: bool) -> ctypes.c_void_p:
    """
    Create a new Gooey window.
    """
    return c_lib.GooeyWindow_Create(title.encode('utf-8'), width, height, visibiliy)

# void GooeyWindow_Run(int num_windows, void* window);
c_lib.GooeyWindow_Run.argtypes = [ctypes.c_int, ctypes.c_void_p]
c_lib.GooeyWindow_Run.restype = None
#TODO: FIX THIS ASAP ON C SIDE
def GooeyWindow_Run(num_windows: int, window: ctypes.c_void_p):
    """
    Run the Gooey windows.
    """
    c_lib.GooeyWindow_Run(num_windows, window)

c_lib.GooeyWindow_Cleanup.argtypes = [ctypes.c_int, ctypes.c_void_p]
c_lib.GooeyWindow_Cleanup.restype = None
def GooeyWindow_Cleanup(num_windows: int, window: ctypes.c_void_p):
    """
    Destroy the Gooey windows.
    """
    c_lib.GooeyWindow_Cleanup(num_windows, window)
    
c_lib.GooeyWindow_RegisterWidget.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
c_lib.GooeyWindow_RegisterWidget.restype = None
def GooeyWindow_RegisterWidget(window: ctypes.c_void_p, widget: ctypes.c_void_p):
    """
    Register a widget with the Gooey window.
    """
    c_lib.GooeyWindow_RegisterWidget(window, widget)

c_lib.GooeyWindow_MakeResizable.argtypes = [ctypes.c_void_p, ctypes.c_bool]
c_lib.GooeyWindow_MakeResizable.restype = None
def GooeyWindow_MakeResizable(window: ctypes.c_void_p, state: ctypes.c_bool):
    """
    Manage visibility on a Gooey window.
    """
    c_lib.GooeyWindow_MakeResizable(window, state)
    
c_lib.GooeyWindow_RequestCleanup.argtypes = [ctypes.c_void_p]
c_lib.GooeyWindow_RequestCleanup.restype = None
def GooeyWindow_RequestCleanup(window: ctypes.c_void_p):
    """
    Request cleanup for a Gooey window.
    """
    c_lib.GooeyWindow_RequestCleanup(window)