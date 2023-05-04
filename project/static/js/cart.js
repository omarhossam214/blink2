var updateBtns = document.getElementsByClassName('update-cart')




for(var i=0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        var sizeInputs = document.querySelectorAll('.size__input');
        var selectedSize = '';
        if(!this?.dataset.size){
          for (var i = 0; i < sizeInputs.length; i++) {
          if (sizeInputs[i]?.checked) {
              selectedSize = sizeInputs[i]?.nextElementSibling?.nextElementSibling?.innerText;
              break;
            }
          }
        }else{
          selectedSize = this.dataset.size
        }
        

        console.log('productId:',productId,'action:',action,'selectedSize:',selectedSize)

        console.log('user:',user)
        if(user == 'AnonymousUser'){
            console.log('not logged in')
            updateUserOrder(productId, action, selectedSize)

        } else{
            updateUserOrder(productId, action, selectedSize)
        }
    }) 
}

function updateUserOrder(productId, action,selectedSize){
  console.log('user is logged in,sending data')


  var url = '/shop/update_item/'

  fetch(url,{
    method:'POST',
    headers:{
      'content-Type':'application/json',
      'X-CSRFToken' : csrftoken
    },
    body:JSON.stringify({'productId':productId,'action':action,'selectedSize':selectedSize})
  })


  .then((data) =>{
    console.log('data:', data)
    location.reload()
    
  })

}



var sizeInputs = document.querySelectorAll('.size__input');
var selectedSize = '';

for (var i = 0; i < sizeInputs.length; i++) {
if (sizeInputs[i].checked) {
    selectedSize = sizeInputs[i].nextElementSibling.nextElementSibling.innerText;
    break;
}
}

console.log(selectedSize);

