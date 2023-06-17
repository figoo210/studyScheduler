function searchField(fieldId) {
  let targetField = document.getElementById(fieldId);
  let inputText = targetField.value;
  let resultBox = targetField.parentNode.children[1];
  let fieldData = JSON.parse(
    document.getElementById(fieldId + "-data").value.replace(/'/g, '"')
  );

  let words = [];
  if (inputText != "") {
    for (let i = 0; i < fieldData.length; ++i) {
      let j = -1;
      let correct = 1;

      while (correct == 1 && ++j < inputText.length) {
        if (fieldData[i].charAt(j) != inputText.charAt(j)) correct = 0;
      }

      if (correct == 1) words.push(fieldData[i]);
      resultBox.innerHTML = "";
    }

    for (const key in words) {
      let searchResultElement = document.createElement("li");
      let searchResult = document.createElement("a");
      searchResult.setAttribute("href", "#");
      searchResult.setAttribute("onClick", "selectSearchResult(this)");
      searchResult.textContent = words[key];
      searchResultElement.appendChild(searchResult);
      resultBox.appendChild(searchResultElement);
    }
  } else {
    resultBox.innerHTML = "";
  }

  // targetField.addEventListener("blur", (e) => {
  //   resultBox.innerHTML = "";
  // });
}

function selectSearchResult(e) {
  let fieldId = e.parentNode.parentNode.parentNode.children[0].id;
  let targetField = document.getElementById(fieldId);
  let resultBox = targetField.parentNode.children[1];
  let selectedResult = e.textContent;

  targetField.value = selectedResult;
  resultBox.innerHTML = "";

  getAutoFieldsByName(fieldId, selectedResult)
}

function getAutoFieldsByName(fieldId, selected) {
  // textSearchField-fullData
  let dataRoute = document.getElementById(fieldId + "-fullData").value;
  let autoFields = document.getElementsByClassName("textSearchField-autoField");

  $.get(dataRoute, (data, status) => {
    for (let x = 0; x < data.length; x++) {
      if (data[x]["name"] == selected) {
        for (let i = 0; i < autoFields.length; i++) {
          const element = autoFields[i];
          element.value = data[x][element.name];
        }
      }
    }
  });

}

// HTML Field Example
{/* <div class="col-3 mb-md-0 mb-3">
  <input
    type="text"
    value=""
    class="form-control form-control-lg col-12"
    id="textSearchField"
    onkeyup="searchField('textSearchField')"
    placeholder="الإسم"
  />
  <ul id="searchResultBox"></ul>
  <input
    hidden
    id="{{ 'textSearchField-' + 'data' }}"
    value='{{ ["Always","azulejo","to","change","an","azo","compound","third"] }}'
  />
</div>; */}



// Course Selector Search
function selectCourse() {
  let semester = document.getElementsByName("semester");
  let regulation = document.getElementsByName("regulation");
  // let year = document.getElementsByName("year");
  semester = semester[semester.length - 1];
  regulation = regulation[regulation.length - 1];
  // year = year[year.length - 1];
  let department = document.getElementsByName("department")[0];
  let course = document.getElementById("courseSearch");

  if (semester.value != "الترم" && regulation.value != "الائحة" && department != "") {
    course.innerHTML = `<option selected disabled>المادة</option>`
    $.get("/api/courses", (data, status) => {
      for (let x = 0; x < data.length; x++) {
        if (
          data[x]["semester"] == semester.value &&
          data[x]["regulation"] == regulation.value &&
          data[x]["department"] == department.value
        ) {
          const option = document.createElement("option");
          option.value = data[x]["id"];
          option.textContent = data[x]["name"];
          course.appendChild(option);
        }
      }
    });
  }
}


