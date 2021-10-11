window.onload = function (){
    document.getElementById('inputOtp').style.display = "none";
    document.getElementById('submitOtp').style.display = "none";
    console.log(123)
}
function unhide() {
    document.getElementById('getOtp').style.display = "none";
    document.getElementById('inputOtp').style.display = "block";
    document.getElementById('submitOtp').style.display = "inline-block";
}