$(function () {
  $("#datepicker").datepicker({
    showOn: "button",
    buttonImage: "./images/calendar.svg",
    buttonImageOnly: true,
    buttonText: "icono",
    showOn: "both",
  });
  $(".datepicker").datepicker({
    showOn: "button",
    buttonImage: "./images/calendar.svg",
    buttonImageOnly: true,
    buttonText: "icono",
    showOn: "both",
    startDate: "-4m",
    endDate: "+0d",
  });
  $(".attendance-datepicker").datepicker({
    showOn: "button",
    buttonImage: "./images/calendar.svg",
    buttonImageOnly: true,
    buttonText: "icono",
    showOn: "both",
    startDate: "-4m",
    endDate: "+0d"
  })
  .on("changeDate", e => {
    // Handle displayed date
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const url = new URL(window.location.href);
    url.searchParams.set("date", e.date.toLocaleDateString('en-UK').replace("/", "-").replace("/", "-"));
    window.location.href = url.href;
  });
});

// $(document).ready(function() {
//   // Initialize datepicker
//   var currentDate = new Date();
//   $('.datepicker-input-date').datepicker();

//   // Add event listener to icon
//   $('.datepicker-icon-date').click(function() {
//     $('.datepicker-input-date').datepicker('show');
//   });
// });

function removeClass(element) {
  element.classList.remove("placeholderclass");
}
