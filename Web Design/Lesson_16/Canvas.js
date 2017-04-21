function mouse()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");

    window.addEventListener("mousemove", icon, false);

}

function icon(e){
    canvas.clearRect(0,0,6000,6000);
    var xPos = e.clientX;
    var yPos = e.clientY;
    var pic = new Image();
    pic.src = "https://alohacooks.files.wordpress.com/2012/06/soft-serve-ice-cream2.png";
    canvas.drawImage(pic, xPos, yPos, 100, 100);

}
window.addEventListener("load", mouse, false);