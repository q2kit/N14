
// function load() {
//     let cityid = document.getElementById('city').value;
//     let arr = document.getElementsByClassName('district');
//     for (let i = 0; i < arr.length; i++) {
//         if (arr[i].dataset.city == cityid) {
//             arr[i].style.display = 'block';
//         }
//         else {
//             arr[i].style.display = 'none';
//         }
//     }
//     let districtid = document.getElementById('district').value;
//     arr = document.getElementsByClassName('ward');
//     for (let i = 0; i < arr.length; i++) {
//         if(arr[i].dataset.district == districtid) {
//             arr[i].style.display = 'block';
//         }
//         else {
//             arr[i].style.display = 'none';
//         }
//     }
    

    
//     console.log('load ok');
// }


function showDistrict() {
    let cityid = document.getElementById('city').value;
    let arr = document.getElementsByClassName('district');
    for (let i = 0; i < arr.length; i++) {
        if (arr[i].dataset.city == cityid) {
            arr[i].style.display = 'block';
        }
        else {
            arr[i].style.display = 'none';
        }
    }
    arr = document.getElementsByClassName('ward');
    for (let i = 0; i < arr.length; i++) {
        arr[i].style.display = 'none';
    }
    document.getElementById('selectDistrict').display = 'block';
    document.getElementById('district').value = 'none';
    document.getElementById('selectWard').display = 'block';
    document.getElementById('ward').value = 'none';

    console.log('changed city');
}

function showWard() {
    let districtid = document.getElementById('district').value;
    let arr = document.getElementsByClassName('ward');
    for (let i = 0; i < arr.length; i++) {
        // console.log(arr[i].district+' '+districtid);
        if(arr[i].dataset.district == districtid) {
            arr[i].style.display = 'block';
        }
        else {
            arr[i].style.display = 'none';
        }
    }
    // arr = document.getElementsByClassName(districtid);
    // for (let i = 0; i < arr.length; i++) {
    //     arr[i].style.display = 'inline';
    // }
    document.getElementById('selectWard').display = 'block';
    document.getElementById('ward').value = 'none';

    console.log('changed district');
}