$(".searchIcon").click(function () {
  $(".searchForm").css("display", "block");
  $(".searchInput").focus();
  $(".searchForm").css("width", "90%");
  $(".main").css("display", "none");
  $(".menu").css("display", "none");
});
$(".myNavbar .fa-times").click(function () {
  $(".searchForm").css("display", "none");
  $(".searchForm").css("width", "70%");
  $(".main").css("display", "block");
  $(".menu").css("display", "block");
});
