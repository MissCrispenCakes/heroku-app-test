function message(){
   var outputObj = document.getElementById("output");
   var msg = prompt("Please enter a message: ", "");
   outputObj.innerHTML = outputObj.innerHTML + msg + "<hr>";
}
