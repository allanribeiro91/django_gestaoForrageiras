//Mudar de página com delegação de eventos
$('#tabProcessosAquisitivos tbody').on('click', 'tr', function() {
    //fetchAndRenderTableData();
    //const produtoId = $(this).attr('data-id').toString();
    window.location.href = `/proaq/ficha/dadosgerais`;
});


//Mudar de aba
$('#proaq_ficha_evolucao').click(function() {
    window.location.href = `/proaq/ficha/evolucao`;
});

//Mudar de aba
$('#proaq_ficha_dados_gerais').click(function() {
    window.location.href = `/proaq/ficha/dadosgerais`;
});

//Mudar de aba
$('#proaq_ficha_tramitacoes').click(function() {
    window.location.href = `/proaq/ficha/tramitacoes`;
});


$('#btnNovaTramitacao').click(function() {

    var modal = new bootstrap.Modal(document.getElementById('tramitacaoModal'));
    modal.show();

});