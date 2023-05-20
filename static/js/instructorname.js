// Get the plus icon
const plusIcon = document.querySelectorAll('.fa-plus');

plusIcon.forEach((icon) => {
  icon.addEventListener("click", add)
})

function add() {

  // Get the form container element
  const formContainer = document.querySelector('.inputs');

  // Create a new form element
  const newForm = document.createElement('div');
  newForm.classList.add('input-form', 'd-flex', 'flex-column');

  // Copy the existing form HTML and add it to the new form element
  newForm.innerHTML = formContainer.querySelector('.input-form').innerHTML;

  // Add a new delete icon to the new form element
  const newDeleteIcon = document.createElement('i');
  newDeleteIcon.classList.add('fa-solid', 'fa-trash-can');
  // icons.appendChild(newDeleteIcon)
  newForm.querySelector('.icons').appendChild(newDeleteIcon);

  const newPlusIcon = newForm.querySelector('.fa-plus');
  newPlusIcon.addEventListener("click", add)

  // Add the new form element to the form container
  formContainer.appendChild(newForm);

  // Add a click event listener to the new delete icon
  newDeleteIcon.addEventListener('click', () => {
    // Remove the parent element of the delete icon (i.e. the form element)
    newDeleteIcon.parentElement.parentElement.remove();
  });
}

// Get all the delete icons and add a click event listener to each one
const deleteIcons = document.querySelectorAll('.fa-trash-can');
deleteIcons.forEach((deleteIcon) => {
  deleteIcon.addEventListener('click', () => {
    // Remove the parent element of the delete icon (i.e. the form element)
    deleteIcon.parentElement.parentElement.remove();
  });
});

//=============================================================================================

