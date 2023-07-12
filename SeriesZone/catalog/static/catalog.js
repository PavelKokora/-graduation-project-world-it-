let body = document.getElementById('body')
var modal = document.getElementById("modalwin");
var btn = document.getElementById("filter-button");
var span = document.getElementsByClassName("close-filter")[0];
let catBtn = document.querySelector('.categoryButton');

// btn.onclick = function() {
//   modal.style.display = "block";
// }

modal.onclick = function() {

  modal.style.display = "none";

}



btn.onclick = function() {
  if (modal.style.display == 'none') {
      modal.style.display = "block";
  }else{
    modal.style.display = "none";
  }
}
