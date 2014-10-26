var $window = $(window);
var $companyInput = $('#company-name'); // Input for username
var $slider = $('.bxslider'); 

function cleanInput(input) {
  return $('<div/>').text(input.trim()).text();
}

$window.keydown(function (event) {
  // Auto-focus the current input when a key is typed
  if (!(event.ctrlKey || event.metaKey || event.altKey)) {
    $companyInput.focus();
  }
  if (cleanInput($companyInput.html()).length > 0) {
    // hide the slider
    $slider.css("color", "#222");
  }
  // // When the client hits ENTER on their keyboard
  // if (event.which === 13) {
  //   if (companyName) {
  //     typing = false;
  //   } else {
  //     setCompanyName();
  //   }
  // }
});