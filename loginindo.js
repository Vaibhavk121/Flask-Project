// Login/Register form
// Author: Ian Pirro 
//------------------------------------
// Form will change from login to register and visa-versa based
// on if the user is already "registered"
// "Usernames" min-len is 5 chars
//
// Could be annoying... but fun anyways


// These users "already exist"
var users = [
  'Suresh',
  'Shivangi',
  'Tanashree',
  'Vaibhav'
]

var loginform = {

  init: function () {
    this.bindUserBox();
  },

  bindUserBox: function () {
    var result = {};

    $(".form").delegate("input[name='un']", 'blur', function () {
      var $self = $(this);

      // this grep would be replaced by $.post tp check db for user
      result = $.grep(users, function (elem, i) {
        return (elem.name == $self.val());
      });

      // This would be callback
      if (result.length === 1) {
        if ($("div.login-wrap").hasClass('register')) {
          loginform.revertForm();
          return;
        }
        else {
          return;
        }
      }

      if (!$("div.login-wrap").hasClass('register')) {
        if ($("input[name='un']").val().length > 4)
          loginform.switchForm();
      }

    });
  },
  switchForm: function () {
    var $html = $("div.login-wrap").addClass('register');
    $html.children('h2').html('Register');
    $html.find(".form input[name='pw']").after("<input type='password' placeholder='Re-type password' name='rpw' />");
    $html.find('button').html('Sign up');
    $html.find('a p').html('Have an account? Sign in');
  },
  revertForm: function () {
    var $html = $("div.login-wrap").removeClass('register');
    $html.children('h2').html('Login');
    $html.find(".form input[name='rpw']").remove();
    $html.find('button').html('Sign in');
    $html.find('a p').html("Don't have an account? Register");
  },
  submitForm: function () {
    e.preventDefault();
    alert("Submitting form...");
    var user = document.querySelector(".login-user").value;
    console.log(user);
  }

} // loginform {}


// Init login form
// loginform.init();
const loginForm = document.querySelector(".login-form");
const usernameInput = document.querySelector(".login-user");
loginForm.addEventListener("submit", (event) => {
  event.preventDefault();
  if (users.includes(usernameInput.value)) {
    console.log("Logged in.");
    window.location.replace("/main.html");
  }
  console.log("ok")
})


// vertical align box
//   (function (elem) {
//     elem.css("margin-top", Math.floor(($(window).height() / 2) - (elem.height() / 2)));
//   }($(".login-wrap")));

// $(window).resize(function () {
//   $(".login-wrap").css("margin-top", Math.floor(($(window).height() / 2) - ($(".login-wrap").height() / 2)));

// });