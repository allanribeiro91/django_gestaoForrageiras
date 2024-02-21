$(document).ready(function() {  

    $('#urt_ciclos').on('click', function() {
        window.location.href = `/urts/ficha/ciclo/`;
    });


    //Mudar de aba
    $('#tabURTs tbody').on('click', 'tr', function() {
        const id_urt = $(this).attr('data-id').toString();
        window.location.href = `/urts/ficha/${id_urt}/`;
    });


    

            
});