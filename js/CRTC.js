/*
    Cycles Render Time Calculator (CRTC)
    Calculate how long your Blender Cycles Engine renders will take.

    Created 2013 Triangle717 & rioforce
    <http://Triangle717.WordPress.com/>
    <http://rioforce.wordpress.com/>

-------------------------------------
Cycles Render Time Calculator - Web Version
*/


function changeFields() {
    /* Change field lables depending on values chosen */

    // Get state of Progressive Refine radio button
    var rendertype = document.getElementById("render").checked

    // User is rendering using Tiles
    if (!rendertype) {
        document.getElementById("numof1label").innerHTML="Number of Tiles: ";
        document.getElementById("numof2label").innerHTML="Render time of one Tile (in seconds) ";
        }

    // User is rendering using Progressive Refine
    else {
        document.getElementById("numof1label").innerHTML="Number of Samples: ";
        document.getElementById("numof2label").innerHTML="Render time of one Sample (in seconds) ";
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
    var first_number = document.getElementById("field1").value;
    var second_number = document.getElementById("field2").value;
    //var isvideo = document.getElementById("videocheck").checked;

    // Do the math
    var results = doMath(first_number, second_number);

    // Standard messages that may be edited later
    var hr_text = " hours"
    var min_text = " minutes"
    var sec_text = " seconds"

    // It will take over an hour
    if (results[0] >= 3600.0) {

        // If it is exactly one hour, change the message to remove the 's'
        if (results[0] === 3600) {
            hr_text = " hour";
        }
        document.getElementById("results").innerHTML="<strong>" + results[2] + hr_text + "</strong>";
        }

    // It will take over a minute but less than an hour
    else if (results[0] >= 60 && results[0] < 3599.9) {

        // If it is exactly one minute, change the message to remove the 's'
        if (results[0] === 60) {
            min_text = " minute";
        }
        document.getElementById("results").innerHTML="<strong>" + results[1] + min_text + "</strong>";
        }

    // It will take only seconds
    else {

        // If it is exactly one second, change the message to remove the 's'
        if (results[0] === 1) {
            sec_text = " second";
        }
        document.getElementById("results").innerHTML="<strong>" + results[0] + sec_text + "</strong>";
        }

    // Do something else here!
    //document.getElementById("results").innerHTML="<strong>10 hours</strong>";

};
