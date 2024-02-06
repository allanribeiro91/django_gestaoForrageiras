function formatarComoMoeda(valor) {
    // Converte o valor para um número flutuante
    let numero = parseFloat(valor);

    // Formata o número como moeda
    let formatado = numero.toLocaleString('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    });
    return formatado;
}


function moeda(valor) {
    if (typeof valor === 'number') {
        // Se o valor for um número, formatar diretamente
        valor = valor.toFixed(2);
    } else if (typeof valor === 'string') {
        // Se o valor for uma string, remover caracteres não numéricos e converter
        valor = valor.replace(/[^\d.,]/g, '');
        valor = valor.replace(/,/g, '.');
        valor = parseFloat(valor);
        if (isNaN(valor)) {
            valor = 0;
        }
        valor = valor.toFixed(2);
    } else {
        // Se o valor não for nem número nem string, definir como 0
        valor = '0.00';
    }

    // Converter para string para fazer as substituições
    valor = valor.toString();

    // Substituir ponto por vírgula e adicionar o símbolo da moeda
    valor = 'R$ ' + valor.replace('.', ',').replace(/(\d)(?=(\d{3})+\d)/g, "$1.");

    return valor;
}

function formatoCelular(campo) {

    celular = campo.value.replace(/\D/g, '');

    if (celular.length > 11) {
        celular = celular.substring(0, 11);
    }

    if (celular.length <= 2) {
        celular = celular.replace(/^(\d{0,2})/, '($1');
    } else if (celular.length <= 6) {
        celular = celular.replace(/^(\d{2})(\d+)/, '($1) $2');
    } else if (celular.length <= 10) {
        celular = celular.replace(/^(\d{2})(\d{5})(\d{0,3})/, '($1) $2-$3');
    } else {
        celular = celular.replace(/^(\d{2})(\d{5})(\d{4})/, '($1) $2-$3');
    }

    campo.value = celular;

}

function formatoTelefone(campo) {

    telefone = campo.value.replace(/\D/g, '');

    if (telefone.length >= 10) {
        telefone = telefone.substring(0, 10);
    }

    if (telefone.length <= 2) {
        telefone = telefone.replace(/^(\d{0,2})/, '($1');
    } else if (telefone.length <= 5) {
        telefone = telefone.replace(/^(\d{2})(\d+)/, '($1) $2');
    } else if (telefone.length <= 9) {
        telefone = telefone.replace(/^(\d{2})(\d{4})(\d{0,3})/, '($1) $2-$3');
    } else {
        telefone = telefone.replace(/^(\d{2})(\d{4})(\d{4})/, '($1) $2-$3');
    }

    campo.value = telefone;

}


function numeroInteiroMilhar(campo) {
    
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

function formatarValorDecimal(valor) {
    // Remove tudo que não é número
    valor = valor.replace(/\D/g, '');

    // Divide o valor por 100 para obter o formato decimal
    valor = (valor / 100).toFixed(2);

    // Formata o número com separador de milhar e vírgula para os decimais
    valor = valor.replace('.', ',').replace(/\B(?=(\d{3})+(?!\d))/g, '.');

    return valor;
}

function validaCPF(cpf) {

    cpf = cpf.replace(/\D/g, ''); // Remove todos os não dígitos

    if (cpf.length !== 11 || /^(\d)\1{10}$/.test(cpf)) {
        return false; // CPF com todos os dígitos iguais é inválido
    }

    if (cpf.length === 11) {
        var sum = 0;
        var rest;
        for (var i = 1; i <= 9; i++) {
            sum = sum + parseInt(cpf.substring(i - 1, i)) * (11 - i);
        }
        rest = (sum * 10) % 11;
        if (rest === 10 || rest === 11) {
            rest = 0;
        }
        if (rest !== parseInt(cpf.substring(9, 10))) {
            return false;
        }

        sum = 0;
        for (var i = 1; i <= 10; i++) {
            sum = sum + parseInt(cpf.substring(i - 1, i)) * (12 - i);
        }
        rest = (sum * 10) % 11;
        if (rest === 10 || rest === 11) {
            rest = 0;
        }
        if (rest !== parseInt(cpf.substring(10, 11))) {
            return false;
        }

        return true; // CPF válido
    }

    return false; // CPF com menos de 11 dígitos não é válido
}

function validarCNPJ(cnpj) {
    cnpj = cnpj.replace(/[^\d]+/g, '');

    if (cnpj == '') return false;

    if (cnpj.length != 14)
        return false;

    // Elimina CNPJs invalidos conhecidos
    if (cnpj == "00000000000000" ||
        cnpj == "11111111111111" ||
        cnpj == "22222222222222" ||
        cnpj == "33333333333333" ||
        cnpj == "44444444444444" ||
        cnpj == "55555555555555" ||
        cnpj == "66666666666666" ||
        cnpj == "77777777777777" ||
        cnpj == "88888888888888" ||
        cnpj == "99999999999999")
        return false;

    // Valida DVs
    tamanho = cnpj.length - 2
    numeros = cnpj.substring(0, tamanho);
    digitos = cnpj.substring(tamanho);
    soma = 0;
    pos = tamanho - 7;
    for (i = tamanho; i >= 1; i--) {
        soma += numeros.charAt(tamanho - i) * pos--;
        if (pos < 2)
            pos = 9;
    }
    resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
    if (resultado != digitos.charAt(0))
        return false;

    tamanho = tamanho + 1;
    numeros = cnpj.substring(0, tamanho);
    soma = 0;
    pos = tamanho - 7;
    for (i = tamanho; i >= 1; i--) {
        soma += numeros.charAt(tamanho - i) * pos--;
        if (pos < 2)
            pos = 9;
    }
    resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
    if (resultado != digitos.charAt(1))
        return false;

    return true;
}
