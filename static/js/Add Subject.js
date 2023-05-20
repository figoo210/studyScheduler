const plusbutton=
document.querySelector("button");
plusbutton.addEventListener('click',cloneelement);

function cloneelement(){
    var element=
    document.getElementById("mydiv")
    var clone=
    element.cloneNode(true);
    document.body.appendChild(clone);
};


const form=
document.getElementById("my-form")



const savebutton=
document.getElementById("save-button");

savebutton.onclick= 
function(){
    form.submit();
    alert("تم حفظ البيانات بنجاح");
    window.history.back();
}

const cancelbutton=
document.getElementById("camcel-button");

cancelbutton.onclick=function(){
    form.reset();
    window.history.back();
}


