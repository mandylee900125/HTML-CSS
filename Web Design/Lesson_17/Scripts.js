function drag(){
    picture = document.getElementById("iceCream");
    leftbox = document.getElementById("leftBox");
    
    picture.addEventListener("dragstart", startDrag, false);
    picture.addEventListener("dragend", endDrag, false);
    
    leftbox.addEventListener("dragenter", dragEnter, false);
    leftbox.addEventListener("dragleave", dragLeave, false);
    leftbox.addEventListener("dragover", function(e){e.preventDefault()}, false);
    leftbox.addEventListener("drop", drop, false);
    
}

function startDrag(e){
    var pic = '<img id = "iceCream" src = "https://alohacooks.files.wordpress.com/2012/06/soft-serve-ice-cream2.png">';
    e.dataTransfer.setData('Picture', pic);
}

function dragEnter(e){
    e.preventDefault();
    leftbox.style.background = "yellow";
    leftbox.style.border = "5px solid black";
}

function dragLeave(e){
    e.preventDefault();
    leftbox.style.background = "white";
    leftbox.style.border = "3px solid #ffa4e2";
}

function drop(e){
    e.preventDefault();
    leftBox.innerHTML = e.dataTransfer.getData('Picture');
}

function endDrag(e){
    pic = e.target;
    pic.style.visibility = "hidden";

}

window.addEventListener("load", drag, false);


