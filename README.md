Cycles Render Time Calculator
=============================

This is the readme to **Cycles Render Time Calculator**, a [Python](http://www.python.org) application written by [Triangle717]
(http://triangle717.wordpress.com) and [rioforce](rioforce.wordpress.com) to calculate render times in [Blender] (http://www.blender.org) 
when using the Cycles Engine.

Why Was This Created
--------------------

It is said that "Necessity is the mother of invention". Well, that can be said of this tool. rioforce and I were always spending lots of time trying to figure 
out when his render would be completed, and we were tired of it. We finally thought that a program should be written to do this for us. Then this program was 
born. Using my knowledge of Python and his Blender skills, we created this small program to calculate render times for both still images and videos.

How It Works
------------

**Cycles Render Time Calculator** supports both the Tile and Progressive Refine render methods for both still images and animations, as well as a general 
animation render (render engine neutral). Blender Render is not supported, and if it were, it would not have Cycles in the name.

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

* Version 1.1/1.2 Stable - February 26, 2013

> [Source Code](https://github.com/le717/Cycles-Render-Time-Calculator/tree/V1.1Stable) [**](#builds)

> [Direct Download](https://github.com/le717/Cycles-Render-Time-Calculator/archive/V1.1Stable.zip)

* Version 1.0 Beta 2 - February 16, 2013

> [Source Code](https://github.com/le717/Cycles-Render-Time-Calculator/tree/V1.0b2)

> [Direct Download](https://github.com/le717/Cycles-Render-Time-Calculator/archive/V1.0b2.zip)

Builds
------
* While **Cycles Render Time Calculator** was originally written in Python 3.3, as of version 1.2, it runs on both Python 2 and 3. It has successfully be 
tested on Python 3.3.0 and 2.7.4 with no errors. No other versions have been tested. Further more, only `CRTC.py` has been upgraded to 
1.2. The OS-specific builds are version 1.1, written with Python 3.3.0.

* Releases are compiled into Windows x86, x64 EXEs and Mac OS X application using [cx_freeze](http://cx-freeze.sourceforge.net). 

* Windows build has been sucessfully tested on x64 Windows 7 and 8. However, Vista (and possibly XP) should be supported.

* Mac OS X build is provided courtesy of [JrMasterModelBuilder](http://jrmastermodelbuilder.netai.net/). Minimum supported version is Mac OS X 10.7 Lion.

* **Cycles Render Time Calculator** has been sucessfully tested on Ubuntu 12.04.1 x86 running Python 3.2. It may run on other Unix distos, but has not been 
tested.


Credit
------

***Cycles Render Time Calculator* and all components were created 2013 Triangle717 and rioforce, and released under the [GNU General Public License Version 3](
http://www.gnu.org/licenses/gpl.html). Special thanks to JrMasterModelBuilder for the Mac OS X build.**
