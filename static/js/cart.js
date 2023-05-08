var updateBtns = document.getElementsByClassName('update-cart');

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(event) {
        event.preventDefault();
        var sizeInputs = document.getElementsByName('size');
        var checkedSize = null;
        for (var j = 0; j < sizeInputs.length; j++) {
            if (sizeInputs[j].checked) {
                checkedSize = sizeInputs[j].value;
                break;
            }
        }
        var colorInputs = document.getElementsByName('color');
        var checkedColor = null;
        for (var k = 0; k < colorInputs.length; k++) {
            if (colorInputs[k].checked) {
                checkedColor = colorInputs[k].value;
                break;
            }
            // <-- MISSING CLOSING CURLY BRACE HERE
        }
        var productAddDiv = this.closest('.product-add');
        var button = productAddDiv.querySelector('.update-cart');
        var productId = button.dataset.product;
        var action = button.dataset.action;
        console.log(checkedSize, checkedColor, action, productId);
        updateUserOrder(checkedSize, checkedColor, action, productId);
    });
}

function updateUserOrder(checkedSize, checkedColor, action, productId) {
    console.log(checkedSize, checkedColor, action, productId);

    var url = '/shop/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action,
            'checkedColor': checkedColor,
            'checkedSize': checkedSize
        })
    })
    .then((data) => {
        console.log('data:', data);
        location.reload();
    });
}
