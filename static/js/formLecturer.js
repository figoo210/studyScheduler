document.getElementsByClassName("error")[0].style.display="none"

function changeNameDr () {
  let nameDoctor=document.getElementById("nameDoc").value
  if(!isFinite(nameDoctor)){
    document.getElementsByClassName("nameDr")[0].innerText=nameDoctor
// document.getElementsByClassName("error")[0].style.display="none"
  }
  // else{
  //   document.getElementsByClassName("error")[0].style.display="block"

  // }
}
function changeMatr () {
  document.getElementsByClassName("matrial")[0].innerText=document.getElementById("matr").value

}
function changeLang () {
  document.getElementsByClassName("lang")[0].innerText=document.getElementById("lang").value

}
