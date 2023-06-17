$(document).ready(function () {
  let choicesExist = document.getElementById("choices-multiple-remove-button");
  if (choicesExist) {
    var multipleCancelButton = new Choices("#choices-multiple-remove-button", {
      removeItemButton: true,
      maxItemCount: 4,
    });
  }

  $('.clockpicker')?.clockpicker();

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

document.getElementById("doctors")?.addEventListener("click", (e) => {
  filterTabs("tabsFilter", "دكتور");
});

document.getElementById("helpers")?.addEventListener("click", (e) => {
  filterTabs("tabsFilter", "معيد");
});
