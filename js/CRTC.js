/*
    Cycles Render Time Calculator (CRTC)
    Calculate how long your Blender Cycles Engine renders will take.

    Created 2013 Triangle717 & rioforce
    <http://Triangle717.WordPress.com/>
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
Cycles Render Time Calculator - Web Version
*/

var app = "Cycles Render Time Calculator"
var majver = "Version 1.2.3"
var minver = "Unstable"
var creator = "Triangle717 and rioforce"

// CRTC icon
var app_icon = "Icon.ico"

var videoRender = function() {
    /* Generic Animation Render Time */

    var videoframes = prompt("\nHow many frames are in your animation? ");
    var videoframetime = prompt("How long does a single frame take to render (in seconds)? ");

    // Convert input to integers using Base10 (duh)
    videoframes = parseInt(videoframes, 10);
    videoframetime = parseInt(videoframetime, 10);

    // Calculate the seconds, minutes, and hours
    var seconds = videoframes * videoframetime;
    var minutes = seconds / 60;
    var hours = seconds / 3600;

    // It will take over an hour to render
    if (seconds >= 3600.0) {
        console.log("\nIt will take approximately " + Math.round(hours) + " hours to render your animation.\n");
        }

    // It will take over a minute but less than an hour to render
    else if (seconds >= 60.0 && seconds < 3599.9) {
        console.log("\nIt will take approximately " + Math.round(minutes)  + " minutes to render your animation.\n");
        }

    // It will take only seconds to render
    else {
        console.log("\nIt will take approximately " + Math.round(seconds) + " seconds to render your animation.\n");
        }
};

var tileRender = function() {
    /* Calculates Render Time (Using Tiles) */

    var numtiles = prompt("\nHow many tiles are in your render? ");
    var tilerendertime = prompt("How long does a single tile take to render (in seconds)? ");

    // Convert input to integers using Base10
    numtiles = parseInt(numtiles, 10);
    tilerendertime = parseInt(tilerendertime, 10);

    // Calculate the seconds, minutes, and hours
    var seconds = numtiles * tilerendertime;
    var minutes = seconds / 60;
    var hours = seconds / 3600;

    // It will take over an hour
    if (seconds >= 3600.0) {
        console.log("\nIt will take approximately " + Math.round(hours) + " hours to render your animation.\n");
        }

    // It will take over a minute but less than an hour
    else if (seconds >= 60.0 && seconds < 3599.9) {
        console.log("\nIt will take approximately " + Math.round(minutes)  + " minutes to render your animation.\n");
    }

    // It will take only seconds
    else {
        console.log("\nIt will take approximately " + Math.round(seconds) + " seconds to render your animation.\n");
        }

    // AKA video or "multi-frame" animation
    var tilevideo = confirm("Are you rendering an animation?");

    // Yes, I am rendering an animation
    if (tilevideo) {
        tileVideoRender(seconds);
        }
};

var tileVideoRender = function(paramseconds) {
    /* Calculates Animation Render Time (Using Tiles) */

    tileframenumber = prompt("\nHow many frames are in your animation? ");

    // Convert input to integers using Base10
    tileframenumber = parseInt(tileframenumber, 10);

    // More mathamatical functions
    seconds = paramseconds * tileframenumber;
    minutes = seconds / 60;
    hours = seconds / 3600;

    // It will take over an hour
    if (seconds >= 3600.0) {
        console.log("It will take approximately " + Math.round(hours) +  "hours to render your animation.");
        }

    // It will take over a minute but less than an hour
    else if (seconds >= 60.0 && seconds < 3599.9) {
        console.log("It will take approximately " + Math.round(minutes) + " minutes to render your animation.");
        }

    // It will take only seconds
    else {
        console.log("It will take approximately " + Math.round(seconds) + " seconds to render your animation.");
        }
};