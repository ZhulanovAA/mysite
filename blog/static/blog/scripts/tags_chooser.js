(function($){
    $(document).ready(function(){
        $('#id_tags option').each(function(){
            $('#tags-chooser').append(
              '<span class="tag' + ($(this).is(':selected') ? '' : ' unselected') +                                     '">' + $(this).text() + '</span> '
            );
        });
        $('#tags-chooser .tag').click(function(){
            if ($(this).hasClass('unselected')){
                $('#id_tags option:contains("' + $(this).text() + '")').attr("selected", "selected");
            } else {
                $('#id_tags option:contains("' + $(this).text() + '")').attr("selected", false);
            }
            $(this).toggleClass('unselected')
        });
    });
})(jQuery);