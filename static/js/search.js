function searchField(fieldId) {
  let targetField = document.getElementById(fieldId);
  let inputText = targetField.value;
  let resultBox = targetField.parentNode.children[1];
  let fieldData = JSON.parse(document.getElementById(fieldId + "-data").value.replace(/'/g, '"'));

  let words = [];
  if (inputText != "") {
    for (let i = 0; i < fieldData.length; ++i) {
      let j = -1;
      let correct = 1;

      while (correct == 1 && ++j < inputText.length) {
        if (fieldData[i].charAt(j) != inputText.charAt(j))
          correct = 0;
      }

      if (correct == 1) words.push(fieldData[i]);
      resultBox.innerHTML = "";
    }

    for (const key in words) {
      let searchResultElement = document.createElement("li");
      let searchResult = document.createElement("a");
      searchResult.setAttribute("href", "#");
      searchResult.setAttribute("onClick", "selectSearchResult(this)");
      searchResult.textContent = words[key];
      searchResultElement.appendChild(searchResult);
      resultBox.appendChild(searchResultElement);
    }

  } else {
    resultBox.innerHTML = "";
  }

  targetField.addEventListener("blur", (e) => {
    resultBox.innerHTML = "";
  });

}

function selectSearchResult(e) {
  let selectedResult = e.textContent;
  let inputText = document.getElementById(e.parentNode.parentNode.parentNode.children[0].id).value;
  console.log(inputText);
  let resultBox = e.parentNode.parentNode.parentNode.children[1];
  inputText = selectedResult;
  resultBox.innerHTML = "";
}
