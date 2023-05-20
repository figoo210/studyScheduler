    
        // Get the container element where the forms will be added
        const container = document.getElementById('form-container');

        // Get the add form button
        const addFormButton = document.getElementById('add-form-button');
        addFormButton.addEventListener('click', addForm);
        
        // Get all the delete buttons
        const deleteButtons = document.querySelectorAll('.delete-button');
        deleteButtons.forEach(button => button.addEventListener('click', removeForm));
        // Get all the delete buttons
        const addButtons = document.querySelectorAll('.add-button');
        addButtons.forEach(button => button.addEventListener('click', addForm));
        // Create a counter variable to keep track of the number of forms
        let formCounter = 1;
        checkRemove()
        function checkRemove(){
            let btnRemove=  document.getElementsByClassName("delete-button")
        
            if(formCounter <= 1){
                btnRemove[0].style.display="none"
        
            }else{
              btnRemove[0].style.display=""
        
            }
        }
        // Create a function to add a new form
        function addForm(event) {
           
            event.preventDefault();
          // Increment the form counter
          formCounter++;
          checkRemove()
          // Create a new form element
          const form = document.createElement('div');
          form.className="row g-0 justify-content-between-start align-items-center pb-4"
          form.id = `form-${formCounter}`;
        
          // Create 4 input fields
          const input1 = document.createElement('div');
          input1.className="row col-10 g-0 justify-content-between"
          input1.innerHTML = `
          <div class="col-12 col-md-3">
                    <select class="form-select addClassRooms form-select-lg mb-3 addClassRoomsPaddingSelect" aria-label=".form-select-lg example">
                        <option selected> اسم المبني</option>
                        <option value="1">مدرج 1</option>
                        <option value="2">مدرج ب</option>
                    </select>
                </div>
                <div class="col-12 col-sm-6 col-md-3 mb-md-0 mb-3">
                    <input type="text" class="form-control form-control-lg col-12" id="exampleFormControlInput1" placeholder="اسم المدرج ">
        
                   
                </div>
                <div class="col-12 col-sm-6 col-md-2 mb-md-0 mb-3">
                    <input type="text" class="form-control form-control-lg col-12" id="exampleFormControlInput2" placeholder=" العدد الرسمي">
        
                   
                </div>
                <div class="col-12 col-sm-6 col-md-2 mb-md-0 mb-3">
                    <input type="text" class="form-control form-control-lg col-12" id="exampleFormControlInput3" placeholder=" العدد الفعلي">
        
                   
                </div>
               
        
        
        
           
        
          `;
          input1.name = `input1-${formCounter}`;
        
         
        
        
          // Create a delete button
          const deleteButton = document.createElement('i');
          deleteButton.className = 'delete-button  text-danger bi bi-trash btn col-6 col-md-1';
          deleteButton.dataset.formId = `form-${formCounter}`;
        
        
          deleteButton.addEventListener('click', removeForm);
          const addButton = document.createElement('button');
          addButton.className = 'add-form-button btn   col-6  col-md-1 text-end';
          addButton.dataset.formId = `form-${formCounter}`;
          addButton.innerHTML = `  <i class="bi bi-plus-lg text-primary fs-4"></i>`;
          addButton.addEventListener('click', addForm);
        
          // Add the input fields and labels to the form
          form.appendChild(input1);
          form.appendChild(addButton);
          form.appendChild(deleteButton);
        
          // Add the form to the container
          container.appendChild(form);
        }
        
        // Create a function to remove a form
        function removeForm(event) {
            event.preventDefault();
            formCounter--;
            checkRemove()
          // Get the form ID from the delete button
          const formId = event.target.dataset.formId;
        
          // Get the form element
          const form = document.getElementById(formId);
        
          // Remove the form from the container
          container.removeChild(form);
        
        }