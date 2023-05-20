//delete row
$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip();
	var actions = $("table td:last-child").html();
	$(document).on("click", ".delete", function(){
        $(this).parents("tr").remove();
		$(".add-new").removeAttr("disabled");
    });
});

//search and filter
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
		const searchQuery = inputField.value.toLowerCase();
  
		for (const tableCell of searchableCells) {
		  const row = tableCell.closest("tr");
		  const value = tableCell.textContent.toLowerCase().replace(",", "");
  
		  row.style.visibility = null;
  
		  if (value.search(searchQuery) === -1) {
			row.style.visibility = "collapse";
		  }
		}
	  });
	});
  });
//end

//search bar

(function() {
	'use strict';

var TableFilter = (function() {
 var Arr = Array.prototype;
		var input;
  
		function onInputEvent(e) {
			input = e.target;
			var table1 = document.getElementsByClassName(input.getAttribute('data-table'));
			Arr.forEach.call(table1, function(table) {
				Arr.forEach.call(table.tBodies, function(tbody) {
					Arr.forEach.call(tbody.rows, filter);
				});
			});
		}

		function filter(row) {
			var text = row.textContent.toLowerCase();
       //console.log(text);
      var val = input.value.toLowerCase();
      //console.log(val);
			row.style.display = text.indexOf(val) === -1 ? 'none' : 'table-row';
		}

		return {
			init: function() {
				var inputs = document.getElementsByClassName('table-filter');
				Arr.forEach.call(inputs, function(input) {
					input.oninput = onInputEvent;
				});
			}
		};
 
	})();

  /*console.log(document.readyState);
	document.addEventListener('readystatechange', function() {
		if (document.readyState === 'complete') {
      console.log(document.readyState);
			TableFilter.init();
		}
	}); */
  
 TableFilter.init(); 
})();