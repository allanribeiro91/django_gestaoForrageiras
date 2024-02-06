document.addEventListener('DOMContentLoaded', function() {
    //componentes
    const unidadeDaf = document.getElementById('inserir_ct_unidade_daf');
    const modalidadeAquisicao = document.getElementById('inserir_ct_modalidade_aquisicao');
    const arpSelect = document.getElementById('inserir_ct_arp');
    const denominacaoGenerica = document.getElementById('inserir_ct_denominacao');
    const fornecedor = document.getElementById('inserir_ct_fornecedor');
    const btnInserirCT = document.getElementById('inserirNovoContrato')


    btnInserirCT.addEventListener('click', function() {
        //Verificar preenchimento dos campos
        let preenchimento_incorreto = verificar_preenchimento_campos()
        if (preenchimento_incorreto === false) {
            return;
        }

        //armazenar no localStorage
            //Unidade Daf
            var selectedText = unidadeDaf.options[unidadeDaf.selectedIndex].text;
            localStorage.setItem('memoria_unidadeDaf_value', (unidadeDaf.value))
            localStorage.setItem('memoria_unidadeDaf_text', selectedText)

            //Modalidade de Aquisição
            selectedText = modalidadeAquisicao.options[modalidadeAquisicao.selectedIndex].text;
            localStorage.setItem('memoria_modalidadeAquisicao_value', (modalidadeAquisicao.value))
            localStorage.setItem('memoria_modalidadeAquisicao_text', selectedText)

            //Numero da ARP
            if (arpSelect.value != '') {
                selectedText = arpSelect.options[arpSelect.selectedIndex].text;
                localStorage.setItem('memoria_numeroARP_value', (arpSelect.value))
                localStorage.setItem('memoria_numeroARP_text', selectedText)
            } else {
                localStorage.setItem('memoria_numeroARP_value', '')
                localStorage.setItem('memoria_numeroARP_text', '')
            }
            

            //Denominação Genérica
            selectedText = denominacaoGenerica.options[denominacaoGenerica.selectedIndex].text;
            localStorage.setItem('memoria_denominacao_value', (denominacaoGenerica.value))
            localStorage.setItem('memoria_denominacao_text', selectedText)

            //Fornecedor
            selectedText = fornecedor.options[fornecedor.selectedIndex].text;
            localStorage.setItem('memoria_fornecedor_value', (fornecedor.value))
            localStorage.setItem('memoria_fornecedor_text', selectedText)

        //ir para a página
        window.location.href = '/contratos/contrato/ficha/novo/'

    })

    unidadeDaf.addEventListener('change', function() {
        if (unidadeDaf.value == '' || unidadeDaf.value == 'nao_informado'){
            ativarModalidadeAquisicao('desabilitar');
            ativarArpSelect('desabilitar');
            denominacaoGenerica.value = '';
            fornecedor.value = '';
        } else {
            ativarModalidadeAquisicao('habilitar');
            if (modalidadeAquisicao.value == 'pregao_comarp'){
                buscarArps(unidadeDaf.value);
            } else {
                if (modalidadeAquisicao.value != 'nao_informado') {
                    buscarDenominacoes(unidadeDaf.value);
                }
            }
        }
    });

    modalidadeAquisicao.addEventListener('change', function() {
        if (modalidadeAquisicao.value == 'pregao_comarp'){
            buscarArps(unidadeDaf.value);
            
            ativarArpSelect('habilitar')
            ativarDenominacaoGenerica('desabilitar');
            ativarFornecedor('desabilitar');
            buscarFornecedores();
        } else {
            ativarArpSelect('desabilitar')
            if (modalidadeAquisicao.value == 'nao_informado') {
                ativarDenominacaoGenerica('desabilitar');
                ativarFornecedor('desabilitar');
            } else {

                ativarDenominacaoGenerica('habilitar');
                if (denominacaoGenerica.value == '') {                    
                    buscarDenominacoes(unidadeDaf.value);
                }
                
                ativarFornecedor('habilitar');
                if (fornecedor.value == '') {
                    buscarFornecedores();
                }
            }
        }
    });

    arpSelect.addEventListener('change', function() {
        const selectedOption = arpSelect.options[arpSelect.selectedIndex];
        denominacaoGenerica.value = selectedOption.getAttribute('data-denominacao');
        fornecedor.value = selectedOption.getAttribute('data-fornecedor');
    });



    function ativarModalidadeAquisicao(valor) {
        if (valor == 'habilitar') {
            modalidadeAquisicao.removeAttribute('disabled');
        } else {
            modalidadeAquisicao.setAttribute('disabled', 'disabled');
            modalidadeAquisicao.value = 'nao_informado';
        }
    }

    function ativarArpSelect(valor) {
        if (valor == 'habilitar') {
            arpSelect.removeAttribute('disabled');
        } else {
            arpSelect.setAttribute('disabled', 'disabled');
            arpSelect.value = 'nao_informado';
        }
    }

    function ativarDenominacaoGenerica(valor) {
        if (valor == 'habilitar') {
            denominacaoGenerica.removeAttribute('disabled');
        } else {
            denominacaoGenerica.setAttribute('disabled', 'disabled');
            denominacaoGenerica.value = '';
        }
    }

    function ativarFornecedor(valor) {
        if (valor == 'habilitar') {
            fornecedor.removeAttribute('disabled');
        } else {
            fornecedor.setAttribute('disabled', 'disabled');
            fornecedor.value = '';
        }
    }

    function buscarArps(unidadeDaf) {
        const url = `/contratos/buscararps/${unidadeDaf}/`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                arpSelect.innerHTML = '<option value=""></option>';

                data.arps.forEach(arp => {
                    const option = document.createElement('option');
                    option.value = arp.id;
                    option.textContent = arp.numero_arp;
                    option.setAttribute('data-denominacao', arp.denominacao);
                    option.setAttribute('data-fornecedor', arp.fornecedor);
                    arpSelect.appendChild(option);
                });
            })
            .catch(error => console.error('Erro ao buscar ARPs:', error));
    }

    function buscarDenominacoes(unidadeDaf) {
        const url = `/produtosdaf/buscardenominacoes/${unidadeDaf}/`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                denominacaoGenerica.innerHTML = '<option value=""></option>';

                data.denominacoes_list.forEach(denominacao => {
                    const option = document.createElement('option');
                    option.value = denominacao.id;
                    option.textContent = denominacao.denominacao + " (ID: " + denominacao.id + ")";
                    denominacaoGenerica.appendChild(option);
                });
            })
            .catch(error => console.error('Erro ao buscar Denominações:', error));
    }

    function buscarFornecedores() {
        const url = `/fornecedores/buscarfornecedores/`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                fornecedor.innerHTML = '<option value=""></option>';

                data.fornecedores_list.forEach(fornecedor_nome => {
                    const option = document.createElement('option');
                    option.value = fornecedor_nome.id;
                    option.textContent = fornecedor_nome.nome_fantasia + " (" + fornecedor_nome.cnpj + ")";
                    fornecedor.appendChild(option);
                });
            })
            .catch(error => console.error('Erro ao buscar Fornecedores:', error));
    }

    function verificar_preenchimento_campos() {
        const campos = [
            { id: 'inserir_ct_unidade_daf', mensagem: 'Informe a Unidade DAF!' },
            { id: 'inserir_ct_modalidade_aquisicao', mensagem: 'Informe a Modalidade de Aquisição!' },
            { id: 'inserir_ct_denominacao', mensagem: 'Informe a Denominação Genérica!' },
            { id: 'inserir_ct_fornecedor', mensagem: 'Informe o Fornecedor!' },
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
});




