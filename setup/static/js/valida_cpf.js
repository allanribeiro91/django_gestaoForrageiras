document.addEventListener("DOMContentLoaded", function () {
    const cpfInput = document.getElementById("cpf");

    cpfInput.addEventListener("input", function () {
        let value = cpfInput.value.replace(/\D/g, ''); // Remove tudo que não for dígito

        if (value.length > 11) {
            value = value.substring(0, 11);
        }

        if (value.length > 2 && value.length <= 6) {
            value = value.replace(/^(\d{3})(\d+)/, '$1.$2');
        } else if (value.length > 6 && value.length <= 9) {
            value = value.replace(/^(\d{3})(\d{3})(\d+)/, '$1.$2.$3');
        } else if (value.length > 9) {
            value = value.replace(/^(\d{3})(\d{3})(\d{3})(\d+)/, '$1.$2.$3-$4');
        }

        cpfInput.value = value; // Atualiza o valor do campo
    });
});

// Função para formatar o CPF com pontos e traço
function formatCPF(cpf) {
    cpf = cpf.replace(/\D/g, ''); // Remove todos os não dígitos

    if (cpf.length <= 3) {
        return cpf;
    } else if (cpf.length <= 6) {
        return cpf.replace(/^(\d{3})(\d+)/, '$1.$2');
    } else if (cpf.length <= 9) {
        return cpf.replace(/^(\d{3})(\d{3})(\d+)/, '$1.$2.$3');
    } else {
        return cpf.replace(/^(\d{3})(\d{3})(\d{3})(\d+)/, '$1.$2.$3-$4');
    }
}

// Função para validar o CPF
function isValidCPF(cpf) {

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


document.addEventListener("DOMContentLoaded", function () {
    const cpfInput = document.getElementById("cpf");
    const errorLabel = document.querySelector(".error-label");

    cpfInput.addEventListener("input", function () {
        const value = cpfInput.value;
        const formattedValue = formatCPF(value);

        cpfInput.value = formattedValue;

        if (value.length === 14) {
            if (!isValidCPF(value)) {
                errorLabel.style.visibility = "visible"; // Mostra a mensagem de erro se o CPF for inválido
            } else {
                errorLabel.style.visibility = "hidden"; // Oculta a mensagem de erro se o CPF for válido
            }
        } else {
            errorLabel.style.visibility = "hidden"; // Oculta a mensagem de erro se o CPF não estiver completo
        }
    });
});



