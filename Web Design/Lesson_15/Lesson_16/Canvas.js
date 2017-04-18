function mouse()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");

    window.addEventListener("mousemove", icon, false);

}

function icon(e){
    canvas.clearRect(0,0,600,600);
    var xPos = e.clientX;
    var yPos = e.clientY;
    var pic = new Image();

    pic.src = "https://alohacooks.files.wordpress.com/2012/06/soft-serve-ice-cream2.png";
    pic.addEventListener("load", function(){ canvas.drawImage(pic, 0, 0, 200, 200)}, false);
    canvas.pic(xPos, yPos);
}
window.addEventListener("load", mouse, false);