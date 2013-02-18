Cycles Render Time Calculator
=============================

This is the readme to **Cycles Render Time Calculator**, a [Python 3](http://www.python.org) application written by [le717](http://triangle717.wordpress.com) and [rioforce](rioforce.wordpress.com) to calculate render times in [Blender] (http://www.blender.org) when using the Cycles Engine.

Why Was This Created
--------------------

It is said that "Necessity is the mother of invention". Well, that can be said of this tool. rioforce and I were always spending lots of time trying to figure 
out when his render would be completed, and we were tired of it. We finally thought that a program should be written to do this for us. Then this program was 
born. Using my knowledge of Python and his Blender skills, we created this small program to calculate render times for both still images and videos.

How It Works
------------

**Cycles Render Time Calculator** supports both the Tile and Progressive Refine render methods for both still images and animations, as well as a general 
animation render (render engine neutral). Blender Internal is not supported, and if it were, it would not have Cycles in the name.

For tile render, simply enter the number of tiles it takes to render your image, and how long it takes (in seconds) to render a single tile (milliseconds 
are supported). This info can easily be found in the Render Window. **Cycles Render Time Calculator** will then calculate an approximate render time. If you 
are rendering an animation (AKA video or "multi-frame" animation), press 'y' when prompted, enter the number of frames your video has, and an approximate 
animation render time will be calculated.

For progressive refine, enter the number of samples in your render, and how long it takes (in seconds) a single sample to render. Again, milliseconds are 
supported. This info can also be found in the Render Window.

The animation render asks only two questions: number of frames, and the time it takes for a single frame to render.

In all modes, render time will be displayed in either seconds, minutes, or hours, depending on the input and the result of the calculations.

*Approximate* is the keyword here. While the render times are accurate if all system variables remain constant, that is an impossible feat to achieve. Thus, 
the final render times will be different than the stated time. For example, it calculated a 6.5 minute render time for me, and it really took 5 minutes.

Releases
--------

* While **Cycles Render Time Calculator** is written in Python 3.3, it runs perfectly on Python 3.2. You will need to have a complete installation of Python 
`>=` 3.2 to run the Python script directly. Any version of Python `<=` 3.1 (including 2.7) is not tested or supported, and a version check will prevent it from 
running on unsupported versions.

* Releases will be compiled into Windows x86, x64 EXEs and Mac OS X application using [cx_freeze](http://cx-freeze.sourceforge.net). 

* Windows build has been sucessfully tested on x64 Windows 7 and 8. However, Vista (and possibly XP) should be supported.

* Mac OS X build is provided courtesy of [JrMasterModelBuilder](http://jrmastermodelbuilder.netai.net/). Minimum supported version is Mac OS X 10.6 Snow Leopard.

* **Cycles Render Time Calculator** has been sucessfully tested on Ubuntu 12.04.1 x86 running Python 3.2. It may run on other Unix distos, but has not been 
tested.

If you get the following error while running **Cycles Render Time Calculator**, on Linux:

```
/usr/local/bin/python3: bad interpreter: No such file or directory
```

Check if your Python 3 installation is located there or not. If it is not, look for it under

```
/usr/bin/python3
```

If it is located there, you'll need edit the script to use the new location.


Credit
------

***Cycles Render Time Calculator* and all components are copyright 2013 le717 and rioforce, and released under the [GNU General Public License Version 3](
http://www.gnu.org/licenses/gpl.html). Special thanks to JrMasterModelBuilder for Mac OS X build.**