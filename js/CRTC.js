/*global document */
/*
    Cycles Render Time Calculator (CRTC)
    Calculate approximate GPU render times
    when using the Blender Cycles Engine

    Created 2013-2014 Triangle717 & rioforce
    <http://Triangle717.WordPress.com/>
    <http://rioforce.wordpress.com/>

    Licensed under The MIT License
    <http://opensource.org/licenses/MIT>

-------------------------------------
Cycles Render Time Calculator - Web Version
*/


/* ------------ Begin Variable Label Texts ------------ */


function changeFields() {
    /* Change field lables depending on values chosen */

    // Get state of Progressive Refine radio button
    var rendertype = document.querySelector("#pro-radio").checked;

    // User is rendering using Tiles
    if (!rendertype) {
        document.querySelector("#numof-label").innerHTML = "Number of Tiles:";
        document.querySelector("#time-label").innerHTML = "Render time of one Tile (in seconds):";
    } else {
        // User is rendering using Progressive Refine
        document.querySelector("#numof-label").innerHTML = "Number of Samples:";
        document.querySelector("#time-label").innerHTML = "Render time of one Sample (in seconds):";
    }
}


function isVideo() {
    /* Change field lables depending on if video is being rendered */

    // Get state of check box
    var value = document.querySelector("#video-check").checked;

    // Display the field for number of frames
    if (value) {
        document.querySelector("#frame-num-div").innerHTML = '<label for="frame-num">Number of frames in animation: </label><li>\n<input id="frame-num" type="text" placeholder="250" autocomplete="off"></li>';
    } else {
        // It is unchecked, display nothing
        document.querySelector("#frame-num-div").innerHTML = "";
    }
}


function displayResults(results) {
    /* Display calculation results */

    // Standard messages that may be edited later
    var hr_text, min_text, sec_text;
    hr_text = " hours";
    min_text = " minutes";
    sec_text = " seconds";

    // Convert numbers back to floats (toFixed changed them to strings)
    var flo_seconds, flo_minutes, flo_hours, final_result;
    flo_seconds = parseFloat(results[0], 2);
    flo_minutes = parseFloat(results[1], 2);
    flo_hours = parseFloat(results[2], 2);

    // It will take over an hour
    if (flo_seconds >= 3600) {

        // If it is exactly one hour, change the message to remove the 's'
        if (flo_hours === 1) {
            hr_text = hr_text.slice(0, -1);
        }

        // Kill trailing .00 if present
        if (results[2].slice(-2) === "00") {
            final_result = flo_hours;
        } else {
            final_result = results[2];
        }

        // Construct final time + word display
        document.querySelector("#results").innerHTML = final_result + hr_text;

    // It will take over a minute but less than an hour
    } else if (flo_seconds >= 60 && flo_seconds < 3599) {

        // If it is exactly one minute, change the message to remove the 's'
        if (flo_minutes === 1) {
            min_text = min_text.slice(0, -1);
        }

        // Kill trailing .00 if present
        if (results[1].slice(-2) === "00") {
            final_result = flo_minutes;
        } else {
            final_result = results[1];
        }

        // Construct final time + word display
        document.querySelector("#results").innerHTML = final_result + min_text;

    // It will take only seconds
    } else if (flo_seconds <= 59.9) {

        // If it is exactly one second, change the message to remove the 's'
        if (flo_seconds === 1) {
            sec_text = sec_text.slice(0, -1);
        }

        // Kill trailing .00 if present
        if (results[0].slice(-2) === "00") {
            final_result = flo_seconds;
        } else {
            final_result = results[0];
        }

        // Construct final time + word display
        document.querySelector("#results").innerHTML = final_result + sec_text;
    }
}


/* ------------ End Variable Label Texts ------------ */


/* ------------ Begin Mathematical Calculations ------------ */


function doMath(number1, number2) {
    /* Do the math */

    // Holds our math results
    var values = [];

    // Reset error message display
    document.querySelector("#error").innerHTML = "";

    // Convert input to floats
    number1 = parseFloat(number1, 2);
    number2 = parseFloat(number2, 2);

    // Make sure an error if second field for video is invalid
    if (thisIsVideo && number1 === 0) {
        number1 =  NaN;
    }

    // A valid number was not entered
    if (isNaN(number1) || isNaN(number2) || number1 === "" || number2 === "") {

        // Display error message stating only munbers are allowed
        document.querySelector("#error").innerHTML = "Only numeric values are allowed!";

        // Stop the calculations from running
        return false;
    }

    // Set number(s) to 0 to stop display of NaN seconds
    if (isNaN(number1)) {
        number1 = 0;
    }
    if (isNaN(number2)) {
        number2 = 0;
    }

    // Calculate the seconds, minutes, and hours
    var seconds, minutes, hours;
    seconds = number1 * number2;
    minutes = seconds / 60;
    hours = seconds / 3600;

    // Round the calculations off to round to two decimal places
    seconds = seconds.toFixed(2);
    minutes = minutes.toFixed(2);
    hours = hours.toFixed(2);

    // Add the results to the the array and return it
    values.push(seconds);
    values.push(minutes);
    values.push(hours);
    return values;
}

// Declare global variable
var thisIsVideo;


function calculate() {
    /* Run process to calculate render time(s) */

    // Get the numbers from the fields
    var first_number, second_number, picture_results;
    first_number = document.querySelector("#numof").value;
    second_number = document.querySelector("#time").value;

    // Do the still image math
    picture_results = doMath(first_number, second_number);

    // Check if a video is being rendered
    thisIsVideo = document.querySelector("#video-check").checked;

    // If so, get the value entered
    var number_of_frames, video_results;
    if (thisIsVideo) {
        number_of_frames = document.querySelector("#frame-num").value;

        // Do the video math
        video_results = doMath(picture_results[0], number_of_frames);

        // Display the video results
        displayResults(video_results);
    } else {
        // Display the still image results
        displayResults(picture_results);
    }
}


/* ------------ End Mathematical Calculations ------------ */
