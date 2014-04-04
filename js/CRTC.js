/* global document, console */
/*
 * Cycles Render Time Calculator (CRTC)
 *
 * Created 2013-2014 Triangle717 & rioforce
 * <http://Triangle717.WordPress.com/>
 * <http://rioforce.wordpress.com/>
 *
 * Licensed under The MIT License
 * <http://opensource.org/licenses/MIT>
*/

/* ------------ Begin Variable Label Texts ------------ */


function changeFields() {
  "use strict";
  /* Change field lables depending on values chosen */

  var numOfLabel = document.querySelector("#numof-label"),
      timeLabel = document.querySelector("#time-label"),
      // Get state of Progressive Refine radio button
      rendertype = document.querySelector("#pro-radio").checked;

  // User is rendering using Tiles
  if (!rendertype) {
    numOfLabel.innerHTML = "Number of Tiles<br>";
    timeLabel.innerHTML = "Render time of one Tile (in seconds)<br>";
  } else {
    // User is rendering using Progressive Refine
    numOfLabel.innerHTML = "Number of Samples<br>";
    timeLabel.innerHTML = "Render time of one Sample (in seconds)<br>";
  }
}


function isVideo() {
  "use strict";
  /* Change field lables depending on if video is being rendered */

  var frameNum = document.querySelector("#frame-num"),
      frameNumLabel = document.querySelector("#frame-num-label"),
      // Get state of check box
      isVideoChecked = document.querySelector("#video-check").checked;

  // Display the field for number of frames
  if (isVideoChecked) {
    frameNum.style.display = "inline";
    frameNumLabel.style.display = "inline";
  } else {
    // It is unchecked, display nothing
    frameNum.style.display = "none";
    frameNumLabel.style.display = "none";
  }
}


function displayResults(results) {
  "use strict";
  /* Display calculation results */

  var finalResult,
      // Standard messages that may be edited later
      hrText = " hours",
      minText = " minutes",
      secondsText = " seconds",

      // Convert numbers back to floats (toFixed changed them to strings)
      floatSeconds = parseFloat(results[0], 2),
      floatMinutes = parseFloat(results[1], 2),
      floatHours = parseFloat(results[2], 2),
      resultsDisplay = document.querySelector("#results");

  // It will take over an hour
  if (floatSeconds >= 3600) {

    // If it is exactly one hour, change the message to remove the 's'
    if (floatHours === 1) {
      hrText = hrText.slice(0, -1);
    }

    // Kill trailing .00 if present
    if (results[2].slice(-2) === "00") {
      finalResult = floatHours;
    } else {
      finalResult = results[2];
    }

    // Construct final time + word display
    resultsDisplay.innerHTML = finalResult + hrText;

    // It will take over a minute but less than an hour
  } else if (floatSeconds >= 60 && floatSeconds < 3599) {

    // If it is exactly one minute, change the message to remove the 's'
    if (floatMinutes === 1) {
      minText = minText.slice(0, -1);
    }

    // Kill trailing .00 if present
    if (results[1].slice(-2) === "00") {
      finalResult = floatMinutes;
    } else {
      finalResult = results[1];
    }

    // Construct final time + word display
    resultsDisplay.innerHTML = finalResult + minText;

    // It will take only seconds
  } else if (floatSeconds <= 59.9) {

    // If it is exactly one second, change the message to remove the 's'
    if (floatSeconds === 1) {
      secondsText = secondsText.slice(0, -1);
    }

    // Kill trailing .00 if present
    if (results[0].slice(-2) === "00") {
      finalResult = floatSeconds;
    } else {
      finalResult = results[0];
    }

    // Construct final time + word display
    resultsDisplay.innerHTML = finalResult + secondsText;
  }
}


/* ------------ End Variable Label Texts ------------ */


/* ------------ Begin Mathematical Calculations ------------ */


function doMath(numberOne, numberTwo) {
  "use strict";
  /* Do the math */

  // Holds our math results
  var values = [],
      errorDisplay = document.querySelector("#error");

  // Reset error message display
  errorDisplay.style.opacity = "0";


  // Convert input to floats
  numberOne = parseFloat(numberOne, 2);
  numberTwo = parseFloat(numberTwo, 2);

  // Make sure an error if second field for video is invalid
  if (thisIsVideo && numberOne === 0) {
    numberOne =  NaN;
  }

  // A valid number was not entered
  if (isNaN(numberOne) || isNaN(numberTwo)) {

    // Display error message stating only numbers are allowed
    errorDisplay.style.opacity = "1";

    // Stop the calculations from running
    return false;
  }

  // Set number(s) to 0 to stop display of NaN seconds
  if (isNaN(numberOne)) {
    numberOne = 0;
  }
  if (isNaN(numberTwo)) {
    numberTwo = 0;
  }

  // Calculate the seconds, minutes, and hours
  var seconds = numberOne * numberTwo,
      minutes = seconds / 60,
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
  "use strict";
  /* Run process to calculate render time(s) */

  // Get the numbers from the fields
  var pictureResults,
      firstNumber = document.querySelector("#numof").value,
      secondNumber = document.querySelector("#time").value;

  // Do the still image math
  pictureResults = doMath(firstNumber, secondNumber);

  // Check if a video is being rendered
  thisIsVideo = document.querySelector("#video-check").checked;

  if (thisIsVideo) {
    // If so, get the value entered
    var numberOfFrames, videoResults;
    numberOfFrames = document.querySelector("#frame-num").value;

    // Do the video math
    videoResults = doMath(pictureResults[0], numberOfFrames);

    // Display the video results
    displayResults(videoResults);

  } else {
    // Display the still image results
    displayResults(pictureResults);
  }
}


/* ------------ End Mathematical Calculations ------------ */
