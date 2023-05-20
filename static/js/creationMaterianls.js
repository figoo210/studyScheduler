
let formCounter = 1;
let formContOfAddTimes = 1;
const containerAddMaterial = document.getElementById("containerAddMaterial");
const containerAddTime = document.getElementById("containerAddTime");
const addButton = document.getElementById("add");
addButton.addEventListener("click", createAddMaterialsAgain);
const addTimeButton =document.getElementById("addTime");
addTimeButton.addEventListener("click", createAddTimesAgain);

checkRemove()
checkRemoveTime()
// Add a new Add Materials to the form
function createAddMaterialsAgain() {
 
  const form = containerAddMaterial.querySelector("section");
  const field = document.createElement("div");
  field.classList.add("field");
  field.innerHTML = `
  <div class="col-12 d-flex justify-content-between flex-wrap" >
  <div class="col-12 col-sm-6 col-md-2">
      <select class="form-select form-select-lg mb-3 " aria-label=".form-select-lg example">
          <option selected>الترم </option>
          <option value="1">احمد</option>
          <option value="2">محمد</option>
      </select>
  </div>
  <div class="col-12 col-sm-6 col-md-2">
      <select class="form-select form-select-lg mb-3 " aria-label=".form-select-lg example">
          <option selected>الأئحة </option>
          <option value="1">احمد</option>
          <option value="2">محمد</option>
      </select>
  </div>
  <div class="col-12 col-md-3">
      <select class="form-select form-select-lg mb-3 " aria-label=".form-select-lg example">
          <option selected> المواد</option>
          <option value="1">احمد</option>
          <option value="2">محمد</option>
      </select>
  </div>
  <div class="col-12 col-sm-6 col-md-2">
      <input type="text" class=" form-control form-control-lg " id="exampleFormControlInput1" placeholder="عدد المجموعات">

     
  </div>
 
  <div class="col-6 col-md-1">
  <button type="button" id="add" class="  btn btn-primaryTwo"  onclick="createAddMaterialsAgain()">
      <i class="bi bi-plus-lg text-primary"></i></button>
      <button type="button" class="remove removeAdd btn btn-primaryTwo bi bi-trash text-danger ">
      </button>
</div>
</div>
  `;
  form.appendChild(field);

  formCounter++;
  checkRemove()  // Add a click event listener to the new field's delete button
  const removeButton = field.querySelector(".remove");
  removeButton.addEventListener("click", removeFieldWithMaterial);
}
// Add a new Add Times to the form

function createAddTimesAgain(){
    const form = containerAddTime.querySelector("section");
    const field = document.createElement("div");
    field.classList.add("field");
    field.innerHTML = `
    <div class="col-12 d-flex justify-content-between flex-wrap" >
    <div class="col-12 col-md-2">
    <select class="form-select form-select-lg mb-3 " aria-label=".form-select-lg example">
        <option selected>اليوم </option>
        <option value="1">احمد</option>
        <option value="2">محمد</option>
    </select>
</div>
<div class="col-12 col-md-2">
    <select class="form-select form-select-lg mb-3 " aria-label=".form-select-lg example">
        <option selected>الفترة </option>
        <option value="1">احمد</option>
        <option value="2">محمد</option>
    </select>
</div>
<div class="col-12 col-md-7">
    <button type="button" id="add" class="  btn btn-primaryTwo"  onclick="createAddTimesAgain()">
        <i class="bi bi-plus-lg text-primary"></i></button>
        <button type="button" class="remove removeTime btn btn-primaryTwo bi bi-trash text-danger ">
        </button>
  </div>
  </div>
    `;
    form.appendChild(field);
  
    formContOfAddTimes++;
    checkRemoveTime();
    const removeButton = field.querySelector(".remove");
    removeButton.addEventListener("click", removeFieldWithTime);
}
// Remove a field from the form
function removeField(event) {
    const field = event.target.parentNode.parentNode;
    field.parentNode.removeChild(field);
  }
function removeFieldWithMaterial(event) {
//   const field = event.target.parentNode.parentNode;
//   field.parentNode.removeChild(field);
removeField(event)
  formCounter--;
  checkRemove();
}
function removeFieldWithTime(event) {
   
    removeField(event)

    formContOfAddTimes--;
    checkRemoveTime()

  }


function checkRemove(){
    let removeButton=  document.getElementsByClassName("removeAdd")

    if(formCounter <= 1 ){
        removeButton[0].style.display="none";


    }else{
        
        removeButton[0].style.display="";

    }
}
function checkRemoveTime(){
    let removeTButton=  document.getElementsByClassName("removeTime")

    if( formContOfAddTimes <= 1){
        removeTButton[0].style.display="none";


    }else{
        
       
        removeTButton[0].style.display="";

    }
}

