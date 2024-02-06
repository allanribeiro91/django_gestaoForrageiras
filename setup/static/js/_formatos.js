function cpfFormato(cpf) {
    
    let cpf_valor = cpf.replace(/\D/g, ''); // Remove tudo que não for dígito

    //Restringir tamanho do CPF
    if (cpf_valor.length > 11) {
        cpf_valor = cpf_valor.substring(0, 11); 
    }

    // Formatação ###.###.###-##
    if (cpf_valor.length > 9) {
        cpf_valor = cpf_valor.replace(/^(\d{3})(\d{3})(\d{3})(\d{2})$/, '$1.$2.$3-$4');
    } else if (cpf_valor.length > 6) {
        cpf_valor = cpf_valor.replace(/^(\d{3})(\d{3})(\d{0,3})/, '$1.$2.$3');
    } else if (cpf_valor.length > 3) {
        cpf_valor = cpf_valor.replace(/^(\d{3})(\d{0,3})/, '$1.$2');
    }

    return cpf_valor

}

function cpfValidar(cpf) {
    cpf = cpf.replace(/\D/g, ''); // Remove tudo que não for dígito

    if (cpf.length !== 11) {
        return false; // Verifica se tem 11 dígitos após remover os caracteres não numéricos
    }

    if (/^(\d)\1{10}$/.test(cpf)) {
        return false; // Verifica se todos os dígitos são iguais, o que invalida o CPF
    }

    let soma = 0;
    let resto;

    // Calcula o primeiro dígito verificador
    for (let i = 1; i <= 9; i++) {
        soma += parseInt(cpf.substring(i - 1, i)) * (11 - i);
    }

    resto = (soma * 10) % 11;
    if ((resto === 10) || (resto === 11)) {
        resto = 0;
    }
    if (resto !== parseInt(cpf.substring(9, 10))) {
        return false;
    }

    soma = 0;
    // Calcula o segundo dígito verificador
    for (let i = 1; i <= 10; i++) {
        soma += parseInt(cpf.substring(i - 1, i)) * (12 - i);
    }

    resto = (soma * 10) % 11;
    if ((resto === 10) || (resto === 11)) {
        resto = 0;
    }
    if (resto !== parseInt(cpf.substring(10, 11))) {
        return false;
    }

    return true;
}


function emailInstitucionalValidar(email) {
    const regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.(org\.br)$/;
    return regex.test(email);
}

function emailValidar(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

function celularFormato(numero) {
    // Remove tudo que não for dígito
    let numeroLimpo = numero.replace(/\D/g, '');

    // Limita a 11 dígitos (2 para o DDD e 9 para o número)
    numeroLimpo = numeroLimpo.substring(0, 11);

    // Formata no padrão (##) #####-####
    // Primeiro verifica se o número tem o comprimento total
    if (numeroLimpo.length === 11) {
        return numeroLimpo.replace(/^(\d{2})(\d{5})(\d{4})$/, '($1) $2-$3');
    } else {
        // Se o número é mais curto, formata conforme o comprimento
        if (numeroLimpo.length > 7) {
            return numeroLimpo.replace(/^(\d{2})(\d{0,5})(\d{0,4})$/, '($1) $2-$3');
        } else if (numeroLimpo.length > 2) {
            return numeroLimpo.replace(/^(\d{2})(\d{0,5})$/, '($1) $2');
        } else {
            return numeroLimpo.replace(/^(\d*)$/, '($1');
        }
    }
}

