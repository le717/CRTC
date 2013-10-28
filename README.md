Cycles Render Time Calculator
=============================

This is the readme to **Cycles Render Time Calculator** (**CRTC**), a [Python  application](http://www.python.org)
and [HTML5/JavaScript website experiment](http://le717.github.io/CRTC) written by
[Triangle717](http://Triangle717.WordPress.com) and [rioforce](http://rioforce.WordPress.com)
to calculate approximate GPU render times when using the [Blender Cycles Engine](http://www.blender.org).

Why Was This Created
--------------------

It is said that "Necessity is the mother of invention". That can be said of this small tool.
Rioforce and I were always spending lots of time trying to figure out when his render would be completed,
and we were tired of it. We finally determined I should write a program to do this for us.
Thus **CRTC** was born.

On October 18, 2013, I began rewriting **CRTC** in HTML5/JavaScript form
as an experiment and learning project on how to create websites. It is hosted using [GitHub Pages](http://pages.github.com)
and can be accessed at [http://le717.github.io/CRTC](http://le717.github.io/CRTC).

How It Works
------------

**Cycles Render Time Calculator** supports Tiles and Progressive Refine render methods
for both still images and animations, as well as a General Animation render (render engine neutral).
Blender Internal is not supported, and if it were, this project would not be named the way it is. :stuck_out_tongue:

**NOTE:** _Approximate_ is the keyword here. While the render times are accurate if all system variables remain constant,
that is an impossible feat to achieve. Thus, the final render times will be different than the stated time.
For example, once it calculated a 6.5 minute render time and it  only took 5 minutes.

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
and does not have a CLI interface. Special care has been taken to ensure cross-browser compatibility,
but some elements may be incorrectly rendered in some browsers, notability mobile ones.

**Internet Explorer users: you will need to allow use of an erroneously labeled "ActiveX" object (actually JavaScript) for _CRTC_ to work.**

Releases
--------

All downloads of both the original Python version and HTML5/JavaScript website are available on the [Releases page](https://github.com/le717/CRTC/releases).
Mac OS X build is provided courtesy of [@JrMasterModelBuilder](https://github.com/JrMasterModelBuilder). Minimum supported version is Mac OS X 10.7 Lion.

License
-------

**Cycles Render Time Calculator** created 2013 Triangle717 and rioforce.
Original Python version licensed under the
[GNU General Public License Version 3](http://www.gnu.org/licenses/gpl.html).
HTML5/JavaScript website experiment licensed under
[The MIT License](http://opensource.org/licenses/MIT).

**CRTC** makes use of the [**CSS Browser Selector**](https://github.com/verbatim/css_browser_selector) library,
originally created by [Rafael Lima] (http://rafael.adm.br) and licensed under the
[CC BY 2.5](http://creativecommons.org/licenses/by/2.5/).
