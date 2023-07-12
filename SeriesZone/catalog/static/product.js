let modWin = document.getElementById('modalwindow');
let closeBuyButton = document.getElementById('closeBuyButton');
let buyButton = document.getElementById('buy-button');

let raitingInCard = document.querySelector('.raiting-in-card');
let a = Number(raitingInCard.textContent);

if(a >= 8){
  raitingInCard.style.color = '#46ac3b';
}else if(a <= 6 & a >3){
  raitingInCard.style.color = 'yellow';
}else if(a <= 3){
  raitingInCard.style.color = 'red';
};


// <input id="url" value="{% url 'transport_url' %}" hidden>
$(document).ready(function(){
  $(".card-series").each(function(index, element){
    console.log(22);
    $(element).click(function(event){
      console.log(11);
      $.ajax({
        url:window.location.href,
        type:'get',
        data:{
          "series_select":$(element).val(),
        },
        success: function(response){
          console.log(response.series_data);
          var vid = document.getElementById('videoPlay');
          vid.src = response.series_data

        }
      });
    });
  });
  $(".season-select-button").click(function(event){
    
    $.ajax({
      url:document.querySelector('#url').value,
      type:'get',
      data:{
        "season-select":$(this).val(),
      },
      success: function(response){
        $('.container-of-series').empty();
        
        for (let index in response.series){
          const Series = ` 
                     
          <button class="card-series" value = "${response.series[index].id}">
              
              <img src = "/media/${response.series[index].preview}" >
              <p>${response.series[index].number_of_series}. ${response.series[index].name}</p>
              
          </button>
          `;

          $('.container-of-series').append(Series);
        }

        
      }
    });
  });
});



function addBasket(event) {
  let button = event.target
  button.textContent = "Видалити з бібліотеки";
  button.classList.remove("button-add-in-basket");
  button.classList.add("button-dell-in-basket");
  button.removeEventListener("click",addBasket)
  let buttonRemoveBasket = document.querySelector(".button-dell-in-basket");
  setTimeout(()=>{buttonRemoveBasket.addEventListener("click",removeBasket)},500)
  event.preventDefault()

  $.ajax({
    url:document.querySelector('#url-library').value,
    type:'get',
    data:{
      "library":"true"
    },
  });
  
}

function removeBasket(event) {
  let button = event.target
  button.textContent = "Додати у бібліотеку";
  button.classList.remove("button-dell-in-basket");
  button.classList.add("button-add-in-basket");
  button.classList.add("modal-button");
  button.removeEventListener("click",removeBasket)
  let buttonAddBasket = document.querySelector(".button-add-in-basket");
  setTimeout(()=>{buttonAddBasket.addEventListener("click",addBasket)},500)

  $.ajax({
    url:document.querySelector('#url-library').value,
    type:'get',
    data:{
      "delete_library":"true"
    }
  });
}

let buttonAddBasket = document.querySelector(".button-add-in-basket");
let buttonRemoveBasket = document.querySelector(".button-dell-in-basket");


if (buttonAddBasket != null){
  buttonAddBasket.addEventListener("click",addBasket)
}
if (buttonRemoveBasket != null){
  buttonRemoveBasket.addEventListener("click",removeBasket)
}



// var modal2 = document.getElementById("mySeriesModal");
// var btn2 = document.getElementById("openModalButtonSerial");
// var span2 = document.getElementsByClassName("close-series")[0];

// btn2.onclick = function() {
//   modal.style.display = "block";
// }

// span2.onclick = function() {
//   modal.style.display = "none";
// }

// window.onclick = function(event) {
//   if (event.target == modal) {
//       modal.style.display = "none";
//   }
// }

var modalfan = document.getElementById("myModal");
var btnfan = document.getElementById("openModalButton");
var spanfan = document.getElementsByClassName("close")[0];

btnfan.onclick = function() {
  modalfan.style.display = "block";
}

spanfan.onclick = function() {
  modalfan.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
      modalfan.style.display = "none";
  }
}

