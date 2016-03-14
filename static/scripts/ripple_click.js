(function($){
    $(document).ready(function(){
        $(".ripple, .ripple-child").click(function(e){
            var parent, ink, d, x, y;
            parent = ($(this).hasClass('ripple')) ? $(this) : $(this).closest('.ripple-parent');

	        if (parent.find(".ink").length != 0){
	            parent.find(".ink").remove();
		    }
	        if ($(this).hasClass('ripple-negative')) {
		        parent.prepend("<span class='ink ink-negative'></span>");
		    } else if ($(this).hasClass('ripple-positive')) {
		        parent.prepend("<span class='ink ink-positive'></span>");
		    } else if ($(this).hasClass('ripple-dark')) {
		        parent.prepend("<span class='ink ink-dark'></span>");
		    } else if ($(this).hasClass('ripple-light')) {
		        parent.prepend("<span class='ink ink-light'></span>");
		    } else {
		        parent.prepend("<span class='ink'></span>");
		    }

	        ink = parent.find(".ink");

		    d = Math.max(parent.outerWidth(), parent.outerHeight());
		    ink.css({height: d, width: d});

	        x = e.pageX - parent.offset().left - ink.width()/2;
	        y = e.pageY - parent.offset().top - ink.height()/2;

	        ink.css({top: y+'px', left: x+'px'}).addClass("animate");
	    });
    });
})(jQuery);