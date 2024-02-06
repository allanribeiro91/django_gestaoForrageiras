$(document).ready(function() {
    $("#profile-pic-img").click(function() {
        $("#dropdown").toggle();
    });

    $(document).keyup(function(e) {
        if (e.key === "Escape") { 
            $("#dropdown").hide();
        }
    });

    // Fechar dropdown quando clicar fora dele
    $(document).click(function(event) {
        var $trigger = $("#profile-pic");
        if($trigger !== event.target && !$trigger.has(event.target).length){
            $("#dropdown").hide();
        }
    });
});
