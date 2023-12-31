const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
var commentTextAreas = document.getElementsByTagName("textarea");

// clear all text areas //

for (let x of commentTextAreas) {
    x.value = "";
}

// script for deleting comment in modal //
// Taken and adapted from CI blog walkthrough //

$(".btn-delete").click(function () {
    let commentId = $(this).attr("value");
    let movieSlug = $(this).attr("name");
    let deleteCon = $("#deleteConfirm");
    deleteCon.attr('href', `delete_comment/${movieSlug}/${commentId}`);
    deleteModal.show();
});

// script for editing comment //
// Taken and adapted from CI blog walkthrough //

$(".btn-edit").click(function () {
    let commentId = $(this).attr("value");
    let FilmId = $(this).attr("name");
    let MovieTitle = $(this).attr("title");
    let subCom = document.getElementById("subcom");
    let movieForm = document.getElementById("comment-form-id");
    let textArea = movieForm.getElementsByTagName("textarea")[0];
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    let addUpdateComment = document.getElementById("add-update-comment");
    let CommentFormInfo = document.getElementById("comment-form-info");
    let formIdChoice = document.getElementById("id_film");
    let formIdSelect = formIdChoice.getElementsByTagName("option")[0];
    formIdSelect.setAttribute("value", `${FilmId}`);
    formIdSelect.innerText = `${MovieTitle}`;
    addUpdateComment.innerText = "Edit Comment";
    CommentFormInfo.innerText = "Please edit your comment";
    subCom.innerText = "Update";
    textArea.value = commentContent;
    movieForm.setAttribute("action", `edit_comment/${commentId}`);
    addUpdateComment.scrollIntoView();
});
