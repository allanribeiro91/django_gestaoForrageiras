document.addEventListener("DOMContentLoaded", function() {
    const unidadeDaf = this.getElementById('ct_unidade_daf')
    const unidadeDaf_display = this.getElementById('ct_unidade_daf_display') 
    const modalidadeAquisicao = this.getElementById('ct_modalidade_aquisicao')
    const modalidadeAquisicao_display = this.getElementById('ct_modalidade_aquisicao_display')
    const arp = this.getElementById('ct_arp')
    const arp_display = this.getElementById('ct_arp_display')
    const denominacaoGenerica = this.getElementById('ct_denominacao')
    const denominacaoGenerica_display = this.getElementById('ct_denominacao_display')
    const fornecedor = this.getElementById('ct_fornecedor')
    const fornecedor_display = this.getElementById('ct_fornecedor_display')
    const processoSei = this.getElementById('ct_processo_sei')
    const lei_licitacao = this.getElementById('ct_lei_licitacao')
    const lei_licitacao_valor = this.getElementById('ct_lei_licitacao_valor')
    const data_publicacao = this.getElementById('data_publicacao')
    const data_vigencia = this.getElementById('data_vigencia')
    const prazo_vigencia = this.getElementById('prazo_vigencia')
    const botao_salvar_contrato = this.getElementById('btnSalvarContrato')
    const contrato_id = this.getElementById('id_contrato').value
    const botao_deletar_contrato = this.getElementById('btnDeletarContrato')
    const botao_nova_parcela = this.getElementById('btnNovaParcela')
    const modal_inserir_parcela = new bootstrap.Modal(document.getElementById('contratoParcelaModal'))
    const modal_definir_item_arp = new bootstrap.Modal(document.getElementById('contratoParcelaARP'))

    //Carregar dados
    carregarDados();

    //Verificar se há mensagem de salvamento com sucesso
    if (localStorage.getItem('showSuccessMessage') === 'true') {
        sweetAlert('Contrato salvo com sucesso!', 'success', 'top-end');
        localStorage.removeItem('showSuccessMessage');
        atualizarDatas();
    }
    
    //Formatação dos dados
    $('#ct_processo_sei').mask('00000.000000/0000-00');
    $('#ct_documento_sei').mask('000000');

    //Atualizar data de vigência e prazo
    data_publicacao.addEventListener('change', atualizarDatas);

    //Lei de Licitação
    lei_licitacao.addEventListener('change', leiLicitacao)

    //Salvar Contrato 
    botao_salvar_contrato.addEventListener('click', function(event){
        event.preventDefault();
        salvarContrato();
    })

    //Deletar Contrato
    botao_deletar_contrato.addEventListener('click', deletarContrato)
    
    //Inserir Parcela
    botao_nova_parcela.addEventListener('click', definicao_modal_abrir)

    function deletarContrato(){
        const url_apos_delete = "/contratos/contratos/";

        //Trata-se de um novo registro que ainda não foi salvo
        if (!contrato_id) { 
            window.location.href = url_apos_delete;
            return; // Sai da função
        }
        
        //parâmetros para deletar
        const mensagem = "Deletar Contrato."
        const url_delete = "/contratos/contrato/deletar/" + contrato_id + "/"
        const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

        //chamar sweetAlert
        sweetAlertDelete(mensagem, url_delete, csrfToken, url_apos_delete)
    }  

    //Funções
    function carregarDados() {
        var unidade_daf_value = localStorage.getItem('memoria_unidadeDaf_value');
        var unidade_daf_text = localStorage.getItem('memoria_unidadeDaf_text');
        if (unidade_daf_value) {
            unidadeDaf.value = unidade_daf_value;
            unidadeDaf_display.value = unidade_daf_text;
        }

        var modalidadeAquisicao_value = localStorage.getItem('memoria_modalidadeAquisicao_value');
        var modalidadeAquisicao_text = localStorage.getItem('memoria_modalidadeAquisicao_text');
        if (modalidadeAquisicao_value) {
            modalidadeAquisicao.value = modalidadeAquisicao_value;
            modalidadeAquisicao_display.value = modalidadeAquisicao_text;
        }

        var numeroARP_value = localStorage.getItem('memoria_numeroARP_value');
        var numeroARP_text = localStorage.getItem('memoria_numeroARP_text');
        if (numeroARP_value) {
            arp.value = numeroARP_value;
            arp_display.value = numeroARP_text;
            buscarDadosSeiArp(numeroARP_value);
        } else {
            if (arp.value == '')
            arp_display.value = "Não se aplica"
        }

        var denominacao_value = localStorage.getItem('memoria_denominacao_value');
        var denominacao_text = localStorage.getItem('memoria_denominacao_text');
        if (denominacao_value) {
            denominacaoGenerica.value = denominacao_value;
            denominacaoGenerica_display.value = denominacao_text;
        }

        var fornecedor_value = localStorage.getItem('memoria_fornecedor_value');
        var fornecedor_text = localStorage.getItem('memoria_fornecedor_text');
        if (fornecedor_value) {
            fornecedor.value = fornecedor_value;
            fornecedor_display.value = fornecedor_text;
        }
        
        localStorage.clear();
    }
    
    function buscarDadosSeiArp(id_arp) {
        const url = `/contratos/arp/buscardadossei/${id_arp}/`;
        
        fetch(url)
            .then(response => response.json())
            .then(data => {
                const arpInfo = data.arp[0]
                processoSei.value = arpInfo.numero_processo_sei;
                lei_licitacao.value = arpInfo.lei_licitacao;
                lei_licitacao_valor.value = arpInfo.lei_licitacao;
                processoSei.setAttribute('readonly', true);
                lei_licitacao.setAttribute('disabled', 'disabled');                
            })
            .catch(error => console.error('Erro ao buscar ARP:', error));
    }

    function leiLicitacao() {
        lei_licitacao_valor.value = lei_licitacao.value;
    }

    function atualizarDatas() {
        if (data_publicacao.value) {
            // Calcula a data de vigência (data_publicacao + 365 dias)
            let dataPublicacao = new Date(data_publicacao.value);
            let dataVigencia = new Date(dataPublicacao);
            dataVigencia.setDate(dataVigencia.getDate() + 365);

            // Formata a data de vigência para o formato apropriado (YYYY-MM-DD)
            let dataVigenciaFormatada = dataVigencia.toISOString().split('T')[0];
            data_vigencia.value = dataVigenciaFormatada;

            // Calcula o prazo de vigência (data_vigencia - data_atual)
            let dataAtual = new Date();
            let prazoVigencia = Math.round((dataVigencia - dataAtual) / (1000 * 60 * 60 * 24)) + 1;
            prazo_vigencia.value = prazoVigencia;
        } else {
            // Limpa os campos se a data de publicação estiver vazia
            data_vigencia.value = '';
            prazo_vigencia.value = '';
        }
    }

    function salvarContrato() {

        //Verificar preenchimento dos campos
        let preenchimento_incorreto = verificar_campos_contrato()
        if (preenchimento_incorreto === false) {
            return;
        }
        
        //Enviar para o servidor
            //definir o caminho
            if (contrato_id == '') {
                postURL = '/contratos/contrato/ficha/novo/'
            } else
            {
                postURL = `/contratos/contrato/ficha/${contrato_id}/`
            }
    
            //pegar os dados
            let formData = new FormData(document.getElementById('contratoForm'));
    
            //enviar 
            fetch(postURL, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
        
        //Retorno do Servidor
        .then(response => {
            // Primeiro verifique se a resposta é ok
            if (!response.ok) {
                sweetAlert('Dados não foram salvos.', 'error', 'red');
                throw new Error('Server response was not ok: ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            if (data.retorno === "Salvo") {
                
                if (data.novo === false) {
                    //logs       
                    document.getElementById('lot_ult_atualizacao').value = data.log_atualizacao_data
                    document.getElementById('log_responsavel_atualizacao').value = data.log_atualizacao_usuario
                    document.getElementById('log_edicoes').value = data.log_edicoes
    
                    //alert
                    sweetAlert('Contrato salvo com sucesso!', 'success', 'green')
                } else {
                    localStorage.setItem('showSuccessMessage', 'true');
                    window.location.href = data.redirect_url;
                }
            }
    
            if (data.retorno === "Não houve mudanças") {
                //alert
                sweetAlert('Dados não foram salvos.<br>Não houve mudanças.', 'warning', 'orange')
            }
    
            if (data.retorno === "Erro ao salvar") {
                //alert
                sweetAlert('Dados não foram salvos.', 'error', 'red')
            }
        })
        .catch(error => {
            console.error('Fetch operation error:', error);
        });
            
    }

    function verificar_campos_contrato() {
        const campos = [
            { id: 'ct_lei_licitacao_valor', mensagem: 'Informe a Lei de Licitação!' },
            { id: 'ct_processo_sei', mensagem: 'Informe o Processo SEI!' },
            { id: 'ct_documento_sei', mensagem: 'Informe o Documento SEI!' },
            { id: 'ct_numero_contrato', mensagem: 'Informe o Número do Contrato!' },
            { id: 'ct_status', mensagem: 'Informe o Status!' },
            { id: 'data_publicacao', mensagem: 'Informe a Data da Publicação!' },
        ];
    
        let mensagensErro = campos.reduce((mensagens, campo) => {
            const elemento = document.getElementById(campo.id);
            if (!elemento || elemento.value === '') {
                mensagens.push(campo.mensagem);
            }
            return mensagens;
        }, []);
    
        if (mensagensErro.length > 0) {
            const campos = mensagensErro.join('<br>')
            sweetAlertPreenchimento(campos)
            return false;
        }
    
        return true;
    }

    function definicao_modal_abrir() {
        if (arp_display.value == "Não se aplica") {
            modal_inserir_parcela.show();
        } else {
            
            modal_definir_item_arp.show();
            buscarDadosItensARP(arp.value);
        }

    }

    function buscarDadosItensARP(id_arp) {
        const url = `/contratos/buscararpsitens/${id_arp}/`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                carregarTabelaItensARP(data.arps_itens)            
            })
            .catch(error => console.error('Erro ao buscar ARP:', error));
    }

    function carregarTabelaItensARP(itensARP) {
        var tabelaItensArp = $('.itensArp');
        tabelaItensArp.empty();
        itensARP.forEach(item => {
            var row = `
                <tr data-id-item-arp="${ item.id }">
                    <td class="col-itemarp-id">${ item.numero_item }</td>
                    <td class="col-itemarp-tipocota" style="text-transform: capitalize;">${ item.tipo_cota }</td>
                    <td class="col-itemarp-produto">${ item.produto }</td>
                    <td class="col-itemarp-qtd">${ item.qtd_registrada.toLocaleString('pt-BR') }</td>
                    <td class="col-itemarp-qtd">0</td>
                    <td class="col-itemarp-qtd">${ item.qtd_saldo.toLocaleString('pt-BR') }</td>
                </tr>
            `;
            tabelaItensArp.append(row);
        });
    }

});
