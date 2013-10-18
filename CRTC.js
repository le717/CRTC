/*
    Cycles Render Time Calculator
    Calculate how long your Blender Cycles Engine renders will take.

    Created 2013 Triangle717 & rioforce
    <http://Triangle717.WordPress.com/>
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

-------------------------------------
Cycles Render Time Calculator - Web Version
*/

var app = "Cycles Render Time Calculator"
var majver = "Version 1.2.3"
var minver = "Unstable"
var creator = "Triangle717 and rioforce"

// CRTC icon
var app_icon = "Icon.ico"

// Generic Animation Render Time
var videoRender = function() {
    var videoframes = prompt("\nHow many frames are in your animation? ");
    var videoframetime = prompt("How long does a single frame take to render (in seconds)? ");

    // Convert input to integers using Base10 (duh)
    videoframes = parseInt(videoframes, 10);
    videoframetime = parseInt(videoframetime, 10);

    // Calculate the seconds, minutes, and hours
    var videoseconds = videoframes * videoframetime;
    var videominutes = videoseconds / 60;
    var videohours = videoseconds / 3600;

    // It will take over an hour to render
    if (videoseconds >= 3600.0) {
            console.log("\nIt will take approximately " + videohours + " hours to render your animation.\n");
        }
    // It will take over a minute but less than an hour to render
    else if (videoseconds >= 60.0 && videoseconds < 3599.9) {
            console.log("\nIt will take approximately " + videominutes  + " minutes to render your animation.\n");
        }
        // It will take only seconds to render
    else {
        console.log("\nIt will take approximately " + videoseconds + " seconds to render your animation.\n");
        }
};
