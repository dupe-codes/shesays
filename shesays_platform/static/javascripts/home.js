 // Initialize varibles
  var $window = $(window);
  var $companyInput = $('#company-name'); // Input for username
  var $slider = $('.bxslider'); 
  var $loginPage = $('.login.page'); // The login page
  var $chatPage = $('.chat.page'); // The chatroom page


  // Prompt for setting a username
  var companyName;
  var clearedCompany = false;
  var j = jQuery.noConflict();
  j(document).ready(function () {
     // j('.bxslider').bxSlider();
   });
  // Sets the client's companyName
  function setCompanyName() {
    companyName = cleanInput($companyInput.html().trim());

    // If the companyName is valid
    if (companyName) {
      $loginPage.fadeOut();
      $chatPage.show();
      $loginPage.off('click');
      // Tell the server your username

    }
  }

  // Prevents input from having injected markup
  function cleanInput (input) {
    return $('<div/>').text(input).text();
  }

  // Keyboard events

  $window.keydown(function (event) {
    // Auto-focus the current input when a key is typed
    if (!(event.ctrlKey || event.metaKey || event.altKey)) {
      $companyInput.focus();
    }
    if (!clearedCompany) {
      $slider.css("color", "#222");
    }
    // When the client hits ENTER on their keyboard
    if (event.which === 13) {
      if (companyName) {
        typing = false;
      } else {
        setCompanyName();
      }
    }
  });

  $companyInput.click(function(event){
    $('.bxslider').css("color", "#222");
  });

  window.onload = function() {
    // $("#company-name").focus();
    $slider.bxSlider();
  };