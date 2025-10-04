from .libgooey import *
import ctypes

# Define the GooeyWidget struct and pointer type
class GooeyWidget(ctypes.Structure):
    pass

# --- GooeyWidget_MakeVisible ---
c_lib.GooeyWidget_MakeVisible.argtypes = [ctypes.c_void_p, ctypes.c_bool]
c_lib.GooeyWidget_MakeVisible.restype = None

def GooeyWidget_MakeVisible(widget: ctypes.c_void_p, state: bool):
    """
    Enable or disable widget visibility
    """
    c_lib.GooeyWidget_MakeVisible(widget, state)

# --- GooeyWidget_MoveTo ---
c_lib.GooeyWidget_MoveTo.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
c_lib.GooeyWidget_MoveTo.restype = None

def GooeyWidget_MoveTo(widget: ctypes.c_void_p, x: int, y: int):
    """
    Move widget
    """
    c_lib.GooeyWidget_MoveTo(widget, x, y)

# --- GooeyWidget_Resize ---
c_lib.GooeyWidget_Resize.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
c_lib.GooeyWidget_Resize.restype = None

def GooeyWidget_Resize(widget: ctypes.c_void_p, w: int, h: int):
    """
    Resize widget
    """
    c_lib.GooeyWidget_Resize(widget, w, h)