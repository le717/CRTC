/*
    Cycles Render Time Calculator (CRTC)
    Calculate how long your Blender Cycles Engine renders will take.

    Created 2013 Triangle717 & rioforce
    <http://Triangle717.WordPress.com/>
    <http://rioforce.wordpress.com/>

-------------------------------------
Cycles Render Time Calculator - Web Version
*/

// Store site (app) info in an array
var appValues = ["Cycles Render Time Calculator - Web Version",
"0.3", "", "Triangle717 and rioforce"];


function changeFields(rendertype) {
    /* Change field lables depending on values chosen */

    // User is rendering using tiles
    if (rendertype === "tiles") {
        document.getElementById("numof1").innerHTML="Number of Tiles: ";
        document.getElementById("numof2").innerHTML="Render time of one Tile (in seconds) ";
        }

    // User is rendering using Progressive Refine
    else {
        document.getElementById("numof1").innerHTML="Number of Samples: ";
        document.getElementById("numof2").innerHTML="Render time of one Sample (in seconds) ";
        }
};


function isVideo() {
    /* Change field lables depending on if video is being rendered */

    // Get state of check box
    var value = document.getElementById("videocheck").checked

    // Display the field for number of frames
    if (value) {
        document.getElementById("numofframes").innerHTML='<li>Number of frames in animation: <input type="text" name="uname" placeholder="250" autocomplete="off"> </li>';
        }

    // It is unchecked, display nothing
    else {
        document.getElementById("numofframes").innerHTML="";
        }
};


function videoRender() {
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


function tileRender() {
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


function tileVideoRender(paramseconds) {
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


function doMath(number1, number2) {
    /* Perform the math problems */

    //console.log(number1);
    //console.log(number2);

    // Holds our math results
    values = [];

    // Convert input to integers using Base10
    number1 = parseInt(number1, 10);
    number2 = parseInt(number2, 10);

    // Calculate the seconds, minutes, and hours
    var seconds = number1 * number2;
    var minutes = seconds / 60;
    var hours = seconds / 3600;

    // Round the calculations off
    seconds = Math.round(seconds);
    minutes = Math.round(minutes);
    hours = Math.round(hours);

    // Add the results to the the array and return it
    values.push(seconds);
    values.push(minutes);
    values.push(hours);
    return values;
};

function calculate() {
    /*  Calculate the render times! */

    // Get the numbers from the fields
    // TODO: Add check to make sure they are numbers
    var first_number = document.getElementById("numof1");
    var second_number = document.getElementById("numof2");
    //var isvideo = document.getElementById("videocheck").checked;
    console.log(first_number);
    console.log(second_number);

    // Do the math
    var results = doMath(first_number, second_number);

    // It will take over an hour
    if (results[0] >= 3600.0) {
        document.getElementById("results").innerHTML="<strong>" + results[2] + " hours</strong>";
        console.log("It will take approximately " + results[2] +  "hours to render your animation.");
        }

    // It will take over a minute but less than an hour
    else if (results[0] >= 60.0 && results[0] < 3599.9) {
        document.getElementById("results").innerHTML="<strong>" + results[1] + " minutes</strong>";
        console.log("It will take approximately " + results[1] + " minutes to render your animation.");
        }

    // It will take only seconds
    else {
        document.getElementById("results").innerHTML="<strong>" + results[0] + " seconds</strong>";
        console.log("It will take approximately " + results[0] + " seconds to render your animation.");
        }

    // Do something else here!
    //document.getElementById("results").innerHTML="<strong>10 hours</strong>";

};
