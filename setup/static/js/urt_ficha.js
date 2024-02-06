document.addEventListener("DOMContentLoaded", function() {

    //Verificar se há mensagem de salvamento com sucesso
    if (localStorage.getItem('urtSalva') === 'true') {
        sweetAlert('Dados da URT salvos com sucesso!', 'success', 'top-end');
        localStorage.removeItem('urtSalva');
    }
    if (localStorage.getItem('especieVegetalSalva') === 'true') {
        sweetAlert('Espécie Vegetal salva com sucesso!', 'success', 'top-end');
        let idVegetal = localStorage.getItem('especie_vegetal_id');
        localStorage.removeItem('especieVegetalSalva');
        if (idVegetal) {
            localStorage.removeItem('especie_vegetal_id');
            openModalEspecieVegetal(idVegetal)
        }
    }
    if (localStorage.getItem('tecnicoSalvo') === 'true') {
        sweetAlert('Técnico da URT salvo com sucesso!', 'success', 'top-end');
        let idTecnico = localStorage.getItem('tecnico_id');
        localStorage.removeItem('tecnicoSalvo');
        if (idTecnico) {
            localStorage.removeItem('tecnico_id');
            openModalTecnicoURT(idTecnico)
        }
    }


    


    //ID da URT
    const id_urt = document.getElementById('urt_id').value
    
    //INSERIR NOVO VEGETAL OU ANIMAL
    const botao_novo_vegetal = document.getElementById('btnNovoVegetal')
    const botao_novo_animal = document.getElementById('btnNovoAnimal')
    const modal_especie_vegetal = new bootstrap.Modal(document.getElementById('especieVegetalModal'))
    const modal_especie_animal = new bootstrap.Modal(document.getElementById('especieAnimalModal'))

    botao_novo_vegetal.addEventListener('click', function(){
        limparDadosEspecieVegetal();
        
        const id_urt_vegetal = document.getElementById('id_urt_vegetal')
        id_urt_vegetal.value = id_urt;

        modal_especie_vegetal.show();
    })

    botao_novo_animal.addEventListener('click', function() {
        limparDadosEspecieAnimal();

        const id_urt_animal = document.getElementById('id_urt_animal')
        id_urt_animal.value = id_urt;

        modal_especie_animal.show();
    })

    function limparDadosEspecieVegetal(){
        //logs
        document.getElementById('vegetal_id').value = ''
        document.getElementById('vegetal_log_data_registro').value = ''
        document.getElementById('vegetal_log_responsavel_registro').value = ''
        document.getElementById('vegetal_log_ult_atualizacao').value = ''
        document.getElementById('vegetal_log_responsavel_atualizacao').value = ''
        document.getElementById('vegetal_log_edicoes').value = ''
        
        //dados da espécie vegetal
        document.getElementById('id_vegetal_especie_vegetal').value = ''
        document.getElementById('id_vegetal_variedades').value = ''
        document.getElementById('id_vegetal_area_utilizada').value = ''
        document.getElementById('id_vegetal_producao_silagem').value = ''
        document.getElementById('id_vegetal_observacoes_gerais').value = ''

        //Campos ocultos
        document.getElementById('id_urt_vegetal').value = ''

    }





    //FORMATO DE TELEFONE E CELULAR
    const celular_proprietario = document.getElementById('id_proprietario_celular')
    celular_proprietario.addEventListener('input', function(){
        formatoCelular(celular_proprietario)
    })
    const elementos = [
        'id_proprietario_telefone',
        'id_federacao_telefone',
        'id_senar_telefone',
        'id_supervisor_telefone'
    ];
    elementos.forEach(elementoId => {
        const elemento = document.getElementById(elementoId);
        elemento.addEventListener('input', function() {
            formatoTelefone(elemento);
        });
    });

    const area_experimento = document.getElementById('id_area_experimento')
    numeroInteiroMilhar(area_experimento)

    const precipitacao_anual = document.getElementById('id_precipitacao_anual')
    numeroInteiroMilhar(precipitacao_anual)

    //PERIODO DE CHUVA E SECA
    const chuva_inicio = document.getElementById('id_periodo_chuva_inicio')
    const chuva_fim = document.getElementById('id_periodo_chuva_fim')
    const seca_inicio = document.getElementById('id_periodo_seca_inicio')
    const seca_fim = document.getElementById('id_periodo_seca_fim')

    chuva_inicio.addEventListener('change', periodo_chuva_seca)
    chuva_fim.addEventListener('change', periodo_chuva_seca)

    function periodo_chuva_seca(){
        inicio_chuva = parseInt(chuva_inicio.value)
        fim_chuva = parseInt(chuva_fim.value)

        if (inicio_chuva){
            
            mes = inicio_chuva - 1
            if (mes < 1) {
                mes = 12
            }
            
            seca_fim.value = mes
        }
        
        if (fim_chuva){

            mes = fim_chuva + 1
            if (mes > 12){
                mes = 1
            }
            seca_inicio.value = mes
        }
                
    }

    //SALVAR URT
    const botao_salvar_urt = document.getElementById('btnSalvarURT')
    botao_salvar_urt.addEventListener('click', function(event){
        event.preventDefault();
        salvarURT();
    })
    
    function salvarURT(){
        const urt_id = document.getElementById('urt_id').value
        
        //Enviar para o servidor
            //definir o caminho
            if (urt_id == '') {
                //postURL = '/contratos/contrato/parcela/salvar/novo/'
            } else
            {
                postURL = `/urts/ficha/salvar/${urt_id}/`
            }

            //pegar os dados
            let formData = new FormData(document.getElementById('formURT'));
    
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
                localStorage.setItem('urtSalva', 'true');
                window.location.reload();
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

    //ESPÉCIE VEGETAL
        //SALVAR ESPÉCIE VEGETAL
        const botao_salvar_vegetal = document.getElementById('btnSalvarVegetal')
        botao_salvar_vegetal.addEventListener('click', function(event){
            event.preventDefault();
            salvarEspecieVegetal();
        })

        function salvarEspecieVegetal() {
            const id_especie_vegetal = document.getElementById('vegetal_id')

            //Verificar preenchimento dos campos
            let preenchimento_incorreto = verificar_campos_especie_vegetal()
            if (preenchimento_incorreto === false) {
                return;
            }
            
            //Enviar para o servidor
                //definir o caminho
                if (id_especie_vegetal.value == '') {
                    postURL = '/urts/ficha/especie-vegetal/salvar/novo/'
                } else
                {
                    postURL = `/urts/ficha/especie-vegetal/salvar/${id_especie_vegetal.value}/`
                }

                //pegar os dados
                let formData = new FormData(document.getElementById('especieVegetalForm'));
        
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
                        let especie_vegetal_id = data.especie_vegetal_id;
                        localStorage.setItem('especieVegetalSalva', 'true');
                        localStorage.setItem('especie_vegetal_id', especie_vegetal_id);
                        window.location.reload();
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

        function verificar_campos_especie_vegetal() {
            const campos = [
                { id: 'id_vegetal_especie_vegetal', mensagem: 'Informe a <b>Espécie Vegetal</b>!' },
                { id: 'id_vegetal_variedades', mensagem: 'Informe a(s) <b>Variedade(s)</b>!' },
                { id: 'id_vegetal_area_utilizada', mensagem: 'Informe a <b>Área Utilizada</b>!' },
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

        function openModalEspecieVegetal(id_vegetal) {
            fetch(`/urts/ficha/especie-vegetal/${id_vegetal}/dados`)

                .then(response => {
                    if (!response.ok) {
                        throw new Error('Erro ao buscar dados da Espécie Vegetal.');
                    }
                    return response.json();
                })
                .then(data => {
                    // Atualizar os campos do formulário no modal com os dados recebidos
                    //log
                    $('#vegetal_id').val(data.id);
                    $('#vegetal_log_data_registro').val(data.log_data_registro);
                    $('#vegetal_log_responsavel_registro').val(data.log_responsavel_registro);
                    $('#vegetal_log_ult_atualizacao').val(data.lot_ult_atualizacao);
                    $('#vegetal_log_responsavel_atualizacao').val(data.log_responsavel_atualizacao);
                    $('#vegetal_log_edicoes').val(data.log_edicoes);

                    //dados da parcela
                    $('#id_vegetal_especie_vegetal').val(data.especie_vegetal)
                    $('#id_vegetal_variedades').val(data.variedades)
                    $('#id_vegetal_area_utilizada').val(data.area_utilizada.toLocaleString('pt-BR'))
                    
                    if (data.producao_silagem === true) {
                        $('#id_vegetal_producao_silagem').val('true');
                    } else if (data.producao_silagem === false) {
                        $('#id_vegetal_producao_silagem').val('false');
                    } else {
                        $('#id_vegetal_producao_silagem').val('');
                    }
                    
                    
                    $('#id_vegetal_observacoes_gerais').val(data.observacoes)
                    
                    //Campos ocultos
                    $('#id_urt_vegetal').val(data.urt_id)

                    // Abrir o modal
                    modal_especie_vegetal.show();

                })
                .catch(error => {
                    console.log(error);
                });
        }

        //Abrir Modal Espécie Vegetal
        const tabela_especies_vegetais = document.getElementById('tabEspeciesVegetais');
        tabela_especies_vegetais.addEventListener('click', function(event) {
        const target = event.target;
        if (target.tagName === 'TD') {
            const row = target.closest('tr');
            const item = row.dataset.id;
            openModalEspecieVegetal(item);
        }
        });

        //DELETAR ESPÉCIE VEGETAL
        const botao_deletar_especie_vegetal = document.getElementById('btnDeletarVegetal')
        botao_deletar_especie_vegetal.addEventListener('click', function() {
            var id_especie_vegetal = document.getElementById('vegetal_id').value

            if (id_especie_vegetal == ''){
                modal_especie_vegetal.hide()
                limparDadosEspecieVegetal();
                return
            }

            //parâmetros para deletar
            const mensagem = "Deletar Espécie Vegetal."
            const url_delete = "/urts/ficha/especie-vegetal/deletar/" + id_especie_vegetal + "/"

            const url_apos_delete = window.location.href;
            const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

            //chamar sweetAlert
            sweetAlertDelete(mensagem, url_delete, csrfToken, url_apos_delete)
        })


    //FORMATAR VALOR DECIMAL DA ÁREA
    const vegetal_area_utilizada = document.getElementById('id_vegetal_area_utilizada')
    vegetal_area_utilizada.addEventListener('input', function(){
        vegetal_area_utilizada.value = formatarValorDecimal(vegetal_area_utilizada.value)
    })
    const animal_area_utilizada = document.getElementById('id_animal_area_utilizada')
    animal_area_utilizada.addEventListener('input', function(){
        animal_area_utilizada.value = formatarValorDecimal(animal_area_utilizada.value)
    })
    
    
    //ESPÉCIE ANIMAL
        //SALVAR ESPÉCIE ANIMAL
        const botao_salvar_animal = document.getElementById('btnSalvarAnimal')
        botao_salvar_animal.addEventListener('click', function(event){
            event.preventDefault();
            salvarEspecieAnimal();
        })

        function salvarEspecieAnimal() {
            const id_especie_animal = document.getElementById('animal_id')

            //Verificar preenchimento dos campos
            let preenchimento_incorreto = verificar_campos_especie_animal()
            if (preenchimento_incorreto === false) {
                return;
            }
            
            //Enviar para o servidor
                //definir o caminho
                if (id_especie_animal.value == '') {
                    postURL = '/urts/ficha/especie-animal/salvar/novo/'
                } else
                {
                    postURL = `/urts/ficha/especie-animal/salvar/${id_especie_animal.value}/`
                }

                //pegar os dados
                let formData = new FormData(document.getElementById('especieAnimalForm'));
        
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
                        let especie_animal_id = data.especie_animal_id;
                        localStorage.setItem('especieAnimalSalva', 'true');
                        localStorage.setItem('especie_animal_id', especie_animal_id);
                        window.location.reload();
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

        function verificar_campos_especie_animal() {
            const campos = [
                { id: 'id_animal_especie_animal', mensagem: 'Informe a <b>Espécie Animal</b>!' },
                { id: 'id_animal_racas', mensagem: 'Informe a(s) <b>Raça(s)</b>!' },
                { id: 'id_animal_area_utilizada', mensagem: 'Informe a <b>Área Utilizada</b>!' },
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

        function openModalEspecieAnimal(id_animal) {
            fetch(`/urts/ficha/especie-animal/${id_animal}/dados`)

                .then(response => {
                    if (!response.ok) {
                        throw new Error('Erro ao buscar dados da Espécie Animal.');
                    }
                    return response.json();
                })
                .then(data => {
                    // Atualizar os campos do formulário no modal com os dados recebidos
                    //log
                    $('#animal_id').val(data.id);
                    $('#animal_log_data_registro').val(data.log_data_registro);
                    $('#animal_log_responsavel_registro').val(data.log_responsavel_registro);
                    $('#animal_log_ult_atualizacao').val(data.lot_ult_atualizacao);
                    $('#animal_log_responsavel_atualizacao').val(data.log_responsavel_atualizacao);
                    $('#animal_log_edicoes').val(data.log_edicoes);

                    //dados da parcela
                    $('#id_animal_especie_animal').val(data.especie_animal)
                    $('#id_animal_racas').val(data.racas)
                    $('#id_animal_area_utilizada').val(data.area_utilizada.toLocaleString('pt-BR'))
                    $('#id_animal_observacoes_gerais').val(data.observacoes)
                    
                    //Campos ocultos
                    $('#id_urt_animal').val(data.urt_id)

                    // Abrir o modal
                    modal_especie_animal.show();

                })
                .catch(error => {
                    console.log(error);
                });
        }

        //Abrir Modal Espécie Animal
        const tabela_especies_animais = document.getElementById('tabEspeciesAnimais');
        tabela_especies_animais.addEventListener('click', function(event) {
        const target = event.target;
        if (target.tagName === 'TD') {
            const row = target.closest('tr');
            const item = row.dataset.id;
            openModalEspecieAnimal(item);
        }
        });

        //DELETAR ESPÉCIE ANIMAL
        const botao_deletar_especie_animal = document.getElementById('btnDeletarAnimal')
        botao_deletar_especie_animal.addEventListener('click', function() {
            var id_especie_animal = document.getElementById('animal_id').value

            if (id_especie_animal == ''){
                modal_especie_animal.hide()
                limparDadosEspecieAnimal();
                return
            }

            //parâmetros para deletar
            const mensagem = "Deletar Espécie Animal."
            const url_delete = "/urts/ficha/especie-animal/deletar/" + id_especie_animal + "/"

            const url_apos_delete = window.location.href;
            const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

            //chamar sweetAlert
            sweetAlertDelete(mensagem, url_delete, csrfToken, url_apos_delete)
        })


        function limparDadosEspecieAnimal(){
            //logs
            document.getElementById('animal_id').value = ''
            document.getElementById('animal_log_data_registro').value = ''
            document.getElementById('animal_log_responsavel_registro').value = ''
            document.getElementById('animal_log_ult_atualizacao').value = ''
            document.getElementById('animal_log_responsavel_atualizacao').value = ''
            document.getElementById('animal_log_edicoes').value = ''
            
            //dados da espécie animal
            document.getElementById('id_animal_especie_animal').value = ''
            document.getElementById('id_animal_racas').value = ''
            document.getElementById('id_animal_area_utilizada').value = ''
            document.getElementById('id_animal_observacoes_gerais').value = ''
    
            //Campos ocultos
            document.getElementById('id_urt_animal').value = ''
    
        }


    

    //TÉCNICOS
        const botao_modal_tecnicos = document.getElementById('btnModalTecnicos')
        const modal_tecnicos = new bootstrap.Modal(document.getElementById('urtTecnicosModal'))
        botao_modal_tecnicos.addEventListener('click', function(){
            modal_tecnicos.show();
        })

        //Inserir Novo Técnico
        const botao_inserir_tecnico = document.getElementById('btnNovoTecnico')
        const modal_ficha_tecnico = new bootstrap.Modal(document.getElementById('fichaTecnicoURTModal'))
        botao_inserir_tecnico.addEventListener('click', function(){
            limparDadosTecnicoURT();

            const id_urt_tecnico = document.getElementById('id_urt_tecnico');
            id_urt_tecnico.value = id_urt;
            
            modal_tecnicos.hide();
            modal_ficha_tecnico.show();
        })

        //Formato de Celular
        const tecnico_celular = document.getElementById('id_tecnico_celular')
        tecnico_celular.addEventListener('input', function(){
            formatoCelular(tecnico_celular)
        })

        //Máscaras
        $('#id_tecnico_cpf').mask('000.000.000-00');
        $('#id_tecnico_cnpj').mask('00.000.000/0000-00');

        //Validar CPF do Técnico
        const tecnico_cpf = document.getElementById('id_tecnico_cpf')
        tecnico_cpf.addEventListener('change', function(){
            var cpf_tecnico = tecnico_cpf.value.replace(/\D/g, '');
            var cpf_valido = validaCPF(cpf_tecnico)
            
            if (cpf_valido == false){
                var mensagem = '<span style="font-weight: normal">CPF: ' + tecnico_cpf.value + ' <b style="color: red">INVÁLIDO!</b></span>'
                sweetAlert(mensagem)
                tecnico_cpf.value = ''
            }
        })

        //Validar CNPJ do técnico
        const tecnico_cnpj = document.getElementById('id_tecnico_cnpj')
        tecnico_cnpj.addEventListener('change', function(){
            var cnpj_tecnico = tecnico_cnpj.value.replace(/\D/g, '');
            var cnpj_valido = validarCNPJ(cnpj_tecnico)
            
            if (cnpj_valido == false){
                var mensagem = '<span style="font-weight: normal">CNPJ: ' + tecnico_cnpj.value + ' <b style="color: red">INVÁLIDO!</b></span>'
                sweetAlert(mensagem)
                tecnico_cnpj.value = ''
            }
        })

        //Salvar Técnico
        const botao_salvar_tecnico = document.getElementById('botaoSalvarTecnico')
        botao_salvar_tecnico.addEventListener('click', function(event){
            event.preventDefault();
            salvarTecnicoURT();
        })

        function salvarTecnicoURT() {
            const id_tecnico = document.getElementById('tecnico_id')

            //Verificar preenchimento dos campos
            let preenchimento_incorreto = verificar_campos_tecnico()
            if (preenchimento_incorreto === false) {
                return;
            }
            
            //Enviar para o servidor
                //definir o caminho
                if (id_tecnico.value == '') {
                    postURL = '/urts/ficha/tecnico/salvar/novo/'
                } else
                {
                    postURL = `/urts/ficha/tecnico/salvar/${id_tecnico.value}/`
                }

                //pegar os dados
                let formData = new FormData(document.getElementById('fichaTecnicoURTForm'));
        
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
                        let tecnico_id = data.tecnico_id;
                        localStorage.setItem('tecnicoSalvo', 'true');
                        localStorage.setItem('tecnico_id', tecnico_id);
                        window.location.reload();
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

        function verificar_campos_tecnico() {
            const campos = [
                { id: 'id_tecnico_status_contrato', mensagem: 'Informe o <b>Status do Contrato</b>!' },
                { id: 'id_tecnico_tecnico', mensagem: 'Informe o <b>Nome do Técnico</b>!' },
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

        //Abrir modal do técnico
        function openModalTecnicoURT(id_tecnico) {
            fetch(`/urts/ficha/tecnico/${id_tecnico}/dados`)

                .then(response => {
                    if (!response.ok) {
                        throw new Error('Erro ao buscar dados do Técnico da URT.');
                    }
                    return response.json();
                })
                .then(data => {
                    // Atualizar os campos do formulário no modal com os dados recebidos
                    //log
                    $('#tecnico_id').val(data.id);
                    $('#tecnico_log_data_registro').val(data.log_data_registro);
                    $('#tecnico_log_responsavel_registro').val(data.log_responsavel_registro);
                    $('#tecnico_log_ult_atualizacao').val(data.lot_ult_atualizacao);
                    $('#tecnico_log_responsavel_atualizacao').val(data.log_responsavel_atualizacao);
                    $('#tecnico_log_edicoes').val(data.log_edicoes);

                    //contrato
                    $('#id_tecnico_status_contrato').val(data.status_contrato);
                    $('#id_tecnico_numero_contrato').val(data.numero_contrato);
                    $('#id_tecnico_data_inicio').val(data.data_inicio);
                    $('#id_tecnico_data_fim').val(data.data_fim);

                    //dados da empresa
                    $('#id_tecnico_cnpj').val(data.cnpj);
                    $('#id_tecnico_razao_social').val(data.razao_social);
                    $('#id_tecnico_nome_fantasia').val(data.nome_fantasia);

                    //dados do técnico
                    $('#id_tecnico_cpf').val(data.cpf);
                    $('#id_tecnico_tecnico').val(data.tecnico);
                    $('#id_tecnico_formacao_tecnica').val(data.formacao_tecnica);
                    $('#id_tecnico_celular').val(data.celular);
                    $('#id_tecnico_email').val(data.email);
                    $('#id_tecnico_formacao_tecnica').val(data.formacao_tecnica);

                    //observações
                    $('#id_tecnico_observacoes_gerais').val(data.observacoes);

                    //campos ocultos
                    $('#id_urt_tecnico').val(data.urt_id);

                    // Abrir o modal
                    modal_ficha_tecnico.show();

                })
                .catch(error => {
                    console.log(error);
                });
        }

        const tabela_tecnicos = document.getElementById('tabTecnicosURT');
        tabela_tecnicos.addEventListener('click', function(event) {
        const target = event.target;
        if (target.tagName === 'TD') {
            const row = target.closest('tr');
            const item = row.dataset.id;
            modal_tecnicos.hide();
            openModalTecnicoURT(item);
        }
        });

        //Deletar Técnico da URT
        const botao_deletar_tecnico = document.getElementById('btnDeletarTecnico')
        botao_deletar_tecnico.addEventListener('click', function() {
            var id_tecnico = document.getElementById('tecnico_id').value

            if (id_tecnico == ''){
                modal_ficha_tecnico.hide();
                limparDadosTecnicoURT();
                return
            }

            //parâmetros para deletar
            const mensagem = "Deletar Técnico da URT."
            const url_delete = "/urts/ficha/tecnico/deletar/" + id_tecnico + "/"

            const url_apos_delete = window.location.href;
            const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

            //chamar sweetAlert
            sweetAlertDelete(mensagem, url_delete, csrfToken, url_apos_delete)
        })

        //Limpar dados do modal do Técnico da URT
        function limparDadosTecnicoURT() {
            var campos = [
                'tecnico_id', 'tecnico_log_data_registro', 'tecnico_log_responsavel_registro', 
                'tecnico_log_ult_atualizacao', 'tecnico_log_responsavel_atualizacao', 'tecnico_log_edicoes',

                'id_tecnico_status_contrato', 'id_tecnico_numero_contrato', 'id_tecnico_data_inicio',
                'id_tecnico_data_fim', 
                
                'id_tecnico_cnpj', 'id_tecnico_razao_social', 'id_tecnico_nome_fantasia',

                'id_tecnico_cpf', 'id_tecnico_tecnico', 'id_tecnico_formacao_tecnica',
                'id_tecnico_celular', 'id_tecnico_email', 'id_urt_tecnico',

                'id_tecnico_observacoes_gerais',
            ];
        
            campos.forEach(function(campo) {
                document.getElementById(campo).value = '';
            });

        }
        
    //Relatório URT
    const botao_relatorio_ficha_urt = document.getElementById('btnRelatorioFichaURT')
    botao_relatorio_ficha_urt.addEventListener('click', function(){
        const urt_id = document.getElementById('urt_id').value
        if (urt_id == '') {
            sweetAlert('Não há dados!', 'warning')
            return
        }
        
        var width = 1000;
        var height = 700;
        var left = (window.screen.width / 2) - (width / 2);
        var top = (window.screen.height / 2) - (height / 2);
        
        var url = '/urts/relatorio/ficha-urt/' + urt_id + '/';
        window.open(url, 'newwindow', 'scrollbars=yes, width=' + width + ', height=' + height + ', top=' + top + ', left=' + left);
    })

});