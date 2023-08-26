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
function selectCourse(e) {
  let indx = e.parentNode.parentNode.id == "formRow" ? 0 : parseInt(e.parentNode.parentNode.id.split("-")[1]);
  console.log("###############################");
  console.log(indx);
  let semester = document.getElementsByName("semester");
  let regulation = document.getElementsByName("regulation");
  // let year = document.getElementsByName("year");
  semester = semester[indx];
  regulation = regulation[indx];
  // year = year[year.length - 1];
  let department = document.getElementsByName("department")[0];
  let course = document.getElementsByName("course")[indx];

  if (semester.value != "الترم" && regulation.value != "الائحة") {
    course.innerHTML = `<option selected disabled>المادة</option>`
    $.get("/api/courses", (data, status) => {
      for (let x = 0; x < data.length; x++) {
        if (
          data[x]["semester"] == semester.value || semester.value == "Summer" &&
          data[x]["regulation_id"] == regulation.value
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

function openCourseProfile(courseId) {
  window.location.href = `/course/${courseId}`;
}

function openInstructorReport(instructorId) {
  window.location.href = `/instructor/${instructorId}/courses`;
}

// Instructor Selector Search
function selectInstructor(e, instructorId) {
  e.addEventListener("click", (e) => {
    let instructor = e.target.parentNode.parentNode.parentNode.children[2];
    let resultBox = e.target.parentNode.parentNode.parentNode.children[1];
    let inputText = e.target.parentNode.parentNode.parentNode.children[0];
    instructor.value = instructorId;
    inputText.value = e.target.textContent;
    resultBox.innerHTML = "";
  });
}

function selectInstructorCourses(e, instructorId) {
  let instructor = e.parentNode.parentNode.parentNode.children[2];
  let resultBox = e.parentNode.parentNode.parentNode.children[1];
  let inputText = e.parentNode.parentNode.parentNode.children[0];
  instructor.value = instructorId;
  inputText.value = e.textContent.split(" (")[0];
  resultBox.innerHTML = "";

  document.getElementById("instructor_name").textContent = e.textContent.split(" (")[0];
  document.getElementById("instructor_role").textContent = e.textContent.split(" (")[1].replace(")", "");
  const listCont = document.getElementById("instructorCourses");
  listCont.innerHTML = "";
  $.get(`/api/instructor/courses/${instructorId}`, (data, status) => {
    for (let x = 0; x < data.length; x++) {
      const d = data[x];
      listCont.innerHTML += `
        <li class='row my-3'>
          <div class='col-9'>${d.course.name} - ${d.path_data.year_trans} قسم ${d.course.department} ${d.path_data.language_trans} ${d.path_data.program_trans}</div>
          <button class='btn btn-secondary col-3' type='button' onClick='fillAttendanceReport(${d.course_id}, "${d.path}")'>اختيار</button>
        </li><hr>
      `
    }
  });
}

function fillAttendanceReport(courseId, path) {
  console.log(courseId, path);
  $.get(`/api/attendance-report/${courseId}/${path}`, (data, status) => {
    console.log(data);
    document.getElementById("language").textContent = data.lecture.path_data.language_trans;
    document.getElementById("regulation").textContent = data.lecture.path_data.regulation_trans;
    document.getElementById("semester").textContent = data.course.semester_ar;
    document.getElementById("course").textContent = data.course.name;
    document.getElementById("credit_hrs").textContent = data.course.credit_hrs;
    const table_data = document.getElementById("table_data");
    const table_data2 = document.getElementById("table_data2");
    table_data.innerHTML = "";
    table_data2.innerHTML = "";
    let counter = 0;
    for (let i = 0; i < data.lecture_attendance.length; i++) {
      const element = data.lecture_attendance[i];

      if (i >= 7) {
        table_data2.innerHTML += `
          <tr class="text-center">
            <td scope="row">${element.date}</td>
            <td>${data.lecture.start_time}</td>
            <td>${data.lecture.end_time}</td>
            <td>${data.course.credit_hrs}</td>
            <td></td>
          </tr>
        `;
      } else {
        table_data.innerHTML += `
          <tr class="text-center">
            <td scope="row">${element.date}</td>
            <td>${data.lecture.start_time}</td>
            <td>${data.lecture.end_time}</td>
            <td>${data.course.credit_hrs}</td>
            <td></td>
          </tr>
        `;
      }

      counter++;

    }
    document.getElementById("total_hrs").textContent = `${counter * parseInt(data.course.credit_hrs)} ساعة`;
  });
}

// Course Selector Search
function selectCoursBySearch(e, courseId) {
  e.addEventListener("click", (e) => {
    let course = e.target.parentNode.parentNode.parentNode.children[2];
    let resultBox = e.target.parentNode.parentNode.parentNode.children[1];
    let inputText = e.target.parentNode.parentNode.parentNode.children[0];
    course.value = courseId;
    inputText.value = e.target.textContent;
    resultBox.innerHTML = "";
    console.log(course.value);
  });
}


// General Search ##################################################################################################

function generalSearch(e, endpoint, resultBoxId, executeFunction, isCustomFunction) {
  $.ajax({
    type: 'POST',
    url: endpoint,
    data: {search_text: e.value, table_type: e.name},
    dataType: 'json',
    success: function(data) {
      $(`#${resultBoxId}`).html("");
      if (e.value != "") {
        for (let index = 0; index < data.length; index++) {
          let d = data[index]
          let searchResultElement = document.createElement("li");
          let searchResult = document.createElement("a");
          // searchResult.setAttribute("href", "#");
          searchResult.setAttribute("class", "cursor");
          isCustomFunction ?
            searchResult.setAttribute("onClick", executeFunction.replace(")", `, ${d.id})`))
            : searchResult.setAttribute("onClick", `${executeFunction}(${d.id})`);
          searchResult.textContent = d.role ? `${d.name} (${d.role})` : d.name;
          searchResultElement.appendChild(searchResult);
          $(`#${resultBoxId}`).append(searchResultElement);
        }
      } else {
        $(`#${resultBoxId}`).html("");
      }
    }
  });
}



