from GooeyGUI_Python.gooey_window import GooeyWindow_Create, GooeyWindow_MakeResizable, GooeyWindow_RegisterWidget, GooeyWindow_Run, GooeyWindow_Cleanup, GooeyWindow_RequestCleanup
from GooeyGUI_Python.gooey_widget import Gooey_Init

def main():
    Gooey_Init()
    win = GooeyWindow_Create("Gooey test window", 600, 500, True)
    GooeyWindow_Run(1, win)
    GooeyWindow_Cleanup(1, win)

if __name__ == '__main__':
    main()
