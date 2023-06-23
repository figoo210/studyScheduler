
let courseCard = () => {
  return `
  <ul class="list-group rounded-top rounded-6 col-4 m-1 position-relative ">

    <li class="bg-primary text-left d-flex px-1 border-0" style="padding: 0;">
      <i class="bi bi-x fs-4" style="padding: 0; margin: 0; color: #fff; cursor: pointer;" onClick="removeCourseCard(this)"></i>
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

const inputFields = [
  {
    fieldName: "instructor",
    defaultValue: "إسم المحاضر"
  },
  {
    fieldName: "course",
    defaultValue: "المادة"
  },
  {
    fieldName: "room",
    defaultValue: "المكان"
  },
  {
    fieldName: "startTime",
    defaultValue: ""
  }
]

// Manual Timetable scheduling

function addNewGroup(groupNum, groupName, container, contentHtml) {

  let newGroupContainer = document.createElement("div");
  newGroupContainer.id = `group-${groupNum}`;
  newGroupContainer.className = "accordion-body p-5";
  newGroupContainer.innerHTML = contentHtml;
  newGroupContainer.querySelector("#groupName").textContent = `مجموعة (${groupName})`
  container.appendChild(newGroupContainer);
}

function removeLastGroup(container, groupToRemove) {
  container.removeChild(groupToRemove);
}

function handleTables(e) {
  let accordionStatus = e.querySelector("#accordionStatus");
  let groupsNum = e.querySelector("#groupsNum");
  let groupsNumValue = groupsNum.value;
  let tableBox = e.parentNode.parentNode.querySelector(".accordion-collapse");
  let tables = tableBox.getElementsByClassName("accordion-body");
  let groupContainer = tableBox.querySelector("#group-0");

  // Handle Number of groups
  if (groupsNumValue == "") {
    groupsNumValue = 1;
  } else {
    groupsNumValue = parseInt(groupsNumValue);
  }

  groupsNum.addEventListener("blur", (e) => {
    if (tables.length != groupsNumValue) {
      if (groupsNumValue > tables.length) {
        for (let i = 0; i < (groupsNumValue - tables.length); i++) {
          addNewGroup(tables.length, tables.length + 1, tableBox, groupContainer.innerHTML);
        }
      } else {
        for (let i = 0; i < (tables.length - groupsNumValue); i++) {
          removeLastGroup(tableBox, tables[tables.length - 1])
        }
      }
    }
  });

  if (tables.length != groupsNumValue) {
    if (groupsNumValue > tables.length) {
      for (let i = 0; i < (groupsNumValue - tables.length); i++) {
        addNewGroup(tables.length, tables.length + 1, tableBox, groupContainer.innerHTML);
      }
    } else {
      for (let i = 0; i < (tables.length - groupsNumValue); i++) {
        removeLastGroup(tableBox, tables[tables.length - 1])
      }
    }
  }

  // Handle Status
  let accordion = e.parentNode.parentNode;
  for (let i = 0; i < inputFields.length; i++) {
    const inf = inputFields[i];
    let fields = accordion.querySelectorAll(`[name=${inf.fieldName}]`);
    if (fields.length >= 1) {
      for (let j = 0; j < fields.length; j++) {
        const element = fields[j];
        if (element.value == inf.defaultValue) {
          accordionStatus.textContent = "لم يكتمل";
          accordionStatus.classList.remove("bg-success");
          accordionStatus.classList.add("bg-danger");
        } else {
          accordionStatus.textContent = "اكتمل";
          accordionStatus.classList.remove("bg-danger");
          accordionStatus.classList.add("bg-success");
        }
      }
    } else {
      accordionStatus.textContent = "";
    }
  }

}

function addCourseCard(e, day) {
  let dayContainer = e.parentNode.parentNode.parentNode.querySelector(`.day-${day}`);
  console.log(dayContainer);
  dayContainer.querySelector("#dayContent").innerHTML += courseCard();
  $(".clockpicker").clockpicker();
}

function removeCourseCard(e) {
  e.parentNode.parentNode.remove();
}

// Handle data with API
function callAPI(url, options) {
  return new Promise((resolve, reject) => {
    $.ajax(url, {
      method: options.method || 'GET',
      data: options.body,
      success: function(response) {
        resolve(response);
      },
      error: function(err) {
        reject(err);
      }
    })
  });
}

// Instructors, Courses, InstructorCourses, Buildings, Rooms, Lectures
