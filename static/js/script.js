// script for navbar toggle //

$(".toggle").click(function () {
    if ($(this).attr("src") === "/static/images/envelope.png") {
        $(this).attr("src", "/static/images/envelope-open.png");
    } else if ($(this).attr("src") === "/static/images/envelope-open.png") {
        $(this).attr("src", "/static/images/envelope.png");
    };
});

// script for flippers toggle //

$(".flippers").click(function(){
  $(this.nextElementSibling).toggleClass("hidden");
});

$(".close-cont").click(function(){
  $(this.parentElement).toggleClass("hidden");
});

// script for closing trailer modal and stopping trailer playing //

$(".button-close").click(function() {
  let iFrame = $("#iframe");
  let videoSRC = $("#iframe").attr("src");
  iFrame.attr('src', videoSRC);
});