
function showDistrict(){
    let cityid = document.getElementById('city').value;
    let arr = document.getElementsByClassName('district');
    for (let i = 0; i < arr.length; i++){
        arr[i].style.display = 'none';
    }
    arr = document.getElementsByClassName(cityid);
    for (let i = 0; i < arr.length; i++) {
        arr[i].style.display = 'inline-block';
    }
    document.getElementById('district').value='none';
    document.getElementById('ward').value='none';
}

function showWard(){
    let districtid = document.getElementById('district').value;
    let arr = document.getElementsByClassName('ward');
    for (let i = 0; i < arr.length; i++){
        arr[i].style.display = 'none';
    }
    arr = document.getElementsByClassName(districtid);
    for (let i = 0; i < arr.length; i++) {
        arr[i].style.display = 'inline-block';
    }
    document.getElementById('ward').value='none';
}