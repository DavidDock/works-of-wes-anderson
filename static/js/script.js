const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
var commentTextAreas = document.getElementsByTagName("textarea");

// clear all text areas //

for (let x of commentTextAreas) {
    x.value = "";
};

// messages taken from CI walkthrough//

setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);

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

// script for closing trailer modal and stopping trailer playing //
// Taken and adapted from CI blog walkthrough //

$(".btn-delete").click(function () {
    let commentId = $(this).attr("comment_id");
    let movieSlug = $(this).attr("movie_slug");
    let deleteCon = $("#deleteConfirm");
    deleteCon.attr('href', `delete_comment/${movieSlug}/${commentId}`);
    deleteModal.show();
});