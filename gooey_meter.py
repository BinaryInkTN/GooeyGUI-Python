from libgooey import *

c_lib.GooeyMeter_Create.argtypes = [
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_char_p,
    ctypes.c_char_p
]

c_lib.GooeyMeter_Create.restype = ctypes.c_void_p

#GooeyMeter *GooeyMeter_Create(int x, int y, int width, int height, long initial_value, const char *label, const char *icon_path)
def GooeyMeter_Create(x: int, y: int, width: int, height: int, initial_value: int, label: str, icon_path: str) -> ctypes.c_void_p:
    """
    Create a new Gooey meter.
    """
    return c_lib.GooeyMeter_Create(x, y, width, height, initial_value, label.encode('utf-8'), icon_path.encode('utf-8'))

#void GooeyMeter_Update(GooeyMeter *meter, long new_value)
