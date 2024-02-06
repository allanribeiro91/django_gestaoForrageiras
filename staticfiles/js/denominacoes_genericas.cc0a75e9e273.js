

//Deletar
$(document).ready(function() {
    $('#apagarDenominacao').on('click', function() {
        const denominacaoId = $('#id').val();  // Pega o ID da denominação do campo de input
    
        if (!denominacaoId) { //Trata-se de um novo registro que ainda não foi salvo
            window.location.href = `/produtosdaf/denominacoes`;
            return; // Sai da função
        }
        
        $.ajax({
            url: `/produtosdaf/denominacoes/deletar/${denominacaoId}/`,
            method: 'POST',
            headers: {
                'X-CSRFToken': $('meta[name="csrf-token"]').attr('content')  // Pega o token CSRF para autenticação
            },
            success: function(response) {
                // Redireciona para a lista de denominações após a deleção bem-sucedida
                //alert(response.message);
                window.location.href = `/produtosdaf/denominacoes`;
            },
            error: function(error) {
                // Aqui você pode adicionar qualquer lógica que deseja executar se houver um erro ao tentar deletar a denominação.
                alert('Ocorreu um erro ao tentar deletar a denominação. Por favor, tente novamente.');
            }
        });
    });

        //Mudar de página com delegação de eventos
    denominacaoFetchAndRenderTableData();
    $('#tabdenominacao  tbody').on('click', 'tr', function() {
        console.log('denominacaoFetchAndRenderTableData')
        const denominacaoId = $(this).attr('data-id').toString();
        window.location.href = `/produtosdaf/denominacoes/ficha/${denominacaoId}/`;
    });


    //Limpar Filtros
    $('.limpar-filtro').on('click', function() {
        console.log('limpar filtros')
        $('#tipo_produto').val('');
        $('#denominacao').val('');
        $('#basico').prop('checked', false);
        $('#especializado').prop('checked', false);
        $('#estrategico').prop('checked', false);
        $('#farmacia_popular').prop('checked', false);
        $('#hospitalar').prop('checked', false);
        denominacaoFetchAndRenderTableData();
    });

    //Filtrar
    $('#tipo_produto, #denominacao').change(function() {
        console.log('filtrar: tipo_produto, denominacao')
        denominacaoFetchAndRenderTableData();
    });

    //Fitlrar unidades
    $('#basico, #especializado, #estrategico, #farmacia_popular, #hospitalar').change(function() {
        console.log('filtrar: unidades')
        denominacaoFetchAndRenderTableData();
    });

    let denominacaoCurrentPage = 1;

    //Próxima página
    $('#denominacaoNextPage').on('click', function() {
        denominacaoFetchAndRenderTableData(denominacaoCurrentPage + 1);
    });

    //Página anterior
    $('#denominacaoPreviousPage').on('click', function() {
        denominacaoFetchAndRenderTableData(denominacaoCurrentPage - 1);
    });

   
    //Renderizar tabela
    function denominacaoFetchAndRenderTableData(page = 1) {
        var selectedTipo = $('#tipo_produto').val();
        var denominacao = $('#denominacao').val();
        
        var dataToSend = {
            'tipo_produto': selectedTipo,
            'denominacao': denominacao,
        };
        
        if ($('#basico').prop('checked')) {
            dataToSend.basico = true;
        }
        if ($('#especializado').prop('checked')) {
            dataToSend.especializado = true;
        }
        if ($('#estrategico').prop('checked')) {
            dataToSend.estrategico = true;
        }
        if ($('#farmacia_popular').prop('checked')) {
            dataToSend.farmacia_popular = true;
        }
        if ($('#hospitalar').prop('checked')) {
            dataToSend.hospitalar = true;
        }

        $.ajax({
            url: "/produtosdaf/denominacoes/filtro/",
            data: { ...dataToSend, page: page },
            dataType: 'json',
            success: function(data) {
                updateTable(data.data);
                $('#numeroDenominacoes').text(data.numero_denominacoes.toLocaleString('pt-BR').replace(/,/g, '.'));
                $('#denominacaoCurrentPage').text(data.current_page);
                $('#denominacaoNextPage').prop('disabled', !data.has_next);
                $('#denominacaoPreviousPage').prop('disabled', !data.has_previous);
                denominacaoCurrentPage = data.current_page;
            }
        });
    }




    //Atualizar tabela
    function updateTable(denominacoes) {
        console.log('updateTable')
        var $tableBody = $('.table tbody');
        $tableBody.empty(); // Limpar as linhas existentes

        denominacoes.forEach(denominacao => {
            var row = `
                <tr data-id="${denominacao.id}">
                    <td>${denominacao.id}</td>
                    <td>${denominacao.tipo_produto}</td>
                    <td>${denominacao.denominacao}</td>
                    <td style="text-align: center;">${denominacao.unidade_basico ? '<span class="bold-blue">Sim</span>' : 'Não'}</td>
                    <td style="text-align: center;">${denominacao.unidade_especializado ? '<span class="bold-blue">Sim</span>' : 'Não'}</td>
                    <td style="text-align: center;">${denominacao.unidade_estrategico ? '<span class="bold-blue">Sim</span>' : 'Não'}</td>
                    <td style="text-align: center;">${denominacao.unidade_farm_popular ? '<span class="bold-blue">Sim</span>' : 'Não'}</td>
                    <td style="text-align: center;">${denominacao.hospitalar ? '<span class="bold-blue">Sim</span>' : 'Não'}</td>
                </tr>
            `;
            $tableBody.append(row);
        });
    }

});







//Exportar dados
document.querySelector('#exportarBtn').addEventListener('click', function() {
    // Coleta valores dos campos
    const tipo_produto = document.querySelector('#tipo_produto').value;
    const denominacao = document.querySelector('#denominacao').value;
    const basico = document.querySelector('#basico').checked;
    const especializado = document.querySelector('#especializado').checked;
    const estrategico = document.querySelector('#estrategico').checked;
    const farmacia_popular = document.querySelector('#farmacia_popular').checked;
    const hospitalar = document.querySelector('#hospitalar').checked;
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    // Define dados a serem enviados
    const data = {
        tipo_produto: tipo_produto,
        denominacao: denominacao,
        basico: basico,
        especializado: especializado,
        estrategico: estrategico,
        farmacia_popular: farmacia_popular,
        hospitalar: hospitalar
    };

    // Envia solicitação AJAX para o servidor
    fetch('denominacoes/exportar/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify(data)
    })
    .then(response => response.blob()) // Trata a resposta como um Blob
    .then(blob => {
        // Inicia o download do arquivo
        const a = document.createElement('a');
        const url = URL.createObjectURL(blob);
        a.href = url;
        a.download = 'denominacoes_genericas.xlsx';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    });
});


//Salvar dados
document.getElementById('btnSaveDenominacao').addEventListener('click', function(e) {
    e.preventDefault();  // Evita o envio padrão do formulário

    let formData = new FormData(document.getElementById('denominacaoForm'));
    console.log('SALVAR DENOMINAÇÃO')

    fetch("{% if form.instance.id %}{% url 'denominacoes_ficha' form.instance.id %}{% else %}{% url 'nova_denominacao' %}{% endif %}", {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest'  // Indica que é uma requisição AJAX
        }
    })
    .then(response => response.json())
    .then(data => {
        // Atualize os campos do log com os dados retornados
        const denominacaoId = data.id;
        document.getElementById('log_data_registro').value = data.registro_data;
        document.getElementById('log_responsavel_registro').value = data.usuario_registro;
        document.getElementById('lot_ult_atualizacao').value = data.ult_atual_data;
        document.getElementById('log_responsavel_atualizacao').value = data.usuario_atualizacao;
        document.getElementById('log_edicoes').value = data.log_n_edicoes;
        
        window.location.href = `/produtosdaf/denominacoes/ficha/${denominacaoId}/`;
    });
    

});


