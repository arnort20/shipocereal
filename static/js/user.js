const arrowContainer = document.createElement("div");
arrowContainer.className = "col-md-10"
arrowContainer.className += " arrow__container"

const arrowTag = document.createElement("i");
arrowTag.className = "arrow";
arrowTag.className += " col-md-2";

const arrowText = document.createTextNode("\u2192");
arrowTag.appendChild(arrowText);
const first_placement = document.getElementById("myinfo");
first_placement.appendChild(arrowTag);

const container_activeOption = document.getElementsByClassName("useroptions__optiondisplay-col");
const id_prefix = "div__"



function ChangeUserOptions(id){
    /*MOVES THE ARROW AROUND IN THE MENUBAR*/
    var menubar__container = document.getElementById(id);
    menubar__container.appendChild(arrowTag);

    var current_menubar = document.getElementsByClassName("active__menubar");
    current_menubar[0].className = current_menubar[0].className.replace(" active__menubar", "");
    menubar__container.className += " active__menubar";

    /*CHANGES THE HEADER IN THE USER OPTION CONTAINER*/
    var current_title = document.getElementsByClassName("optiondisplay__header-title");
    var new_title = menubar__container.innerText.replace("\u2192","")

    current_title[0].innerText = new_title


    /*CHANGES THE CONTENT IN THE USER OPTIONS*/
    var activeOption = document.getElementsByClassName(id_prefix+id);

    var previouslyActive = document.getElementsByClassName(" active__option");
    previouslyActive[0].className = previouslyActive[0].className.replace(" active__option","");
    activeOption[0].className += " active__option";
}

