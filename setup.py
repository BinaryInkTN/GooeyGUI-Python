from setuptools import setup, find_packages
from setuptools.command.build_py import build_py
from setuptools.command.develop import develop
import subprocess
import os
import sys
import platform
import glob

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

class BuildCLibraryMixin:
    """Mixin to build the C library"""
    
    def build_c_library(self):
        """Clone and compile the external C library"""
        c_lib_repo = "https://github.com/BinaryInkTN/GooeyGUI.git"
        build_dir = "tmp_build"
        original_dir = os.getcwd()
        
        print("=== Starting C library build process ===")
        
        try:
            # Clone the repository
            print(f"Cloning repository from {c_lib_repo}...")
            if not os.path.exists(build_dir):
                
                # subprocess.check_call(["rm", "-rf", build_dir])
            
                result = subprocess.run(
                    ["git", "clone", "--recursive", c_lib_repo, build_dir],
                    capture_output=True, text=True, check=True
                )
                print("Repository cloned successfully")
            
            # Build with CMake
            build_path = os.path.join(build_dir, "build")
            if not os.path.exists(build_path):

                print(f"Creating build directory: {build_path}")
                os.makedirs(build_path, exist_ok=True)
                os.chdir(build_path)
            
                # Configure with CMake
                print("Running cmake...")
                result = subprocess.run(["cmake", ".."], capture_output=True, text=True, check=True)
                print("CMake configuration successful")
            
                # Build the library
                print("Building library with make...")
                result = subprocess.run(["make", "-j4"], capture_output=True, text=True, check=True)
                print("Library built successfully")
            
            # Return to original directory
            os.chdir(original_dir)
            lib_path= os.path.join(build_path,"lib");
            # Find ALL built libraries (more comprehensive search)

            target_path=os.path.join(original_dir,"GooeyGUI-Python/lib")
            print("Searching for compiled libraries...")
            target_path = os.path.join(lib_path, "libGooeyGUI-1.so")
            subprocess.check_call(["cp", lib_path, target_path])
            print(f"Successfully copied {lib_path} to {target_path}")
                
            # Cleanup
            print("Cleaning up build directory...")
            # subprocess.check_call(["rm", "-rf", build_dir])
            print("=== C library build completed ===")
            
        except subprocess.CalledProcessError as e:
            print(f"=== Build failed with subprocess error: {e} ===")
            print(f"Command output: {e.stderr}")
            os.chdir(original_dir)
            
            # Create placeholder to allow installation to continue
        except Exception as e:
            print(f"=== Build failed with unexpected error: {e} ===")
            os.chdir(original_dir)
            raise

class CustomBuildPyCommand(BuildCLibraryMixin, build_py):
    """Custom build command that builds C library first"""
    
    def run(self):
        self.build_c_library()
        super().run()

class CustomDevelopCommand(BuildCLibraryMixin, develop):
    """Custom develop command that builds C library first"""
    
    def run(self):
        self.build_c_library()
        super().run()

# Always use custom commands (they handle failures gracefully)
cmdclass = {
    'build_py': CustomBuildPyCommand,
    'develop': CustomDevelopCommand,
}

setup(
    name="GooeyGUI_Python",
    version="1.0.2",
    author="BinaryInk",
    author_email="contact@binaryink.dev",
    description="A Python GUI library ported from C",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    package_data={
        "GooeyGUI_Python": ["lib/*.so", "lib/*.dll", "lib/*.dylib", "lib/*.a"]
    },
    include_package_data=True, 
    install_requires=[],
    cmdclass=cmdclass,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    keywords="gui, ui, widgets, graphics",
    url="https://github.com/BinaryInkTN/GooeyGUI-Python.git",
    project_urls={
        "Bug Tracker": "https://github.com/BinaryInkTN/GooeyGUI-Python/issues",
        "Source Code": "https://github.com/BinaryInkTN/GooeyGUI-Python",
    },
)
