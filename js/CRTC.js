/*
    Cycles Render Time Calculator (CRTC)
    Calculate how long your Blender Cycles Engine renders will take.

    Created 2013 Triangle717 & rioforce
    <http://Triangle717.WordPress.com/>
    <http://rioforce.wordpress.com/>

    Licensed under The MIT License
    <http://opensource.org/licenses/MIT>

-------------------------------------
Cycles Render Time Calculator - Web Version
*/


function changeFields() {
    /* Change field lables depending on values chosen */

    // Get state of Progressive Refine radio button
    var rendertype = document.getElementById("prradio").checked

    // User is rendering using Tiles
    if (!rendertype) {
        document.getElementById("numof1label").innerHTML="Number of Tiles: ";
        document.getElementById("numof2label").innerHTML="Render time of one Tile (in seconds): ";
        }

    // User is rendering using Progressive Refine
    else {
        document.getElementById("numof1label").innerHTML="Number of Samples: ";
        document.getElementById("numof2label").innerHTML="Render time of one Sample (in seconds): ";
        }
};


function isVideo() {
    /* Change field lables depending on if video is being rendered */

    // Get state of check box
    var value = document.getElementById("videocheck").checked

    // Display the field for number of frames
    if (value) {
        document.getElementById("numofframes").innerHTML='<label id="numofframeslabel" for="numofframes">Number of frames in animation: </label><li>\n<input id="field3" type="text" placeholder="250" autocomplete="off"></li>';
        }

    // It is unchecked, display nothing
    else {
        document.getElementById("numofframes").innerHTML="";
        }
};


function doMath(number1, number2) {
    /* Perform the math problems */

    // Holds our math results
    values = [];

    // Reset error message display
    document.getElementById("errmessage").innerHTML="";

    // Convert input to integers using Base10
    number1 = parseInt(number1, 10);
    number2 = parseInt(number2, 10);

    // A valid number was not entered
    if (isNaN(number1) || isNaN(number2) || number1 === 0 || number2 === 0)  {

        // Display error message stating only munbers are allowed
        document.getElementById("errmessage").innerHTML="Only numeric values are allowed!";
    }

    // Set number(s) to 0 to stop display of NaN seconds
    if (isNaN(number1)) {
        number1 = 0; }

     if (isNaN(number2)) {
        number2 = 0; }

    // Calculate the seconds, minutes, and hours
    var seconds = number1 * number2;
    var minutes = seconds / 60;
    var hours = seconds / 3600;

    // Round the calculations off to round to two decimal places
    seconds = seconds.toFixed(2);
    minutes = minutes.toFixed(2);
    hours = hours.toFixed(2);

    // Add the results to the the array and return it
    values.push(seconds);
    values.push(minutes);
    values.push(hours);
    return values;
};

// Declare global variable
var thisIsVideo;


function calculate() {
    /*  Calculate the render times! */

    // Get the numbers from the fields
    var first_number = document.getElementById("field1").value;
    var second_number = document.getElementById("field2").value;

    // Do the still image math
    var picture_results = doMath(first_number, second_number);

    // Check if a video is being rendered
    thisIsVideo = document.getElementById("videocheck").checked;

    // If so, get the value entered
    if (thisIsVideo) {
        var number_of_frames = document.getElementById("field3").value;

        // Do the video math
        var video_results = doMath(picture_results[0], number_of_frames);

        // Display the video results
        displayResults(video_results);
        }

    // Display the still image results
    else {
        displayResults(picture_results);
        }
};


function displayResults(results) {

    // Standard messages that may be edited later
    var hr_text = " hours"
    var min_text = " minutes"
    var sec_text = " seconds"

    // It will take over an hour
    if (results[0] >= 3600.0) {

        // If it is exactly one hour, change the message to remove the 's'
        if (results[0] === 3600) {
            hr_text = hr_text.slice(0, -1);
            }
        document.getElementById("results").innerHTML = results[2] + hr_text;
    }

    // It will take over a minute but less than an hour
    else if (results[0] >= 60 && results[0] < 3599.9) {

        // If it is exactly one minute, change the message to remove the 's'
        if (results[0] === 60) {
            min_text = min_text.slice(0, -1);
            }
        document.getElementById("results").innerHTML = results[1] + min_text;
    }

    // It will take only seconds
    else {

        // If it is exactly one second, change the message to remove the 's'
        if (results[0] === 1) {
            sec_text = sec_text.slice(0, -1);
            }
        document.getElementById("results").innerHTML = results[0] + sec_text;
    }
};
