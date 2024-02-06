$(document).ready(function() {
    $("#toggleButton").click(function() {
        $("#dropdown").toggle();
    });

    $(document).keyup(function(e) {
        if (e.key === "Escape") { 
            $("#dropdown").hide();
        }
    });

    // Fechar dropdown quando clicar fora dele
    $(document).click(function(event) {
        var $trigger = $("#toggleButton");
        if($trigger !== event.target && !$trigger.has(event.target).length){
            $("#dropdown").hide();
        }
    });
});
