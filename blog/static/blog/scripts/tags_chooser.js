(function($){
    $(document).ready(function(){
        //$('#id_tags').hide();
        //alert($("#id_tags option").text());
        $('#id_tags option').each(function(){
            $('#tags-chooser').append(
              '<span class="tag' + ($(this).is(':selected') ? '' : ' tag-unselected') +                                     '">' + $(this).text() + '</span> '
            );
        });
        $('#tags-chooser .tag').click(function(){
            if ($(this).hasClass('tag-unselected')){
                $('#id_tags option:contains("' + $(this).text() + '")').attr("selected", "selected");
            } else {
                $('#id_tags option:contains("' + $(this).text() + '")').attr("selected", false);
            }
            $(this).toggleClass('tag-unselected')
        });
    });
})(jQuery);