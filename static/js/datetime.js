$(document).ready(function () {
  const minDate = new Date(1900, 0, 1);
  $(".input-daterange").datepicker({
    format: "dd-mm-yyyy",
    todayHighlight: true,
    minDate: minDate,
  });
});
