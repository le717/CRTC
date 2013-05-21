#! python3
# -*- coding: utf-8 -*-
"""
    Cycles Render Time Calculator -  calculate how long your Blender Cycles Engine renders will take.
    Created 2013 Triangle717 & rioforce
    <http://triangle717.wordpress.com/>
    <http://rioforce.wordpress.com/>

    Cycles Render Time Calculator is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Cycles Render Time Calculator is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Cycles Render Time Calculator. If not, see <http://www.gnu.org/licenses/>.

"""
# Cycles Render Time Calculator setup script using cx_Freeze.
# Taken from https://github.com/Lyrositor/EBPatcher
# and https://github.com/JrMasterModelBuilder/JAM-Extractor
# With changes by Triangle717

from cx_Freeze import setup, Executable
import sys

# Append build to the arguments. Just type "python setup.py" and it will compile
if len(sys.argv) == 1: sys.argv[1:] = ["build"]

# Compile into the proper folder depending on the architecture
# Based on code from the Python help file (platform module) and my own tests
if sys.maxsize == 2147483647:
    destfolder = "Compile/Windows32"
else:
    destfolder = "Compile/Windows64"

build_exe_options = {"build_exe": destfolder,
                     "icon": "Icon.ico"}

setup(
    name = "Cycles Render Time Calculator",
    version = "1.2.2",
    author = "Triangle717",
    description = "Cycles Render Time Calculator 1.2.2",
    license = "GNU GPLv3",
    options = {"build_exe": build_exe_options},
    executables = [Executable("CRTC.py", targetName="CRTC.exe")]
)