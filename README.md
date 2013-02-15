Render Calculator
=================

This is the readme to **Render Calculator**, a [Python 3](http://www.python.org) application written by [le717](http://triangle717.wordpress.com) and [rioforce](rioforce.wordpress.com) to calculate render times in [Blender] (http://www.blender.org) when using the Cycles Engine.

Why Was This Created
--------------------

It is said that "Necessity is the mother of invention". Well, that can be said of this tool. rioforce and I were always spending lots of time trying to figure out
when his render would be completed, and we were tired of it. We finally thought that a program should be written to do this for us. Then this program was born.
Using my knowledge of Python 3 and his Blender skills, we created this small program to calculate render times for both still images and videos.

How It Works
------------

Currently, it only supports the Cycles Engine and rendering with tiles. Support for Progressive Refinement and Blender Engine is planned if possible. 

You simply need to input the number of tiles it takes to render your image, and how long it takes to render a single tile. This info can easily be found
in the Render Window. **Render Calculator** will then calculate an approximate render time. If you are rendering an animation (AKA video or "multi-frame" animation), press 'y' when prompted, enter the number of frames your video has, and an approximate animation render time will be calculated.

*Approximate* is the keyword here. While the render times are accurate if all system variables are constant, that is impossible to achieve. Thus, the final render times will differ to the stated time. For myself, it calculated a 6.5 minute render time, and it really took 5 minutes. In short, your mileage will vary.

Releases
--------

* **Render Calculator** is written in Python 3, 3.3.0 to be exact. You will need to have a complete installation of Python `>=` 3.3 to run the Python script directly. Any version of Python `<=` is not supported, and a version check will prevent it from running on unsupported versions.

* Releases will be compiled into x86 and x64 Windows EXEs using [cx_freeze](http://cx-freeze.sourceforge.net). [py2exe](http://www.py2exe.org) does not support 
Python 3.3, so I cannot use it.

* Mac OS X, Unix, and similar systems should be supported, as I've written this with cross-platform support in mind. However, that has not yet been tested.

Credit
------

***Render Calculator* and all components are copyright 2013 le717 and rioforce, and released under the [GNU General Public License Version 3](http://www.gnu.org/licenses/gpl.html).**