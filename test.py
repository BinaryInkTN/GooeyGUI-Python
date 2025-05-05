from gooey_button import *
from gooey_window import *
from gooey_menu import *
from gooey_meter import *

def hello_callback():
    print("Hello, World!")

Gooey_Init()

window = GooeyWindow_Create("Test Window", 1920, 1080, False)
GooeyWindow_EnableDebugOverlay(window, True)
button_0 = GooeyButton_Create("Button 1", 50, 50, 100, 30, None)
meter_0 = GooeyMeter_Create(50, 100, 200, 30, 0, "Meter", "")
GooeyWindow_RegisterWidget(window, button_0)

menu = GooeyMenu_Set(window)
GooeyMenuChild = GooeyMenu_AddChild(window, "File")
GooeyMenuChild_AddElement(GooeyMenuChild, "Hello", lambda: print("Hello!"))

GooeyWindow_RegisterWidget(window, meter_0)
GooeyWindow_Run(1, window)
GooeyWindow_Cleanup(1, window)