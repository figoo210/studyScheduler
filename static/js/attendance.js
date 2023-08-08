var objToday = new Date()
// weekday = new Array('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'),
// dayOfWeek = weekday[objToday.getDay()],

// Handle displayed date
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);

if (!queryString || queryString == "" || !urlParams.has("date")) {
  const url = new URL(window.location.href);
  url.searchParams.set("date", objToday.toLocaleDateString('en-UK').replace("/", "-").replace("/", "-"));
  window.location.href = url.href;
}

let domEnder = (function () {
    var a = objToday;
    if (/1/.test(parseInt((a + "").charAt(0)))) return "";
    a = parseInt((a + "").charAt(1));
    return 1 == a ? " " : 2 == a ? "" : 3 == a ? "" : "";
  })(),
  dateList = urlParams.has("date")
    ? urlParams.get("date").split("-")
    : objToday.toLocaleDateString('en-UK').replace("/", "-").replace("/", "-").split("-"),
  dayOfMonth = dateList[0],
  months = new Array(
    "يناير",
    "فبراير",
    "مارس",
    "ابريل",
    "مايو",
    "يونيو",
    "يوليو",
    "اغسطس",
    "سبتمبر",
    "اكتوبر",
    "نوفمبر",
    "ديسمبر"
  ),
  curMonth = months[parseInt(dateList[1]) - 1],
  curYear = dateList[2],
  curHour =
    objToday.getHours() > 12
      ? objToday.getHours() - 12
      : objToday.getHours() < 10
      ? "0" + objToday.getHours()
      : objToday.getHours(),
  curMinute =
    objToday.getMinutes() < 10
      ? "0" + objToday.getMinutes()
      : objToday.getMinutes(),
  curSeconds =
    objToday.getSeconds() < 10
      ? "0" + objToday.getSeconds()
      : objToday.getSeconds(),
  curMeridiem = objToday.getHours() > 12 ? "PM" : "AM";
//  dayOfMonth + " " + curMonth + " " + curYear;
var today = `<div class=" d-flex justify-content-start align-items-center">
 <span class="fw-bolder fs-1 style-day-month">${dayOfMonth}</span >
 <div class="d-flex flex-column justify-content-center align-items-center">
 <span class="style-month">${curMonth}</span>
 <span class="style-year">${curYear}</span>
 </div> </div>`;

// document.getElementsByClassName("mb-5 py-3")[0].innerHTML = today;
document.getElementById("dayOfMonth").innerHTML = dayOfMonth;
document.getElementById("curMonth").innerHTML = curMonth;
document.getElementById("curYear").innerHTML = curYear;


