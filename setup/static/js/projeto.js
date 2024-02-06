document.addEventListener('DOMContentLoaded', function() {
    //Abrir a ficha do Projeto
    $('#tabProjetos tbody').on('click', 'tr', function() {
        const id_projeto = $(this).attr('data-id').toString();
        window.location.href = `/projetos/ficha/dados-gerais/${id_projeto}/`;
    });  


    //Filtro
    const filtro_regional = this.getElementById('filtro_regional')
    const filtro_status = this.getElementById('filtro_status')
    const filtro_subprograma = this.getElementById('filtro_subprograma')
    const filtro_data_inicio = this.getElementById('filtro_data_inicio')
    const filtro_data_fim = this.getElementById('filtro_data_fim')
    const filtro_nome_plano_trabalho = this.getElementById('filtro_nome_plano_trabalho')
    const botao_filtrar = this.getElementById('filtro_limpar')

        //limpar filtros
        botao_filtrar.addEventListener('click', limmparFiltros)
        function limmparFiltros(){
            filtro_regional.value = ''
            filtro_status.value = ''
            filtro_subprograma.value = ''
            filtro_data_inicio.value = ''
            filtro_data_fim.value = ''
            filtro_nome_plano_trabalho.value = ''

            buscarAtualizarProjetos();
        }

        //filtrar
        $(filtro_nome_plano_trabalho).keyup(function() {
            buscarAtualizarProjetos();
        });

        $('#filtro_regional, #filtro_status, #filtro_subprograma, #filtro_data_inicio, #filtro_data_fim').change(function() {
            buscarAtualizarProjetos();
        });
        

        //buscar dados
        function buscarAtualizarProjetos(page = 1) {
            var regional = filtro_regional.value;
            var status = filtro_status.value;
            var subprograma = filtro_subprograma.value;
            var data_inicio = filtro_data_inicio.value;
            var data_fim = filtro_data_fim.value;
            var nome_plano_trabalho = filtro_nome_plano_trabalho.value;

            var dataToSend = {
                'regional': regional,
                'status': status,
                'subprograma': subprograma,
                'data_inicio': data_inicio,
                'data_fim': data_fim,
                'nome_plano_trabalho': nome_plano_trabalho,
            };

            $.ajax({
                url: "/projetos/filtro/",
                data: { ...dataToSend, page: page },
                dataType: 'json',
                success: function(data) {
                    recarregarTabela(data.data);
                    $('#numeroProjetos').text(data.total_projetos.toLocaleString('pt-BR').replace(/,/g, '.'));
                    $('#currentPage').text(data.current_page);
                    $('#nextPage').prop('disabled', !data.has_next);
                    $('#previousPage').prop('disabled', !data.has_previous);
                    currentPage = data.current_page;
                }
            });
        }
        //recarregar tabela
        function recarregarTabela(projetos) {
            var $tableBody = $('.table tbody');
            $tableBody.empty(); // Limpar as linhas existentes
        
            projetos.forEach(projeto => {
                var row = `
                    <tr data-id="${ projeto.id }">
                        <td class="col-id">${ projeto.id_projeto_sisateg }</td>
                        <td class="col-id">${ projeto.regional }</td>
                        <td class="col-status">${ projeto.status }</td>
                        <td class="col-subprograma">${ projeto.subprograma }</td>
                        <td class="col-subprograma">${ projeto.nome_plano_trabalho }</td>
                        <td class="col-processo">${ projeto.n_processo }</td>
                        <td class="col-data">${ projeto.data_inicio }</td>
                        <td class="col-data">${ projeto.data_fim }</td>
                        <td class="col-responsavel">${ projeto.gestor_dateg }</td>
                    </tr>
                `;
                $tableBody.append(row);
            });
        }
});




    