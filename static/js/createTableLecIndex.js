let courseCard = (instructorsData, coursesData, buildingsData, roomsData) => {
  let instructors = () => {
    let options = "";
    for (let i = 0; i < instructorsData.length; i++) {
      const element = instructorsData[i];
      options += `<option value="${element.instructor.id}">${element.instructor.name}</option>`;
    }
    return options;
  };

  let rooms = () => {
    let options = "";
    for (let i = 0; i < buildingsData.length; i++) {
      const building = buildingsData[i];
      options += `<optgroup label="${building.name}">`;
      for (let j = 0; j < roomsData.length; j++) {
        const room = roomsData[j];
        if (room.building_id == building.id) {
          options += `<option value="${room.id}">${room.name}</option>`;
        }
      }
      options += `</optgroup>`;
    }
    return options;
  };

  let courses = () => {
    let options = "";
    for (let i = 0; i < coursesData.length; i++) {
      const element = coursesData[i];
      if (element.course_instructors.length >= 1) {
        let instructorId = "";
        for (let j = 0; j < element.course_instructors.length; j++) {
          const each = element.course_instructors[j];
          instructorId += each.instructor_id + ",";
          options += `<option value="${element.course.id}" instructorId="${instructorId}">${element.course.name}</option>`;
        }
      } else {
        options += `<option value="${element.course.id}" instructorId="">${element.course.name}</option>`;
      }
    }
    return options;
  };
  return `
  <ul class="list-group rounded-top rounded-6 col-4 m-1 position-relative dayCard">

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

        ${instructors()}

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
        onClick="coursesHandler(this);"
      >
        <option selected disabled>المادة</option>

        ${courses()}

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

        ${rooms()}

      </select>
    </li>
    <li class="list-group-item bg-primary px-1 clockpicker border-0" style="padding: 0.2rem;">
      <input
        type="text"
        value=""
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

let coursesHandler = (e) => {
  let options = e.getElementsByTagName("option");
  let instructorId =
    e.parentNode.parentNode.querySelector(`[name=instructor]`).value;
  for (let i = 1; i < options.length; i++) {
    const option = options[i];
    let instructorIds = option.getAttribute("instructorId");
    if (instructorIds.includes(instructorId)) {
      option.style.display = "block";
    } else {
      option.style.display = "none";
    }
  }
};

const weekDays = [
  "Saturday",
  "Sunday",
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
];

const inputFields = [
  {
    fieldName: "instructor",
    defaultValue: "إسم المحاضر",
  },
  {
    fieldName: "course",
    defaultValue: "المادة",
  },
  {
    fieldName: "room",
    defaultValue: "المكان",
  },
  {
    fieldName: "startTime",
    defaultValue: "",
  },
];

// # Need to check all primary keys with group num

// # Need to check room with day with start time

// # Need to check instructor with day with start time

// runtimeData example
// runtimeData = [
//   {
//     path: "accordionId_groupId_day",
//     day: "",
//     instructor: "",
//     course: "",
//     room: "",
//     startTime: "",
//   },
// ];

let runtimeData = [];

// Manual Timetable scheduling

function addNewGroup(groupNum, groupName, container, contentHtml) {
  let newGroupContainer = document.createElement("div");
  newGroupContainer.id = `group-${groupNum}`;
  newGroupContainer.className = "accordion-body p-5";
  newGroupContainer.innerHTML = contentHtml;
  newGroupContainer.querySelector(
    "#groupName"
  ).textContent = `مجموعة (${groupName})`;
  container.appendChild(newGroupContainer);
}

function removeLastGroup(container, groupToRemove) {
  container.removeChild(groupToRemove);
}

function handleTables(e) {
  $(".clockpicker").clockpicker();

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
        for (let i = 0; i < groupsNumValue - tables.length; i++) {
          addNewGroup(
            tables.length,
            tables.length + 1,
            tableBox,
            groupContainer.innerHTML
          );
        }
      } else {
        for (let i = 0; i < tables.length - groupsNumValue; i++) {
          removeLastGroup(tableBox, tables[tables.length - 1]);
        }
      }
    }
  });

  if (tables.length != groupsNumValue) {
    if (groupsNumValue > tables.length) {
      for (let i = 0; i < groupsNumValue - tables.length; i++) {
        addNewGroup(
          tables.length,
          tables.length + 1,
          tableBox,
          groupContainer.innerHTML
        );
      }
    } else {
      for (let i = 0; i < tables.length - groupsNumValue; i++) {
        removeLastGroup(tableBox, tables[tables.length - 1]);
      }
    }
  }

  // Handle Status
  let accordion = e.parentNode.parentNode;
  outer:
  for (let i = 0; i < inputFields.length; i++) {
    const inf = inputFields[i];
    let fields = accordion.querySelectorAll(`[name=${inf.fieldName}]`);
    if (fields.length >= 1) {
      for (let j = 0; j < fields.length; j++) {
        const element = fields[j];
        if (element.value == inf.defaultValue) {
          console.log("here");
          accordionStatus.textContent = "لم يكتمل";
          accordionStatus.classList.remove("bg-success");
          accordionStatus.classList.add("bg-warning");
          break outer;
        } else {
          accordionStatus.textContent = "اكتمل";
          accordionStatus.classList.remove("bg-warning");
          accordionStatus.classList.add("bg-success");
        }
      }
    } else {
      accordionStatus.textContent = "";
    }
  }

  // Manual Scheduling
  // manualScheduling();
}

function addCourseCard(e, day, data) {
  // Manual Scheduling
  // manualScheduling();

  let dayContainer = e.parentNode.parentNode.parentNode.querySelector(
    `.day-${day}`
  );
  let dayContent = dayContainer.querySelector("#dayContent");

  // Instructors, Courses, Buildings, Rooms, Lectures
  callAPI("/lecture/data", {
    method: "POST",
    body: data,
  })
    .then((data) => {
      let newCard = courseCard(
        data.instructors,
        data.courses,
        data.buildings,
        data.rooms
      );
      const parser = new DOMParser();
      const doc = parser.parseFromString(newCard , "text/html");
      dayContent.appendChild(doc.body.firstChild);
      $(".clockpicker").clockpicker();
    })
    .catch((err) => {
      console.log(err);
    });
}

function removeCourseCard(e) {
  e.parentNode.parentNode.remove();

  // Manual Scheduling
  // manualScheduling();
}

// Handle data with API
function callAPI(url, options) {
  return new Promise((resolve, reject) => {
    $.ajax(url, {
      method: options.method || "GET",
      data: options.body,
      success: function (response) {
        resolve(response);
      },
      error: function (err) {
        reject(err);
      },
    });
  });
}

// function manualScheduling() {
//   console.log(runtimeData);

//   let tables = document
//     .getElementById("accordionExample")
//     .getElementsByClassName("accordion-body");

//   for (let i = 0; i < tables.length; i++) {
//     const element = tables[i];

//     for (let j = 0; j < weekDays.length; j++) {
//       const day = weekDays[j];
//       let dayElement = element.querySelector(`.day-${day}`);
//       let dayCards = dayElement.querySelectorAll(".dayCard");

//       if (dayCards.length > 0) {
//         for (let c = 0; c < dayCards.length; c++) {
//           const card = dayCards[c];
//           let genericPath = `${element.parentNode.id}_${element.id}_${day}_${c}`;

//           if (runtimeData.length == 0) {
//             runtimeData.push({
//               path: genericPath,
//               day: day,
//               instructor:
//                 card.querySelector(`[name=instructor]`).value == "إسم المحاضر"
//                   ? ""
//                   : card.querySelector(`[name=instructor]`).value,
//               course:
//                 card.querySelector(`[name=course]`).value == "المادة"
//                   ? ""
//                   : card.querySelector(`[name=course]`).value,
//               room:
//                 card.querySelector(`[name=room]`).value == "المكان"
//                   ? ""
//                   : card.querySelector(`[name=room]`).value,
//               startTime: card.querySelector(`[name=startTime]`).value,
//             });
//           } else {
//             let pathes = []
//             for (let r = 0; r < runtimeData.length; r++) {
//               const rtd = runtimeData[r];
//               pathes.push(rtd.path);
//             }
//             if (pathes.includes(genericPath)) {
//               continue;
//             } else {
//               runtimeData.push({
//                 path: genericPath,
//                 day: day,
//                 instructor:
//                   card.querySelector(`[name=instructor]`).value == "إسم المحاضر"
//                     ? ""
//                     : card.querySelector(`[name=instructor]`).value,
//                 course:
//                   card.querySelector(`[name=course]`).value == "المادة"
//                     ? ""
//                     : card.querySelector(`[name=course]`).value,
//                 room:
//                   card.querySelector(`[name=room]`).value == "المكان"
//                     ? ""
//                     : card.querySelector(`[name=room]`).value,
//                 startTime: card.querySelector(`[name=startTime]`).value,
//               });
//             }
//           }
//         }
//       }
//     }
//   }


// }

function submitGroupTable(e) {

  let dataList = [];

  const element = e.parentNode.parentNode;

  for (let j = 0; j < weekDays.length; j++) {
    const day = weekDays[j];
    let dayElement = element.querySelector(`.day-${day}`);
    let dayCards = dayElement.querySelectorAll(".dayCard");

    if (dayCards.length > 0) {
      for (let c = 0; c < dayCards.length; c++) {
        const card = dayCards[c];
        let genericPath = `${element.parentNode.id}_${element.id}_${day}_${c}`;

        dataList.push({
          path: genericPath,
          day: day,
          instructor:
            card.querySelector(`[name=instructor]`).value == "إسم المحاضر"
              ? ""
              : card.querySelector(`[name=instructor]`).value,
          course:
            card.querySelector(`[name=course]`).value == "المادة"
              ? ""
              : card.querySelector(`[name=course]`).value,
          room:
            card.querySelector(`[name=room]`).value == "المكان"
              ? ""
              : card.querySelector(`[name=room]`).value,
          startTime: card.querySelector(`[name=startTime]`).value,
        });
      }
    }
  }

  console.log(dataList);
  let alertBox = element.querySelector("#alert")

  // callAPI
  callAPI("/lecture/add", {
    method: "POST",
    body: JSON.stringify(dataList),
  })
  .then((data) => {
    console.log(data);
    if (data.status == false) {
      alertBox.innerHTML = data.msg;
      alertBox.classList.add("alert-danger");
      alertBox.classList.remove("alert-success");
    } else {
      alertBox.innerHTML = data.msg;
      alertBox.classList.add("alert-success");
      alertBox.classList.remove("alert-danger");

    }
  })
  .catch((err) => {
    console.log(err);
      alertBox.innerHTML = "هذه المحاضرة موجودة بالفعل";
      alertBox.classList.add("alert-danger");
      alertBox.classList.remove("alert-success");
  });

}
