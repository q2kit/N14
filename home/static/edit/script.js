
function showHuyen(){
    let tinhid = document.getElementById('tinh').value;
    let arr = document.getElementsByClassName('huyen');
    for (let i = 0; i < arr.length; i++){
        arr[i].style.display = 'none';
    }
    arr = document.getElementsByClassName(tinhid);
    for (let i = 0; i < arr.length; i++) {
        arr[i].style.display = 'inline-block';
    }
    document.getElementById('huyen').value='none';
    document.getElementById('xa').value='none';
}

function showXa(){
    let huyenid = document.getElementById('huyen').value;
    let arr = document.getElementsByClassName('xa');
    for (let i = 0; i < arr.length; i++){
        arr[i].style.display = 'none';
    }
    arr = document.getElementsByClassName(huyenid);
    for (let i = 0; i < arr.length; i++) {
        arr[i].style.display = 'inline-block';
    }
    document.getElementById('xa').value='none';
}