/*回到顶部*/
$(window).scroll(function () {
    if($(window).scrollTop() >= 300) {
        $('#toTop').removeClass('hidden');
        $('#toTop').fadeIn(300);
    }else {
        $('#toTop').fadeOut(300);
    }
});

$(function(){
    $('#toTop').click(function() {
        $('html, body').animate({scrollTop: 0}, 500);
    }); 
})




var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?d1d114373d7d0d47ff3a2ff038ca6060";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
