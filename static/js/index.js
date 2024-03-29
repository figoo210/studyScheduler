$(document).ready(function () {
  let choicesExist = document.getElementById("choices-multiple-remove-button");
  if (choicesExist) {
    var multipleCancelButton = new Choices("#choices-multiple-remove-button", {
      removeItemButton: true,
      maxItemCount: 4,
    });
  }

  $(".clockpicker").clockpicker();

  $("#departmentForm").submit((e) => {
    // e.preventDefault();
    $("#departmentFormDivisions").val($("#departmentForm select").val());
  });

});

  // Add id to clicked edit modal
function editThisByModal(modalData) {
  let modal = document.getElementById("editModal");
  let modalInput = modal.getElementsByTagName("input");
  let modalSelect = modal.getElementsByTagName("select");
  for (let i = 0; i < modalInput.length; i++) {
    const element = modalInput[i];
    if (element.type == "checkbox") {
      element.checked = modalData[element.name] == 1 ? true : false;
    } else {
      element.value = modalData[element.name];
    }
  }
  for (let i = 0; i < modalSelect.length; i++) {
    const element = modalSelect[i];
    for (let j = 0; j < element.getElementsByTagName("option").length; j++) {
      const e = element.getElementsByTagName("option")[j];
      if (e.value == modalData[element.name]){
        e.selected = true;
        break;
      }
    }
  }
}


// Update checkbox
function updateCheckbox(e, id) {
  let route = e.getAttribute("route") + id + "/" + e.checked;
  console.log(route);

  // Need to remove has summer col and add or delete rows depend on summer exist

  $.get(route, (data, status) => {
    console.log(status);
  });
}


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

let myButton = document.getElementsByName("dynamic");
let myInput = document.querySelectorAll(".viewPass");
myButton.forEach(function (element, index) {
  element.onclick = function () {
    if (myInput[index].type == "password") {
      myInput[index].setAttribute("type", "text");
      element.innerHTML = ' <i class="bi bi-eye-slash"></i>';
    } else {
      myInput[index].setAttribute("type", "password");
      element.innerHTML = ` <i class="bi bi-eye"></i>`;
    }
  };
});

//search and filter

function fieldSearch(query, searchableCells) {
  let searchQuery = query;

  for (const tableCell of searchableCells) {
    const row = tableCell.closest("tr");
    const value = tableCell.textContent.toLowerCase().replace(",", "");

    row.style.visibility = null;

    if (value.search(searchQuery) === -1) {
      row.style.visibility = "collapse";
    }
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".search-input").forEach((inputField) => {
    const tableRows = inputField
      .closest("table")
      .querySelectorAll("tbody > tr");
    const headerCell = inputField.closest("th");
    const otherHeaderCells = headerCell.closest("tr").children;
    const columnIndex = Array.from(otherHeaderCells).indexOf(headerCell);
    const searchableCells = Array.from(tableRows).map(
      (row) => row.querySelectorAll("td")[columnIndex]
    );

    inputField.addEventListener("input", () => {
      fieldSearch(inputField.value.toLowerCase(), searchableCells);
    });
  });
});
//end

//search bar

(function () {
  "use strict";

  var TableFilter = (function () {
    var Arr = Array.prototype;
    var input;

    function onInputEvent(e) {
      input = e.target;
      var table1 = document.getElementsByClassName(
        input.getAttribute("data-table")
      );
      Arr.forEach.call(table1, function (table) {
        Arr.forEach.call(table.tBodies, function (tbody) {
          Arr.forEach.call(tbody.rows, filter);
        });
      });
    }

    function filter(row) {
      var text = row.textContent.toLowerCase();
      //console.log(text);
      var val = input.value.toLowerCase();
      //console.log(val);
      row.style.display = text.indexOf(val) === -1 ? "none" : "table-row";
    }

    return {
      init: function () {
        var inputs = document.getElementsByClassName("table-filter");
        Arr.forEach.call(inputs, function (input) {
          input.oninput = onInputEvent;
        });
      },
    };
  })();

  TableFilter.init();
})();

// Filter Tables using Tabs
function filterTabs(colId, filterWord) {
  const inputField = document.getElementById(colId);
  const tableRows = inputField.closest("table").querySelectorAll("tbody > tr");
  const headerCell = inputField.closest("th");
  const otherHeaderCells = headerCell.closest("tr").children;
  const columnIndex = Array.from(otherHeaderCells).indexOf(headerCell);
  const searchableCells = Array.from(tableRows).map(
    (row) => row.querySelectorAll("td")[columnIndex]
  );
  fieldSearch(filterWord, searchableCells);
}

// Instructors Filter Tabs
document.getElementById("allInstractors")?.addEventListener("click", (e) => {
  filterTabs("tabsFilter", "");
});

let roles = document.getElementsByClassName("roles");
for (let i = 0; i < roles.length; i++) {
  roles[i].addEventListener("click", (e) => {
    filterTabs("tabsFilter", roles[i].innerText);
  });
}

// Buildings Filter Tabs
document.getElementById("allBuildings")?.addEventListener("click", (e) => {
  filterTabs("tabsFilter", "");
});

let buildings = document.getElementsByClassName("buildings");
for (let i = 0; i < buildings.length; i++) {
  buildings[i].addEventListener("click", (e) => {
    filterTabs("tabsFilter", buildings[i].innerText);
  });
}

// Courses Filter Tabs
document.getElementById("allCourses")?.addEventListener("click", (e) => {
  filterTabs("tabsFilter", "");
});

let courses = document.getElementsByClassName("courses");
for (let i = 0; i < courses.length; i++) {
  courses[i].addEventListener("click", (e) => {
    console.log(courses[i].innerText);
    filterTabs("tabsFilter", courses[i].innerText);
  });
}



function autoGenerate(e) {

    let form = document.getElementById("formModal");
    let formData = new FormData(form);


    if (formData.get("exec") == "auto") {
      // Open the iframe in a new window
      var newWindow = window.open("/pdf", "_blank");

      // window.location.href = "/pdf";

      // Add the iframe to the new window
      // newWindow.document.body.appendChild(iframe);
    }
}


// Print
function printElem(el) {
  $( document ).ready(function() {
    var printcontent = $('#' + el).clone();
    let headerStyle = `
      <style type="text/css" media="print">
        @page
        {
          size:  auto;   /* auto is the initial value */
          margin: 0;  /* this affects the margin in the printer settings */
        }

        html
        {
          background-color: #FFFFFF;
          margin: 0px;  /* this affects the margin on the html before sending to printer */
        }

        @page :first {
          margin-top: 0;
        }

        .tableWidth {
          transform: scale(0.99) !important;
        }

        body
        {
          margin: 30px 15px;
        }


      </style>
    `
    $('body').empty().html(printcontent);
    $('html').attr("xmlns", "http://www.w3.org/1999/xhtml");
    $('head').append(headerStyle);
    $('body').prepend(`<div class="mb-5"><img src="{{ url_for('static', filename='img/logo.png') }}" class="img-fluid" alt="alex-logo"></div>`);
    window.print();
    window.location.reload();
  });
}


// Dropdown
const dropdownToggle = document.getElementById('dropdownMenuButton');
const dropdownMenu = document.querySelector('.dropdown-menu');

dropdownToggle.addEventListener('click', () => {
  dropdownMenu.classList.toggle('show');
});

