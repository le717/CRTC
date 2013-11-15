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

------------------------------------
Cycles Render Time Calculator v1.3.0
"""

import os
import sys
import time

# Global variables, CRTC icon
app = "Cycles Render Time Calculator"
majver = "1.3"
minver = ".0"
creator = "Triangle717 and rioforce"
app_icon = "Icon.ico"

# Prohibit running on anything lower than 3.3.0
if sys.version_info < (3, 3, 0):
    print('''
You are running Python {0}.
You need to download Python 3.3.0 or newer to run
{1} {2}.
'''.format(sys.version[0:5], app, majver))
    raise SystemExit(0)


def main(num_of_loops=1):
    """Menu Layout"""
    num_of_loops += 1

    # If the user has pressed an valid key 5 times or this is app launch
    if (num_of_loops == 2 or num_of_loops == 6):
        # Reset the count back to two,
        if num_of_loops == 6:
            num_of_loops = 2

        print("\n{0}\nCreated 2013 {1}".format(app, creator))
        print('''
[a] Animation Render
[t] Render Using Tiles
[p] Render Using Progressive Refine
[q] Quit''')
    menuopt = input("\n> ")
    while True:
        if menuopt.lower() == "a":
            videoRender()
        elif menuopt.lower() == "t":
            tileRender()
        elif menuopt.lower() == "p":
            layerRender()
        elif menuopt.lower() == "q":
            raise SystemExit(0)
        # Undefined input
        else:
            print("\nThat is an invalid option!")
            main(num_of_loops=num_of_loops)

# ------------ Begin Value Input ------------ #


def videoRender():
    """Generic Animation Render Time"""
    try:
        # Number of frames and render time of one frame
        num_of_frames = int(input("\nNumber of frames in animation: "))
        frame_render_time = float(input(
            "Render time of one frame (in seconds): "))

        calculate(num_of_frames, frame_render_time, False)
        time.sleep(1)
        main()

    # Catch any non-numerical input
    except ValueError:
        print("That is an invalid input. Please try again.")
        videoRender()


def tileRender():
    """Calculate Image Render Time Using Tiles"""
    try:
        # Number of tiles and render time of one tile
        num_of_tiles = int(input("\nNumber of Tiles: "))
        tile_render_time = float(input(
            "Render time of one Tile (in seconds): "))

        # Ask if user is rendering a video ("multi-frame" animation)
        print("\nAre you rendering an animation?\n")
        tile_video = input(r"[Y\N] > ")

        # No, an animation is not being rendered
        if tile_video.lower() != "y":
            ani_render = False
        else:
            # Yes, an animation is being rendered
            ani_render = True

        # Calculate the time, pause for 1 second to better display result
        calculate(num_of_tiles, tile_render_time, ani_render)
        time.sleep(1)
        main()

    # Catch any non-numerical input
    except ValueError:
        print("That is an invalid input. Please try again.")
        tileRender()


def layerRender():
    """Calculate Image Render Time Using Progessive Refine"""
    try:
        num_of_layers = int(input("\nNumber of Samples: "))
        layer_render_time = float(input(
            "Render time of one Sample (in seconds): "))

         # Ask if user is rendering a video ("multi-frame" animation)
        print("\nAre you rendering an animation?\n")
        layer_video = input(r"[Y\N] > ")

        # No, an animation is not being rendered
        if layer_video.lower() != "y":
            ani_render = False
        else:
            # Yes, an animation is being rendered
            ani_render = True

        # Calculate the time, pause for 1 second to better display result
        calculate(num_of_layers, layer_render_time, ani_render)
        time.sleep(1)
        main()

    # Catch any non-numerical input
    except ValueError:
        print("That is an invalid input. Please try again.")
        layerRender()

# ------------ End Value Input ------------ #


# ------------ Begin Result Display ------------ #


def displayResults(results):
    """Display calculation results"""

    # Standard messages that may be edited later
    hr_text = "hours"
    min_text = "minutes"
    sec_text = "seconds"

    # Assign results to variables for easier access
    flo_seconds = results[0]
    flo_minutes = results[1]
    flo_hours = results[2]
    str_seconds = str(results[0])
    str_minutes = str(results[1])
    str_hours = str(results[2])

    # It will take over an hour
    if flo_seconds >= 3600.0:

        # If it is exactly one hour, change the message to remove the 's'
        if flo_hours == 1.0:
            hr_text = hr_text[:-1]

        # Kill trailing .0 if present
        if str_hours.endswith(".0"):
            final_result = str_hours[:-2]
        else:
            final_result = flo_hours

        # Construct final time + word display
        final_time = "{0} {1}".format(final_result, hr_text)

    # It will take over a minute but less than an hour
    elif (flo_seconds >= 60.0 and flo_seconds < 3599.9):

        # If it is exactly one minute, change the message to remove the 's'
        if flo_minutes == 1.0:
            min_text = min_text[:-1]

        # Kill trailing .0 if present
        if str_minutes.endswith(".0"):
            final_result = str_minutes[:-2]
        else:
            final_result = flo_minutes

        # Construct final time + word display
        final_time = "{0} {1}".format(final_result, min_text)

    # It will take only seconds
    elif flo_seconds <= 59.9:

        # If it is exactly one second, change the message to remove the 's'
        if flo_seconds == 1:
            sec_text = sec_text[:-1]

        # Kill trailing .0 if present
        if str_seconds.endswith(".0"):
            final_result = str_seconds[:-2]
        else:
            final_result = flo_seconds

        # Construct final time + word display
        final_time = "{0} {1}".format(final_result, sec_text)

    print('''

It will take approximately {0} to render your animation.
'''.format(final_time))

# ------------ End Result Display ------------ #


# ------------ Begin Mathematical Calculations ------------ #


def doMath(number1, number2):
    """Do the math"""

    # Holds our math results
    values = []

    # Calculate the seconds, minutes, and hours
    seconds = number1 * number2
    minutes = seconds / 60
    hours = seconds / 3600

    # Round the calculations off to round to two decimal places
    seconds = round(seconds, 2)
    minutes = round(minutes, 2)
    hours = round(hours, 2)

    # Add the results to the the array and return it
    values.append(seconds)
    values.append(minutes)
    values.append(hours)
    return values


def calculate(first_number, second_number, thisIsVideo):
    """Run process to calculate render time(s)"""

    # Do the still image math
    picture_results = doMath(first_number, second_number)

    # If an animation is being rendered, get the number of frames
    # A try... except block is not needed here
    # because the calling function handles it for us
    if thisIsVideo:
        number_of_frames = int(input("\nNumber of frames in animation: "))

        # Do the video math
        video_results = doMath(picture_results[0], number_of_frames)

        # Display the video results
        displayResults(video_results)

    # Display the still image results
    else:
        displayResults(picture_results)

# ------------ End Mathematical Calculations ------------ #


if __name__ == "__main__":
    os.system("title {0} v{1}{2}".format(app, majver, minver))
    main()
