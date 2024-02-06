document.addEventListener("DOMContentLoaded", function () {
    const cpf = document.getElementById('cpf');
    const email_institucional = document.getElementById('email_institucional')
    const email_pessoal = document.getElementById('email_pessoal')
    const celular = document.getElementById('celular')
    const senha1 = document.getElementById('senha1')
    const senha2 = document.getElementById('senha2')

    cpf.addEventListener('input', function() {
        //Formatar o CPF
        let cpfFormatado = cpfFormato(this.value);
        this.value = cpfFormatado; // Atualiza o valor do campo com o CPF formatado

        //Validar o CPF quando atingir o tamanho completo
        if (this.value.length === 14) {

            var cpf_validacao = cpfValidar(this.value);
            if (!cpf_validacao) {
                sweetAlert('CPF Inválido', 'error', 'red');
                this.value = '';
            }
        }
    });

    email_institucional.addEventListener('change', function() {
        let validacaoEmail = emailInstitucionalValidar(this.value)

        //Validar email institucional
        if (validacaoEmail === false) {
            sweetAlert('Email Inválido<br><span style="font-weight: normal !important;">' + this.value + '</span>', 'error', 'red');
            this.value = '';
        }
    });

    email_pessoal.addEventListener('change', function() {
        let validacaoEmail = emailValidar(this.value)

        //Validar email pessoal
        if (validacaoEmail === false) {
            sweetAlert('Email Inválido<br><span style="font-weight: normal !important;">' + this.value + '</span>', 'error', 'red');
            this.value = '';
            this.focus();
        }

    });

    celular.addEventListener('input', function() {
        //Formatar o Celular
        let celularFormatado = celularFormato(this.value);
        this.value = celularFormatado;

    });

    senha1.addEventListener('change', function() {
        tamanhoSenha = senha1.value.length
        if (tamanhoSenha < 6) {
            sweetAlert('Informe uma senha válida!', 'warning', 'orange');
            this.value = '';
            this.focus();
        }
    });

    senha2.addEventListener('change', function(){
        verificarSenhas = (senha2.value == senha1.value)
        if (!verificarSenhas) {
            sweetAlert('Senhas diferentes!', 'warning', 'orange');
            this.value = '';
            this.focus();
        }
    });

});



