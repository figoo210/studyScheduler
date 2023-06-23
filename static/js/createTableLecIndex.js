const weekDays = [
  "السبت",
  "الأحد",
  "الإثنين",
  "الثلاثاء",
  "الاربعاء",
  "الخميس",
  "الجمعة",
];

let courseCard = () => {
  return `
  <ul class="list-group rounded-top rounded-6 col-4 m-1 position-relative ">

    <li class="bg-primary text-left d-flex px-1 border-0" style="padding: 0;">
      <i class="bi bi-x fs-4" style="padding: 0; margin: 0; color: #fff; cursor: pointer;"></i>
    </li>
    <li class="list-group-item bg-primary d-flex px-1 border-0" style="padding: 0.2rem;">
      <select
        class="form-control col-12"
        style="
          font-family: bootstrap-icons;
          border: 1px solid #ced4da;
          color: #6c757d;
          border-radius: .5rem;
          min-height: 100%;
        "
        aria-label=".form-select-lg example"
        name="instructor"
      >
        <option selected disabled>إسم المحاضر</option>

        {% for instructor in department.instructors %}
        <option value="{{ instructor.id }}">{{ instructor.name }}</option>
        {% endfor %}

      </select>
    </li>
    <li class="list-group-item bg-primary px-1 border-0" style="padding: 0.2rem;">
      <select
        class="form-control col-12"
        style="
          font-family: bootstrap-icons;
          border: 1px solid #ced4da;
          color: #6c757d;
          border-radius: .5rem;
          min-height: 100%;
        "
        aria-label=".form-select-lg example"
        name="course"
      >
        <option selected disabled>المادة</option>

        {% for course in department.courses %}
        <option value="{{ course.id }}">{{ course.name }}</option>
        {% endfor %}

      </select>
    </li>
    <li class="list-group-item bg-primary px-1 border-0" style="padding: 0.2rem;">
      <select
        class="form-control col-12"
        style="
          font-family: bootstrap-icons;
          border: 1px solid #ced4da;
          color: #6c757d;
          border-radius: .5rem;
          min-height: 100%;
        "
        aria-label=".form-select-lg example"
        name="room"
      >
        <option selected disabled>المكان</option>

        {% for building in context.buildings %}

        <optgroup label="{{ building.name }}">

          {% for room in context.rooms %}
          {% if room.building_id == building.id %}
          <option value="{{ room.id }}">{{ room.name }}</option>
          {% endif %}
          {% endfor %}

        </optgroup>

        {% endfor %}

      </select>
    </li>
    <li class="list-group-item bg-primary px-1 clockpicker border-0" style="padding: 0.2rem;">
      <input
        type="text"
        class="form-control col-12 text-center"
        style="
          font-family: bootstrap-icons;
          border: 1px solid #4372EA;
          color: #4372EA;
          border-radius: .5rem;
        "
        placeholder="وقت المحاضرة  &#xF293;"
        name="startTime"
      />
    </li>
  </ul>
  `;
};


function addTables(tables_num, container, targetContainer) {
  for (let i = 0; i < tables_num; i++) {
    container.appenChild(targetContainer)
  }

}

function addAccordionTaple(e) {
  let accordionStatus = e.querySelector("#accordionStatus");
  let groupsNum = e.querySelector("#groupsNum");
  let groupsNumValue = groupsNum.value;
  let tableBox = e.parentNode.parentNode.querySelector(".accordion-collapse");
  let tables = tableBox.getElementsByClassName("accordion-body");

  let groupContainer = tableBox.querySelector("#group-0");
  console.log(groupContainer);
  let newGroupContainer = groupContainer;
  newGroupContainer.id = `group-${groupsNumValue}`;
  tableBox.appenChild(newGroupContainer);


  if (groupsNumValue == "") {
    groupsNumValue = 1;
  } else {
    groupsNumValue = parseInt(groupsNumValue);
  }

  groupsNum.addEventListener("blur", (e) => {
    if (tables.length != groupsNumValue) {
      console.log("complete num of tables");
      if (groupsNum > tables.length) {
        console.log("add tables");
      } else {
        console.log("remove tables");
      }
    }
  });

  if (tables.length != groupsNumValue) {
    console.log("complete num of tables outside");
  }
}
