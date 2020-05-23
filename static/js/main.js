$(document).ready(function(){
    $('.navbar-nav').on('click', function(){
        $(this).siblings().removeClass('active');
        $(this).addClass('active');
    });
});