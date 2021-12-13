const csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
console.log(csrfmiddlewaretoken);

var $j = jQuery.noConflict();


function addQuantity(id) {

    // $j("#btn-sub-add"+id).attr('disabled', true)
    document.getElementById("btn-sub-add" + id).style.display = "block";


    payload = {
        "csrfmiddlewaretoken": csrfmiddlewaretoken,
        'id': id,
    }
    $j.ajax({
        type: "POST",
        dataType: "JSON",
        url: "/add/",
        timeout: 5000,
        data: payload,
        success: function (data) {
            if (data.status == "success") {
                let num = +$j('#' + id).text() + 1;
                $j('#' + id).text(num);// update quantity
                let total = +$j('#total-num').text().slice(0, -1) + (+$j('#price-' + id).text().slice(0, -1));
                $j('#total-num').text(total + '₫');// update total
                console.log($j('#' + id).text());
                console.log($j('#total-num').text());
                for (let i = 0; i < 10e3; i++) {
                    // console.log(i);
                }
                document.getElementById("btn-sub-add" + id).style.display = "none";
            }

        },
        error: function (data) {
            console.log(data);
        }
    })
}

async function subQuantity(id) {
    payload = {
        "csrfmiddlewaretoken": csrfmiddlewaretoken,
        "id": id
    }

    document.getElementById("btn-sub-add" + id).style.display = "block";

    $j.ajax({
        type: "POST",
        dataType: "json",
        url: "/sub/",
        timeout: 5000,
        data: payload,
        success: function (data) {
            if (data['status'] == 'success') {
                let num = +$j('#' + id).text() - 1;
                $j('#' + id).text(num);// update quantity
                let total = $j('#total-num').text().slice(0, -1) - $j('#price-' + id).text().slice(0, -1);
                $j('#total-num').text(total + '₫');// update total

                if (data['num'] == 0) {
                    $j('#number_in_cart').text($j('#number_in_cart').text() - 1);
                    $j('#order-' + id).remove();
                    // $j('#order-'+id).remove();
                    if (data['numInCart'] == 0) {
                        $j('#total').remove();
                        $j('#pay').remove();
                        $j('#cart').empty();
                        $j('#cart').append('<h1>Giỏ hàng</h1><h5>Không có sản phẩm nào</h5>');
                    }
                }

                for (let i = 0; i < 10e3; i++) {
                    // console.log(i);
                }
                document.getElementById("btn-sub-add" + id).style.display = "none";
            }

        },
        error: function (data) {
            console.log('error');
        }
    })
}

function deleteOrder(id) {

    total = $j('#total-num').text().slice(0, -1) - 1 * $j('#price-' + id).text().slice(0, -1) * $j('#' + id).text();
    $j('#total-num').text(total + '₫');// update total

    $j.ajax({
        type: 'POST',
        dataType: 'json',
        url: '/remove/',
        timeout: 5000,
        data: {
            "csrfmiddlewaretoken": csrfmiddlewaretoken,
            'id': id
        },
        success: function (data) {
            console.log(id);
            if (data['status'] == 'success') {
                $j('#order-' + id).remove();
                $j('#number_in_cart').text($j('#number_in_cart').text() - 1);
                // $j('#order-'+id).remove();
                if (data['numInCart'] == 0) {
                    $j('#total').remove();
                    $j('#pay').remove();
                    $j('#cart').empty();
                    $j('#cart').append('<h1>Giỏ hàng</h1><h5>Không có sản phẩm nào</h5>');

                }
                console.log(data);

            }
        }
    })
}