let container2 = document.getElementById("form-container2");
let formRow2 = document.getElementById("formRow2");
// let addFormButton = document.getElementById("add-form-button");
// let deleteButtons = document.querySelectorAll(".delete-button");
// let addButtons = document.querySelectorAll(".add-button");
let formCounter2 = 1;

// addFormButton.addEventListener("click", addForm);
// deleteButtons.forEach((button) => button?.addEventListener("click", removeForm));
// addButtons.forEach((button) => button?.addEventListener("click", addForm));

checkRemove2();

function checkRemove2() {
  let btnRemove = document.getElementsByClassName("delete-button2");
  if (btnRemove[0]) {
    if (formCounter2 <= 1) {
      btnRemove[0].style.display = "none";
    } else {
      btnRemove[0].style.display = "block";
    }
  }
}

// Create a function to add a new form
function addForm2() {
  // Create a new form element
  let form = document.createElement("div");
  form.className = formRow2.className + " mt-3";
  form.id = `form2-${formCounter2}`;
  form.innerHTML = formRow2.innerHTML;

  // Add the form to the container
  container2.appendChild(form);

  // Increment the form counter
  formCounter2++;
  checkRemove2();
  $(".clockpicker").clockpicker();
}

// Create a function to remove a form
function removeForm2(e) {
  console.log(e.parentNode.parentNode.id);
  // Get the form ID from the delete button
  let formId = e.parentNode.parentNode.id;

  // Get the form element
  let form = document.getElementById(formId);

  // Remove the form from the container
  container2.removeChild(form);

  formCounter2--;
  checkRemove2();
}

function instructorAssignFormSubmit(e) {
  let form = document.getElementById("multiValuesForm2") || e.parentNode.parentNode;
  console.log(form);
  let formData = new FormData(form);
  let instructor_course = [];
  let instructor_time = [];

  let courses = document.getElementsByName("course");
  for (let i = 0; i < courses.length; i++) {
    let groups_num = document.getElementsByName("groupsNumber")[i].value;
    instructor_course.push({
      instructor_id: formData.get("id"),
      course_id: courses[i].value,
      groups_num: groups_num
    });
  }

  let weekDay = document.getElementsByName("weekDay");
  for (let i = 0; i < weekDay.length; i++) {
    let startTime = document.getElementsByName("startTime")[i].value;
    let endTime = document.getElementsByName("endTime")[i].value;
    instructor_time.push({
      instructor_id: formData.get("id"),
      day_of_week: weekDay[i].value,
      start_time: startTime,
      end_time: endTime
    });
  }

  let instructorAssignObj = {
    instructor_course: instructor_course,
    instructor_time: instructor_time
  };

  $.ajax({
    type: "POST",
    url: form.action,
    data: JSON.stringify(instructorAssignObj),
    processData: false,
    contentType: false,
    success: function() {
      window.location.href = form.getAttribute("redirectlink");
    }
  });

}
