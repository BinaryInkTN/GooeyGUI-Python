from gooey_button import *
from gooey_window import *
from gooey_menu import *
from gooey_meter import *
from gooey_canvas import *
from gooey_list import *
from gooey_progressbar import *
from gooey_image import *

@GooeyButtonCallback
def hello_callback():
    print("Hello, World!")

@GooeyMenuCallback
def menu_callback():
    print("hello from menu")

@GooeyImageCallback
def image_callback():
    print("Image clicked")

def main():
    Gooey_Init()

    window = GooeyWindow_Create("Test Window", 1920, 1080, False)
    GooeyWindow_EnableDebugOverlay(window, True)
    button_0 = GooeyButton_Create("Button 1", 50, 50, 100, 30, hello_callback)
    meter_0 = GooeyMeter_Create(50, 100, 200, 30, 0, "Meter", "")
    GooeyWindow_RegisterWidget(window, button_0)
    canvas = GooeyCanvas_Create(50, 150, 400, 400)
    GooeyCanvas_DrawRectangle(canvas, 100, 100, 200, 200, 0xFF0000, True, 1.0, True, 10.0)
    GooeyWindow_RegisterWidget(window, canvas)
    glist = GooeyList_Create(50, 600, 400, 200, hello_callback)
    GooeyList_AddItem(glist, "Item 1", "Description 1")
    GooeyList_AddItem(glist, "Item 2", "Description 2")
    GooeyList_AddItem(glist, "Item 3", "Description 3")
    GooeyList_UpdateItem(glist, 1, "Updated Item 2", "Updated Description 2")
    GooeyList_ShowSeparator(glist, True)
    GooeyList_AddItem(glist, "Item 4", "Description 4")
    GooeyList_AddItem(glist, "Item 4", "Description 4")
    GooeyList_AddItem(glist, "Item 4", "Description 4")
    GooeyList_AddItem(glist, "Item 4", "Description 4")
    GooeyList_AddItem(glist, "Item 4", "Description 4")
    GooeyList_AddItem(glist, "Item 4", "Description 4")
    image_0 = GooeyImage_Create("gooey.png", 50, 800, 200, 200, image_callback)
    menu = GooeyMenu_Set(window)
    GooeyMenuChild = GooeyMenu_AddChild(window, "File")
    GooeyMenuChild_AddElement(GooeyMenuChild, "Hello", menu_callback)
    GooeyWindow_RegisterWidget(window, glist)
    progressbar = GooeyProgressBar_Create(50, 200, 100, 30, 50)

    GooeyWindow_RegisterWidget(window, progressbar)
    GooeyWindow_RegisterWidget(window, image_0)
   
    GooeyWindow_Run(1, window)
    GooeyWindow_Cleanup(1, window)
    
if __name__ == "__main__":
    main()