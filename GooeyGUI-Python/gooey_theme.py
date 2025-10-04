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
import ctypes

# Theme Structure
class GooeyTheme(ctypes.Structure):
    _fields_ = [
        ("base", ctypes.c_uint32),
        ("neutral", ctypes.c_uint32),
        ("primary", ctypes.c_uint32),
        ("widget_base", ctypes.c_uint32),
        ("danger", ctypes.c_uint32),
        ("info", ctypes.c_uint32),
        ("success", ctypes.c_uint32)
    ]

# Theme Function Bindings

# GooeyTheme_LoadFromFile
c_lib.GooeyTheme_LoadFromFile.argtypes = [ctypes.c_char_p]
c_lib.GooeyTheme_LoadFromFile.restype = ctypes.POINTER(GooeyTheme)

def GooeyTheme_LoadFromFile(theme_path: str):
    """
    Loads a theme from a file and returns a pointer to the loaded theme.
    
    Args:
        theme_path (str): Path to the theme file
        
    Returns:
        ctypes.POINTER(GooeyTheme): Pointer to the loaded theme, or None if failed
    """
    return c_lib.GooeyTheme_LoadFromFile(theme_path.encode('utf-8'))

# GooeyTheme_LoadFromString
c_lib.GooeyTheme_LoadFromString.argtypes = [ctypes.c_char_p]
c_lib.GooeyTheme_LoadFromString.restype = ctypes.POINTER(GooeyTheme)

def GooeyTheme_LoadFromString(styling: str):
    """
    Loads a theme from a string and returns a pointer to the loaded theme.
    
    Args:
        styling (str): Theme styling as a string
        
    Returns:
        ctypes.POINTER(GooeyTheme): Pointer to the loaded theme, or None if failed
    """
    return c_lib.GooeyTheme_LoadFromString(styling.encode('utf-8'))

# GooeyTheme_Destroy
c_lib.GooeyTheme_Destroy.argtypes = [ctypes.POINTER(GooeyTheme)]
c_lib.GooeyTheme_Destroy.restype = None

def GooeyTheme_Destroy(theme):
    """
    Destroys a theme and frees its memory.
    
    Args:
        theme: Pointer to the GooeyTheme to destroy
    """
    c_lib.GooeyTheme_Destroy(theme)

# Window Theme Functions

# GooeyWindow_SetTheme
c_lib.GooeyWindow_SetTheme.argtypes = [ctypes.c_void_p, ctypes.POINTER(GooeyTheme)]
c_lib.GooeyWindow_SetTheme.restype = None

def GooeyWindow_SetTheme(win, theme):
    """
    Sets the active theme for a window.
    
    Args:
        win: Pointer to the GooeyWindow
        theme: Pointer to the GooeyTheme to set as active
    """
    c_lib.GooeyWindow_SetTheme(win, theme)

# Helper function to create a theme from Python values
def CreateTheme(base=0xFFFFFF, neutral=0x000000, primary=0x2196F3, 
                widget_base=0xD3D3D3, danger=0xE91E63, info=0x2196F3, 
                success=0x00A152):
    """
    Creates a new theme with the specified color values.
    
    Args:
        base (int): Base color (default: white)
        neutral (int): Neutral color (default: black)
        primary (int): Primary color (default: blue)
        widget_base (int): Widget base color (default: light gray)
        danger (int): Danger color (default: pink/red)
        info (int): Info color (default: blue)
        success (int): Success color (default: green)
        
    Returns:
        GooeyTheme: A new theme structure with the specified colors
    """
    return GooeyTheme(
        base=base,
        neutral=neutral,
        primary=primary,
        widget_base=widget_base,
        danger=danger,
        info=info,
        success=success
    )

# Helper function to convert theme to dictionary
def ThemeToDict(theme_ptr):
    """
    Converts a theme pointer to a Python dictionary.
    
    Args:
        theme_ptr: Pointer to GooeyTheme
        
    Returns:
        dict: Dictionary containing theme colors
    """
    if not theme_ptr:
        return None
    
    theme = theme_ptr.contents
    return {
        'base': theme.base,
        'neutral': theme.neutral,
        'primary': theme.primary,
        'widget_base': theme.widget_base,
        'danger': theme.danger,
        'info': theme.info,
        'success': theme.success
    }

# Helper function to create theme from dictionary
def ThemeFromDict(theme_dict):
    """
    Creates a theme from a dictionary.
    
    Args:
        theme_dict (dict): Dictionary containing theme colors
        
    Returns:
        GooeyTheme: New theme structure
    """
    return CreateTheme(
        base=theme_dict.get('base', 0xFFFFFF),
        neutral=theme_dict.get('neutral', 0x000000),
        primary=theme_dict.get('primary', 0x2196F3),
        widget_base=theme_dict.get('widget_base', 0xD3D3D3),
        danger=theme_dict.get('danger', 0xE91E63),
        info=theme_dict.get('info', 0x2196F3),
        success=theme_dict.get('success', 0x00A152)
    )

# Context manager for theme management
class ThemeManager:
    """
    Context manager for automatic theme resource management.
    """
    def __init__(self, theme_source=None, from_file=False, from_string=False):
        self.theme_ptr = None
        self.theme_source = theme_source
        self.from_file = from_file
        self.from_string = from_string
        
    def __enter__(self):
        if self.from_file and self.theme_source:
            self.theme_ptr = GooeyTheme_LoadFromFile(self.theme_source)
        elif self.from_string and self.theme_source:
            self.theme_ptr = GooeyTheme_LoadFromString(self.theme_source)
        else:
            # Create default theme
            self.theme_ptr = GooeyTheme_LoadFromString("")
            
        if not self.theme_ptr:
            raise RuntimeError(f"Failed to load theme from {self.theme_source}")
            
        return self.theme_ptr
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.theme_ptr:
            GooeyTheme_Destroy(self.theme_ptr)