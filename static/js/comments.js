const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
var commentTextAreas = document.getElementsByTagName("textarea");

// clear all text areas //

for (let x of commentTextAreas) {
    x.value = "";
};

// script for deleting comment in modal //
// Taken and adapted from CI blog walkthrough //

$(".btn-delete").click(function () {
    let commentId = $(this).attr("comment_id");
    let movieSlug = $(this).attr("movie_slug");
    let deleteCon = $("#deleteConfirm");
    deleteCon.attr('href', `delete_comment/${movieSlug}/${commentId}`);
    deleteModal.show();
});

// script for editing comment //
// Taken and adapted from CI blog walkthrough //

$(".btn-edit").click(function () {
    let commentId = $(this).attr("comment_id");
    let movieSlug = $(this).attr("movie_slug");
    let subCom = document.getElementById(`${movieSlug}subcom`);
    let movieForm = document.getElementById(`${movieSlug}form`);
    let textArea = movieForm.getElementsByTagName("textarea")[0];
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    subCom.innerText = "Update";
    textArea.value = commentContent;
    movieForm.setAttribute("action", `edit_comment/${movieSlug}/${commentId}`);
});
