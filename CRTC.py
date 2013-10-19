#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
    Cycles Render Time Calculator (CRTC)
    Calculate how long your Blender Cycles Engine renders will take.

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
Cycles Render Time Calculator V1.2.2 Stable
"""

import os
import time

app = "Cycles Render Time Calculator"
majver = "Version 1.2.3"
minver = "Unstable"
creator = "Triangle717 and rioforce"

# CRTC icon
app_icon = "Icon.ico"


def main():
    """Menu Layout"""
    print("\n{0}\nCreated 2013 {1}".format(app, creator))
    print('''\nPlease make a selection:\n
[a] Animation Render
[t] Render Using Tiles
[p] Render Using Progressive Refine
[q] Quit''')
    menuopt = input("\n> ")
    while True:
        if menuopt.lower() == "t":
            tilerender()
        elif menuopt.lower() == "a":
            videorender()
        elif menuopt.lower() == "p":
            layerrender()
        elif menuopt.lower() == "q":
            raise SystemExit(0)
        # Undefined input
        else:
            main()


def videorender():
    """Generic Animation Render Time"""
    try:
        videoframes = int(input("\nHow many frames are in your animation? "))
        videoframetime = float(input("How long does a single frame take to render (in seconds)? "))
        # Calculate the seconds, minutes, and hours
        videoseconds = videoframes * videoframetime
        videominutes = videoseconds / 60
        videohours = videoseconds / 3600

        # It will take over an hour to render
        if videoseconds >= 3600.0:
            print('''
It will take approximately {0} hours to render your animation.
'''.format(round(videohours, 2)))
            time.sleep(0.5)
            main()

        # It will take over a minute but less than an hour to render
        elif videoseconds >= 60.0 and videoseconds < 3599.9:
            print('''
It will take approximately {0} minutes to render your animation.
'''.format(round(videominutes, 2)))
            time.sleep(0.5)
            main()

        # It will take only seconds to render
        else:
            print('''
It will take approximately {0} seconds to render your animation.
'''.format(round(videoseconds, 2)))
            time.sleep(0.5)
            main()

    except ValueError:
        print("That is an invalid input. Please try again.")
        videorender()


def tilerender():
    """Calculates Render Time (Using Tiles)"""
    try:
        numtiles = int(input("\nHow many tiles are in your render? "))
        tilerendertime = float(input("How long does a single tile take to render (in seconds)? "))

        # Mathamatical functions
        tileseconds = numtiles * tilerendertime
        tileminutes = tileseconds / 60
        tilehours = tileseconds / 3600

        # It will take over an hour
        if tileseconds >= 3600.0:
            print('''
It will take approximately {0} hours to render your image.
'''.format(round(tilehours, 2)))

        # It will take over a minute but less than an hour
        elif tileseconds >= 60.0 and tileseconds < 3599.9:
            print('''
It will take approximately {0} minutes to render your image.
'''.format(round(tileminutes, 2)))

        # It will take only seconds
        else:
            print('''
It will take approximately {0} seconds to render your image.
'''.format(round(tileseconds, 2)))

    # Catch any non-numerical input
    except ValueError:
        print("That is an invalid input. Please try again.")
        tilerender()

    # AKA video or "multi-frame" animation
    print("Are you rendering an animation? " + r"(y\N)")
    tilevideo = input("\n\n> ")
    # No, I am not rendering an animation
    if tilevideo.lower() != "y":
        main()
    else:
        # Yes, I am
        tilevideorender(tileseconds)


def tilevideorender(tileseconds):
    """Calculates Animation Render Time (Using Tiles)"""
    try:
        tileframenumber = int(input("\nHow many frames are in your animation? "))

        # More mathamatical functions
        tilevideoseconds = tileseconds * tileframenumber
        tilevideominutes = tilevideoseconds / 60
        tilevideohours = tilevideoseconds / 3600

        # It will take over an hour
        if tilevideoseconds >= 3600.0:
            print('''
It will take approximately {0} hours to render your animation.
'''.format(round(tilevideohours, 2)))

        # It will take over a minute but less than an hour
        elif tilevideoseconds >= 60.0 and tilevideoseconds < 3599.9:
            print('''
It will take approximately {0} minutes to render your animation.
'''.format(round(tilevideominutes, 2)))

        else:
            print('''
It will take approximately {0} seconds to render your animation.
'''.format(round(tilevideoseconds, 2)))
        time.sleep(0.5)
        main()

    # Catch any non-numerical input
    except ValueError:
        print("That is an invalid input. Please try again.")
        tilevideorender(tileseconds)


def layerrender():
    """
    Calculates Image Render Time (Using Progessive Refine)
    Progressive Refine Image and Animation render is just the Tile render code adapted to
    support the Progressive Refine method. Therefore, I've omitted the comments.
    """
    try:
        layernum = int(input("\nHow many samples are in your render? "))
        layerrendertime = float(input("How long does a single sample take to render (in seconds)? "))

        # Even more Mathamatical functions
        layerseconds = layernum * layerrendertime
        layerminutes = layerseconds / 60
        layerhours = layerseconds / 3600

        if layerseconds >= 3600.0:
            print('''
It will take approximately {0} hours to render your image.
'''.format(round(layerhours, 2)))

        elif layerseconds >= 60.0 and layerseconds < 3599.9:
            print('''
It will take approximately {0} minutes to render your image.
'''.format(round(layerminutes, 2)))

        else:
            print('''
It will take approximately {0} seconds to render your image.
'''.format(round(layerseconds, 2)))

    except ValueError:
        print("That is an invalid input. Please try again.")
        layerrender()

    print("Are you rendering an animation? " + r"(y\N)")
    layervideo = get_input("\n\n> ")
    if layervideo.lower() != "y":
        main()
    else:
        layervideorender(layerseconds)


def layervideorender(layerseconds):
    """Calculates Animation Render Time (Using Progessive Refine)"""
    try:
        layerframenumber = int(input("\nHow many frames are in your animation? "))
        # Math is FUN!
        layervideoseconds = layerseconds * layerframenumber
        layervideominutes = layervideoseconds / 60
        layervideohours = layervideoseconds / 3600

        if layervideoseconds >= 3600.0:
            print('''
It will take approximately {0} hours to render your animation.
'''.format(round(layervideohours, 2)))
        elif layervideoseconds >= 60.0 and layervideoseconds < 3599.9:
            print('''
It will take approximately {0} minutes to render your animation.
'''.format(round(layervideominutes, 2)))
        else:
            print('''
It will take approximately {0} seconds to render your animation.
'''.format(round(layervideoseconds, 2)))
        time.sleep(0.5)
        main()

    except ValueError:
        print("That is an invalid input. Please try again.")
        layervideorender(layerseconds)


if __name__ == "__main__":
    os.system("title {0} {1}".format(app, majver))
    main()