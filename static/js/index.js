$(document).ready(function () {
  var multipleCancelButton = new Choices("#choices-multiple-remove-button", {
    removeItemButton: true,
    maxItemCount: 4,
  });

  $("#departmentForm").submit((e) => {
    // e.preventDefault();
    $("#departmentFormDivisions").val($("#departmentForm select").val());
  });
});

// Sidebar Active status
let navCont = document.getElementById("navbarTogglerDemo01");
let alinks = navCont.querySelectorAll("a");
alinks.forEach((eachA) => {
  if (eachA.href == window.location.href) {
    for (let i = 0; i < alinks.length; i++) {
      alinks[i].classList.remove("active");
    }
    eachA.classList.add("active");
  }
});
