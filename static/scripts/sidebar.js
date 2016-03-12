(function($){
    $(document).ready(function(){
        $('#toggle-sidebar').click(function(){
            $('.sidebar').toggleClass('sidebar-closed sidebar-opened');
            $('.sidebar').stop().animate({
                left: (($('.sidebar').hasClass('sidebar-opened')) ? '0' : (-$('.sidebar').width() - 10) ) + 'px'
            }, 300)
        });
    });
})(jQuery);