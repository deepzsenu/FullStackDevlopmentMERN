// Get the HTML elements for the clock components
const HourElement = document.getElementById("hours");
const minElement = document.getElementById("mins");
const secsElement = document.getElementById("secs");
const ampmElement = document.getElementById("am-pm");

// Function to update the clock
function updateClock() {
  // Get the current hours, minutes, and seconds using the Date object
  let hours = new Date().getHours();
  let mins = new Date().getMinutes();
  let secs = new Date().getSeconds();
  let ampm = "AM";

  // Check if the current hour is greater than 12 to determine AM/PM
  if (hours > 12) {
    // Convert hours to 12-hour format
    hours = hours - 12;
    ampm = "PM";
  }

  hours =  hour <10 ? "0" + hours : hours;
  mins = mins <10 ? "0" + mins : mins;
  secs = secs <10 ? "0" + secs : secs;

  // Update the clock HTML elements with the current time values
  HourElement.innerHTML = hours;
  minElement.innerHTML = mins;
  secsElement.innerHTML = secs;
  ampmElement.innerHTML = ampm;

  // Call the updateClock function again after 1 millisecond using setTimeout
  setTimeout(updateClock, 1);
}

// Initial call to updateClock to start updating the clock
updateClock();
