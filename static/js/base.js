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

