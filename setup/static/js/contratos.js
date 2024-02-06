$(document).ready(function() {  

    //Mudar de aba
    $('#tabContratos tbody').on('click', 'tr', function() {
        const id_contrato = $(this).attr('data-id').toString();
        window.location.href = `/contratos/contrato/ficha/${id_contrato}/`;
    });

            
});