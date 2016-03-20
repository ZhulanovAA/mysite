(function($){
    $(document).ready(function(){
        $('.labeled-block').focusin(function(){
            $(this).children('label').css({color: '#2196F3'});
        });
        $('.labeled-block').focusout(function(){
            $(this).children('label').css({color: '#9E9E9E'});
        });
    });
})(jQuery);