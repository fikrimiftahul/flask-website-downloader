// sidebar
var sidemenu = document.getElementById("sidemenu");

function openmenu() {
  sidemenu.style.right = "0";
}
function closemenu() {
  sidemenu.style.right = "-200px";
}
// copyright year
function todayDate(){
  var d = new Date();
  var n = d.getFullYear() + "  ";
  return document.getElementById("date").innerHTML = n;
}
// flash message
var messages = document.getElementById("flash-messages");
		if (messages) {
		    messages.style.display = "block";
		    setTimeout(function() {
		        messages.style.display = "none";
		    }, 5000);
		}