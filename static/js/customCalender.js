$( function() {
    $( "#datepicker" ).datepicker({
      showOn: "button",
      buttonImage: "./images/calendar.svg",
      buttonImageOnly: true,
      buttonText: "icono",
      showOn: "both"
    });
  } );

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
    element.classList.remove('placeholderclass');
  }