let container = document.getElementById("form-container");
let formRow = document.getElementById("formRow");
// let addFormButton = document.getElementById("add-form-button");
// let deleteButtons = document.querySelectorAll(".delete-button");
// let addButtons = document.querySelectorAll(".add-button");
let formCounter = 1;

// addFormButton.addEventListener("click", addForm);
// deleteButtons.forEach((button) => button?.addEventListener("click", removeForm));
// addButtons.forEach((button) => button?.addEventListener("click", addForm));

checkRemove();

function checkRemove() {
  let btnRemove = document.getElementsByClassName("delete-button");
  if (btnRemove[0]) {
    if (formCounter <= 1) {
      btnRemove[0].style.display = "none";
    } else {
      btnRemove[0].style.display = "block";
    }
  }
}

// Create a function to add a new form
function addForm() {
  // Create a new form element
  let form = document.createElement("div");
  form.className = formRow.className + " mt-3";
  form.id = `form-${formCounter}`;
  form.innerHTML = formRow.innerHTML;

  // Add the form to the container
  container.appendChild(form);

  // Increment the form counter
  formCounter++;
  checkRemove();
  $(".clockpicker").clockpicker();
}

// Create a function to remove a form
function removeForm(e) {
  console.log(e.parentNode.parentNode.id);
  // Get the form ID from the delete button
  let formId = e.parentNode.parentNode.id;

  // Get the form element
  let form = document.getElementById(formId);

  // Remove the form from the container
  container.removeChild(form);

  formCounter--;
  checkRemove();
}

function onFormSubmited() {
  let form = document.getElementById("multiValuesForm");
  let formData = new FormData(form);
  let inputsArr = []
  let eachRow = {}
  for (const [k, v] of formData) {
    if (eachRow.hasOwnProperty(k)) {
      console.log("HERE");
      inputsArr.push(eachRow);
      eachRow = {};
      eachRow[k] = v;
    } else {
      eachRow[k] = v;
    }
  }
  inputsArr.push(eachRow);
  let formPostData = new FormData();
  formPostData.append("data", JSON.stringify(inputsArr));

  $.ajax({
    type: "POST",
    url: form.action,
    data: formPostData,
    processData: false,
    contentType: false,
    success: function() {
      window.location.href = form.getAttribute("redirectlink");
    }
  });

}
