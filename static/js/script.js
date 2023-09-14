// script for navbar toggle //

$(".toggle").click(function () {
    if ($(this).attr("src") === "/static/images/envelope.png") {
        $(this).attr("src", "/static/images/envelope-open.png");
    } else if ($(this).attr("src") === "/static/images/envelope-open.png") {
        $(this).attr("src", "/static/images/envelope.png");
    };
});