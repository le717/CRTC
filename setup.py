#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
    Cycles Render Time Calculator (CRTC)
    Calculate approximate GPU render times
    when using the Blender Cycles Engine

    Created 2013 Triangle717 & rioforce
    <http://triangle717.wordpress.com/>
    <http://rioforce.wordpress.com/>

    CRTC is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    CRTC is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with CRTC If not, see <http://www.gnu.org/licenses/>.

-------------------------------------
Cycles Render Time Calculator setup script using cx_Freeze.
Taken from https://github.com/Lyrositor/EBPatcher
and https://github.com/JrMasterModelBuilder/JAM-Extractor
With changes by Triangle717
"""

import sys
from cx_Freeze import (setup, Executable)

# Append 'build' to the arguments.
if len(sys.argv) == 1:
    sys.argv[1:] = ["build"]

# Freeze into the proper folder depending on the architecture
# Based on code from the Python help file (platform module) and my own tests
if sys.maxsize < 2 ** 32:
    destfolder = "Compile/Windows32"
else:
    destfolder = "Compile/Windows64"

build_exe_options = {"build_exe": destfolder,
                     "icon": "Icon.ico"}

setup(
    name="Cycles Render Time Calculator",
    verson="1.3.0",
    author="Triangle717",
    description="Cycles Render Time Calculator 1.3.0",
    license="GPLv3",
    options={"build_exe": build_exe_options},
    executables=[Executable("CRTC.py", targetName="CRTC.exe")]
)
