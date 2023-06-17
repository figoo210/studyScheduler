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

function onFormSubmited2() {
  let form = document.getElementById("multiValuesForm2");
  let formData = new FormData(form);
  console.log(formData);
  let inputsArr = []
  let eachRow = {}
  // for (const [k, v] of formData) {
  //   if (eachRow.hasOwnProperty(k)) {
  //     console.log("HERE");
  //     inputsArr.push(eachRow);
  //     eachRow = {};
  //     eachRow[k] = v;
  //   } else {
  //     eachRow[k] = v;
  //   }
  // }
  // inputsArr.push(eachRow);
  // let formPostData = new FormData();
  // formPostData.append("data", JSON.stringify(inputsArr));

  // $.ajax({
  //   type: "POST",
  //   url: form.action,
  //   data: formPostData,
  //   processData: false,
  //   contentType: false,
  //   success: function() {
  //     window.location.href = form.getAttribute("redirectlink");
  //   }
  // });

}
