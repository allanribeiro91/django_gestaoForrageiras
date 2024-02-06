document.addEventListener('DOMContentLoaded', function() {
    //Verificar se há mensagem de salvamento com sucesso
    if (localStorage.getItem('showSuccessMessage') === 'true') {
        sweetAlert('Contrato salvo com sucesso!', 'success', 'top-end');
        localStorage.removeItem('showSuccessMessage');
        atualizarDatas();
    }
    
    
    //componentes
    const aba_dados_gerais = document.getElementById('projeto_ficha_dados_gerais');
    const aba_execucao_financeira = document.getElementById('projeto_ficha_execucao_financeira')
    const id_projeto = document.getElementById('id_projeto')

    aba_dados_gerais.addEventListener('click', function() {
        var url = ''
        if (id_projeto.value == '') {
            url = '/projetos/ficha/dados-gerais/novo/'
        } else {
            url = '/projetos/ficha/dados-gerais/' + id_projeto.value + '/'
        }
        window.location.href = url;
    })

    aba_execucao_financeira.addEventListener('click', function() {
        var url = ''
        if (id_projeto.value == '') {
            url = '/projetos/ficha/execucao-financeira/novo/'
        } else {

            url = '/projetos/ficha/execucao-financeira/' + id_projeto.value + '/'
        }
        window.location.href = url;
    })


    //Campos formulário - Dados Gerais
    const botao_salvar_projeto = document.getElementById('btnSalvarProjeto')

    botao_salvar_projeto.addEventListener('click', function(event){
        event.preventDefault();
        salvarProjeto();
    })

    function salvarProjeto() {

        //Verificar preenchimento dos campos
        let preenchimento_incorreto = verificar_campos_projeto()
        if (preenchimento_incorreto === false) {
            return;
        }
        
        //Enviar para o backend
            //definir o caminho
            if (id_projeto.value == '') {
                postURL = '/projetos/ficha/dados-gerais/novo/'
            } else
            {
                postURL = `/projetos/ficha/dados-gerais/${id_projeto.value}/`
            }
    
            //pegar os dados
            let formData = new FormData(document.getElementById('projetoForm'));
    
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
                    sweetAlert('Projeto salvo com sucesso!', 'success', 'green')
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

    function verificar_campos_projeto() {
        const campos = [
            { id: 'id_status', mensagem: 'Informe o Status do Projeto!' },
            { id: 'id_nome_plano_trabalho', mensagem: 'Informe o nome do Plano de Trabalho!' },
            { id: 'id_regional', mensagem: 'Informe a Regional!' },
            { id: 'id_subprograma', mensagem: 'Informe o Subprograma!' },
            { id: 'id_geracao_projeto', mensagem: 'Informe a Geração do Projeto!' },
            { id: 'id_data_inicio', mensagem: 'Informe a Data de Início!' },
            { id: 'id_data_fim', mensagem: 'Informe a Data Fim!' },
            { id: 'id_projeto_sisateg', mensagem: 'Informe o ID do Projeto no SisATeG!' },
            { id: 'id_gestor_dateg', mensagem: 'Informe o Gestor da DATeG!' },
            { id: 'id_n_processo', mensagem: 'Informe o Número do Processo!' },
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


    //Modal Atividade produtiva
    const modal_atividade_produtiva = new bootstrap.Modal(document.getElementById('projetoAtividadeModal'))
    const botao_inserir_atividade = this.getElementById('btnInserirAtividade')

    botao_inserir_atividade.addEventListener('click', inserir_atividade_produtiva)

    function inserir_atividade_produtiva() {
        modal_atividade_produtiva.show()
    }


    //Formatar campos
    formatarQuantidade('id_n_propriedades')
    formatarQuantidade('id_n_cadernos')
    formatarQuantidade('id_n_tecnicos')
    formatarQuantidade('id_n_supervisores')
    formatarQuantidade('id_n_supervisores_tecnicos_ead')

    function formatarQuantidade(campoId) {
        var campo = document.getElementById(campoId);
        
        campo.addEventListener('input', function (e) {
            // Impede caracteres não-numéricos de serem digitados
            var valor = this.value.replace(/[^0-9]/g, '');
    
            // Converte valor para número
            var numero = parseInt(valor, 10);
    
            // Se o valor for NaN, define como 0
            if (isNaN(numero)) {
                numero = 0;
            }
    
            // Adiciona pontos como separadores de milhar
            var valorFormatado = numero.toLocaleString('pt-BR');
    
            // Atualiza o valor do campo
            this.value = valorFormatado;
        });
    }


    //ID Atividade - Modal
    const id_atividade_id = this.getElementById('id_atividade_id')
    const atividade = this.getElementById('id_atividade')

    atividade.addEventListener('change', function(){
        id_atividade_id.value = atividade.value
    })

});