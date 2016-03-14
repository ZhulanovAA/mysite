(function($){
    $(document).ready(function(){
        var url = window.location.href;
        if (!url.includes('page=')) {
            if (url.includes('?')) {
                url += '&page=';
            } else {
                url += '?page=';
            }
        }
        $('#pages-indicator button.unselected').click(function(){
                window.location = url.replace(/page=[^&$]*/, 'page=' + $(this).text());
        });
        $('#pages-indicator #next-page-button').click(function(){
                window.location = url.replace(/page=[^&$]*/, 'page=' + (parseInt($('#current-page-button').text()) + 1));
        });
        $('#pages-indicator #prev-page-button').click(function(){
                window.location = url.replace(/page=[^&$]*/, 'page=' + (parseInt($('#current-page-button').text()) - 1))
        });
    });
})(jQuery);