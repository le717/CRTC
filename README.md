Cycles Render Time Calculator
=============================

This is the readme to **Cycles Render Time Calculator** (**CRTC**), a [Python  application](http://www.python.org)
and [HTML/JavaScript website experiment](http://le717.github.io/CRTC) written by
[Triangle717](http://Triangle717.WordPress.com) and [rioforce](http://rioforce.WordPress.com)
to calculate approximate GPU render times when using the [Blender Cycles Engine](http://www.blender.org).

Why Was This Created
--------------------

It is said that "Necessity is the mother of invention". That can be said of this small tool.
Rioforce and I were always spending lots of time trying to figure out when his render would be completed,
and we were tired of it. We finally determined I should write a program to do this for us.
Thus **CRTC** was born.

In the third week of October 2013, I began rewriting **CRTC** in HTML/JavaScript form
as an experiment and learning project on how to create websites.

_Coming Soon._

How It Works
------------

**Cycles Render Time Calculator** supports Tiles and Progressive Refine render methods
for both still images and animations, as well as a General Animation render (render engine neutral).
Blender Internal is not supported, and if it were, this project would not be named the way it is. :stuck_out_tongue:

**NOTE:** _Approximate_ is the keyword here. While the render times are accurate if all system variables remain constant,
that is an impossible feat to achieve. Thus, the final render times will be different than the stated time.
For example, once it calculated a 6.5 minute render timr and it  only took 5 minutes.

### Python ###

For Tiles render, simply enter the number of tiles it takes to render your image,
and how many seconds or milliseconds it takes to render a single tile.
This information can easily be found in the Render Window. **CRTC** will then calculate an approximate render time.
If you are rendering an animation (AKA video or "multi-frame" animation), press `y` when prompted,
enter the number of frames your video has, and an approximate animation render time will be calculated.

Progressive Refine render works the same way, differing only by asking for the number of Samples in your render,
and how many seconds/milliseconds it takes to to render one Sample.

General Animation render asks only two questions: the number of frames and the time it takes for a single frame to render.

In all modes, render time will be displayed in either seconds, minutes, or hours,
depending on the input and result of the calculations.

### Website ###

The website experiment works the exact same way as the original Python version, except it lacks the General Animation mode
and does not have a CLI interface. Special care has been taken to ensure cross-browser combatibility,
but some elements may be incorrectly rendered in some browsers, notability mobile ones.

**Internet Explorer users: you will need to allow use of an "ActiveX" object (actually JavaScript for __CRTC__ to work.**

_Coming Soon._


Releases
--------

All downloads are available on the [Releases page](https://github.com/le717/CRTC/releases).

* Version 1.2.2 - May 21, 2013

> [Source Code](https://github.com/le717/Cycles-Render-Time-Calculator/tree/1.2.2)

> [Direct Download](https://github.com/le717/Cycles-Render-Time-Calculator/archive/1.2.2.zip)

* Version 1.1/1.2 Stable - February 26, 2013

> [Source Code](https://github.com/le717/Cycles-Render-Time-Calculator/tree/V1.1Stable) [**](#builds)

> [Direct Download](https://github.com/le717/Cycles-Render-Time-Calculator/archive/V1.1Stable.zip)

* Version 1.0 Beta 2 - February 16, 2013

> [Source Code](https://github.com/le717/Cycles-Render-Time-Calculator/tree/V1.0b2)

> [Direct Download](https://github.com/le717/Cycles-Render-Time-Calculator/archive/V1.0b2.zip)

Builds
------
* **Cycles Render Time Calculator** was originally written in Python 3.3, but in version 1.2, it was updated to run on both Python 2 and 3.
It was successfully tested on Python 3.3.0 and 2.7.4 with no errors. Further more, only the raw Python script of that was upgraded to 1.2.
The OS-specific builds are version 1.1, written with Python 3.3.0 only.

* Releases are compiled into Windows x86, x64 EXEs and Mac OS X application using [cx_freeze](http://cx-freeze.sourceforge.net).

* Windows build has been sucessfully tested on x64 Windows 7 and 8. However, Vista (and possibly XP) should be supported.

* Mac OS X build is provided courtesy of [@JrMasterModelBuilder](https://github.com/JrMasterModelBuilder). Minimum supported version is Mac OS X 10.7 Lion.

* **Cycles Render Time Calculator** has been successfully tested on Ubuntu 12.04.1 x86 running Python 3.2. It may run on other Unix distos, but has not been
tested.

License
-------

**Cycles Render Time Calculator** created 2013 Triangle717 and rioforce.
Original Python version licensed under the
[GNU General Public License Version 3](http://www.gnu.org/licenses/gpl.html).
HTML/JavaScript website experiment licensed under
[The MIT License](http://opensource.org/licenses/MIT).

**CRTC** makes use of the [**CSS Browser Selector**](https://github.com/verbatim/css_browser_selector) library,
originally created by [Rafael Lima] (http://rafael.adm.br) and licensed under the
[CC BY 2.5](http://creativecommons.org/licenses/by/2.5/).
