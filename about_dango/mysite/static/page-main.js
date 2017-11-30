$(document).ready(function () {
  $(".my-menu-item").on("click", "a", function () {
    $(this).parent().toggleClass("active");
    var $spanEle = $(this).find("span");
    if ($spanEle.hasClass("glyphicon-menu-left")) {
      $spanEle.removeClass("glyphicon-menu-left").addClass("glyphicon-menu-down");
    } else {
      $spanEle.removeClass("glyphicon-menu-down").addClass("glyphicon-menu-left");
    }
  });
});