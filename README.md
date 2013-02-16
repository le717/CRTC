Render Time Calculator
======================

This is the readme to **Render Time Calculator**, a [Python 3](http://www.python.org) application written by [le717](http://triangle717.wordpress.com) and [rioforce](rioforce.wordpress.com) to calculate render times in [Blender] (http://www.blender.org) when using the Cycles Engine.

Why Was This Created
--------------------

It is said that "Necessity is the mother of invention". Well, that can be said of this tool. rioforce and I were always spending lots of time trying to figure 
out when his render would be completed, and we were tired of it. We finally thought that a program should be written to do this for us. Then this program was 
born. Using my knowledge of Python and his Blender skills, we created this small program to calculate render times for both still images and videos.

How It Works
------------

Currently, it supports the Cycles Engine with Tiles and the Progressive Refine method. Blender Engine support is planned if possible. 

You simply need to input the number of tiles it takes to render your image, and how long it takes to render a single tile. This info can easily be found
in the Render Window. **Render Time Calculator** will then calculate an approximate render time. If you are rendering an animation (AKA video or "multi-frame" 
animation), press 'y' when prompted, enter the number of frames your video has, and an approximate animation render time will be calculated.

*Approximate* is the keyword here. While the render times are accurate if all system variables remain constant, that is an impossible feat to achieve. Thus, 
the final render times will be different than the stated time. For example, it calculated a 6.5 minute render time for me, and it really took 5 minutes.

Releases
--------

* While **Render Time Calculator** is written in Python 3.3, it runs perfectly on Python 3.2. You will need to have a complete installation of Python `>=` 3.2 to run the Python script directly. Any version of Python `<=` 3.1 is not supported, and a version check will prevent it from running on unsupported versions.

* Releases will be compiled into x86 and x64 Windows EXEs using [cx_freeze](http://cx-freeze.sourceforge.net). [py2exe](http://www.py2exe.org) does not support 
Python 3.3, so I cannot use it.

* **Render Time Calculator** has been tested on Ubuntu 12.04.1 x86, running Python 3.2, and it ran sucessfully. Therefore, it is possible it will run on other
Unix distos, but that has not been tested.

If you get the following error while running **Render Time Calculator** on Linux:

```
/usr/local/bin/python3: bad interpreter: No such file or directory
```

Check if your Python 3 installation is located there or not. If it is not, look for it under

```
/usr/bin/python3
```

If it is located there, you'll need edit the script to use the new location.

* Mac OS X support has not be tested, as the creator's do not have access to a computer running Mac OS X.

Credit
------

***Render Time Calculator* and all components are copyright 2013 le717 and rioforce, and released under the [GNU General Public License Version 3](
http://www.gnu.org/licenses/gpl.html).**