$(".searchIcon").click(function () {
  $(".searchForm").css("display", "flex");
  $(".searchInput").focus();
  $(".searchForm").css("width", "100%");
  $(".main").css("display", "none");
  $(".menu").css("display", "none");
});
$(".myNavbar .fa-times").click(function () {
  $(".searchForm").css("display", "none");
  $(".main").css("display", "flex");
  $(".menu").css("display", "block");
});
