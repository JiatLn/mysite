/*回到顶部*/
$(window).scroll(function () {
    if($(window).scrollTop() >= 400) {
        $('#toTop').removeClass('hidden');
        $('#toTop').fadeIn(400);
    }else {
        $('#toTop').fadeOut(400);
    }
});

$(function(){
    $('#toTop').click(function() {
        $('html, body').animate({scrollTop: 0}, 500);
    }); 
})