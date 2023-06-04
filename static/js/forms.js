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
  if (formCounter <= 1) {
    btnRemove[0].style.display = "none";
  } else {
    btnRemove[0].style.display = "block";
  }
}

// Create a function to add a new form
function addForm() {
  // Create a new form element
  let form = document.createElement("div");
  form.className = formRow.className + " mt-3";
  form.id = `form-${formCounter}`;
  form.innerHTML = formRow.innerHTML;

  console.log("");

  // Add the form to the container
  container.appendChild(form);

  // Increment the form counter
  formCounter++;
  checkRemove();
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
