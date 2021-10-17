window.onload = function () {
    document.getElementById('inputOtp').style.display = "none";
    document.getElementById('submitOtp').style.display = "none";
}

function unhide() {
    if (check(document.getElementById('inputPhone').value)) {
        document.getElementById('getOtp').style.display = "none";
        document.getElementById('inputOtp').style.display = "block";
        document.getElementById('submitOtp').style.display = "inline-block";
        document.getElementById('invalid').style.display = 'none';
    } else {
        document.getElementById('invalid').style.display = 'block';
    }
}

function check(s) {
    if (s[0] !== '0') return false;
    if (s.length !== 10) return false;
    return true;
}

document.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        unhide();
    }
});