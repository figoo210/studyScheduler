$(function () {
  $("#datepicker").datepicker({
    showOn: "both",
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


