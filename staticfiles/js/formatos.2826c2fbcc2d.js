document.addEventListener("DOMContentLoaded", function () {
    const celularInput = document.getElementById("celular"); // Certifique-se de que o campo de input do celular tenha o id "celular"

    celularInput.addEventListener("input", function () {
        let value = celularInput.value.replace(/\D/g, ''); // Remove tudo que não for dígito

        if (value.length > 11) {
            value = value.substring(0, 11); // Limita a 11 dígitos
        }

        if (value.length <= 2) {
            value = value.replace(/^(\d{0,2})/, '($1'); // Formato (##
        } else if (value.length <= 6) {
            value = value.replace(/^(\d{2})(\d+)/, '($1) $2'); // Formato (##) ####
        } else if (value.length <= 10) {
            value = value.replace(/^(\d{2})(\d{5})(\d{0,3})/, '($1) $2-$3'); // Formato (##) #####-####
        } else {
            value = value.replace(/^(\d{2})(\d{5})(\d{4})/, '($1) $2-$3'); // Formato completo (##) #####-####
        }

        celularInput.value = value; // Atualiza o valor do campo
    });
});


document.addEventListener("DOMContentLoaded", function () {
    const emailInput = document.getElementById("email_ms");

    emailInput.addEventListener("input", function () {
        if (emailInput.value.includes("@") && !emailInput.hasAttribute("readonly")) {
            emailInput.value = emailInput.value.split("@")[0] + "@saude.gov.br";
            emailInput.setAttribute("readonly", true); // Desativa a edição do campo
        }
    });

    // Permitir edição se o usuário remove o "@" ao apagar
    emailInput.addEventListener("keydown", function(event) {
        if(event.key === "Backspace" || event.key === "Delete") {
            emailInput.removeAttribute("readonly");
        }
    });

    // Permitir que o campo seja totalmente apagado
    emailInput.addEventListener("click", function () {
        if(emailInput.hasAttribute("readonly")) {
            emailInput.removeAttribute("readonly");
            emailInput.select();
        }
    });
});

