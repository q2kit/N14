function submit() {
    let ls = document.getElementsByClassName("user-box");
    for (let i = 0; i < ls.length; i++) {
        if (ls[i].getElementsByTagName("input")[0].value == "") {
            return;
        }
    }
    document.getElementById('form').submit();
}