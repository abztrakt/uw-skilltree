$(function() {

    // show the handlebars content example
    $("#show_hb_content").click(function(e) {
        
        e.preventDefault(); 
        
        // compile handlebars template
        var template = Handlebars.compile($('#hb_content').html()),
            rendered = template();

        // paint it where? at the end of the content
        $("#hb_content_container").html(rendered);
    
    });

});


