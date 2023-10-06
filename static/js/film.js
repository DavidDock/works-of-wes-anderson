// script for flippers toggle //

$(".flippers").click(function () {
    $(this.nextElementSibling).toggleClass("hidden");
});

$(".close-cont").click(function () {
    $(this.parentElement).toggleClass("hidden");
});

// script for closing trailer modal and stopping trailer playing //

$(".button-close").click(function () {
    let iFrame = $("#iframe");
    let videoSRC = $("#iframe").attr("src");
    iFrame.attr('src', videoSRC);
});
