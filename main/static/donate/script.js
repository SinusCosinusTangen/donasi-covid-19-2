var $title = $('.js-title');
var copy   = '.js-copy';

$title.click(function () {
  $(this).next(copy).slideToggle();
  $(this).parent().siblings().children().next().slideUp();
  return false;
});

$(document).ready(function(){
    $(".pict").mouseenter(function(){
      $(this).css("width", 155);
    });
    $(".pict").mouseleave(function(){
      $(this).css("width", 105);
    });
  });