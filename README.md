# GooeyGUI Python

Python bindings for the **Gooey** GUI library.

**GooeyGUI** allows you to create and manage GUI applications in Python using the **Gooey** C library.

## Installation

### Step 1: Install the C library

Follow the instructions in the main **Gooey** C repository to compile the library and generate the shared library (`.so`, `.dll`, or `.dylib`).

### Step 2: Install the Python bindings

1. Clone this repository or download the Python bindings.
2. Ensure the compiled shared library (`libgooey.so`, `libgooey.dll`, or `libgooey.dylib`) is available in the same directory as the Python bindings.
3. Install the required dependencies:

   ```bash
   pip install ctypes
   ```
