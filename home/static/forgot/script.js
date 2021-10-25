window.onload = function () {
    document.getElementById('Otp').style.display = "none";
    document.getElementById('submitOtp').style.display = "none";
}

function unhide() {
    if (check(document.getElementById('inputPhone').value)) {//check phone number ok
        document.getElementById('getOtp').style.display = "none";
        document.getElementById('submitOtp').style.display = "inline-block";
        document.getElementById('invalid').style.display = 'none';
        document.getElementById('Otp').style.display = "block";
        document.getElementById("inputOtp").focus();
    } else {
        document.getElementById('inputPhone').focus();
        document.getElementById('invalid').style.display = 'block';
    }
}

function check(s) {
    if (s[0] !== '0') return false;
    if (s.length !== 10) return false;
    return true;
}

document.addEventListener("keypress", function(event) {
    if (event.key === "Enter"){
        unhide();
    }
});