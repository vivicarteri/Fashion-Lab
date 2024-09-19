document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('.formulario');
    const btnSubmeter = document.getElementById('btnSubmeter');
    const btnLimpar = document.getElementById('btnLimpar');

    function validarCPF(cpf) {
        cpf = cpf.replace(/\D/g, '');

        if (cpf.length !== 11) return false;

        let soma = 0;
        let resto;

        for (let i = 1; i <= 9; i++) {
            soma += parseInt(cpf.substring(i - 1, i)) * (11 - i);
        }
        resto = (soma * 10) % 11;
        if (resto === 10 || resto === 11) resto = 0;
        if (resto !== parseInt(cpf.substring(9, 10))) return false;

        soma = 0;
        for (let i = 1; i <= 10; i++) {
            soma += parseInt(cpf.substring(i - 1, i)) * (12 - i);
        }
        resto = (soma * 10) % 11;
        if (resto === 10 || resto === 11) resto = 0;
        if (resto !== parseInt(cpf.substring(10, 11))) return false;

        return true;
    }

    function validarDataNascimento(data) {
        const regex = /^\d{2}\/\d{2}\/\d{4}$/;
        if (!regex.test(data)) return false;

        const [dia, mes, ano] = data.split('/').map(Number);
        const dataObj = new Date(ano, mes - 1, dia);

        return dataObj.getDate() === dia && dataObj.getMonth() === mes - 1 && dataObj.getFullYear() === ano;
    }

    function exibirErros(erros) {
        if (erros.length > 0) {
            alert("Erros encontrados:\n" + erros.join('\n'));
        } else {
            alert("Formulário enviado com sucesso!");
            form.reset(); 
        }
    }

    btnSubmeter.addEventListener('click', function(event) {
        event.preventDefault();
        const errors = [];

        const nome = document.getElementById('name').value;
        if (/\d/.test(nome)) {
            errors.push("O nome não deve conter números.");
        }

        const cpf = document.getElementById('cpf').value.replace(/\D/g, '');
        const cpfFormatado = document.getElementById('cpf').value;
        if (!/^\d{3}\.\d{3}\.\d{3}-\d{2}$/.test(cpfFormatado) || !validarCPF(cpf)) {
            errors.push("O CPF deve ter 11 dígitos numéricos e ser válido.");
        }

        const dob = document.getElementById('dob').value;
        if (!validarDataNascimento(dob)) {
            errors.push("A data de nascimento deve estar no formato dd/mm/yyyy e ser uma data válida.");
        }

        const username = document.getElementById('username').value;
        if (/^\d/.test(username)) {
            errors.push("O nome de usuário não deve começar com um número.");
        }
        if (/\s/.test(username)) {
            errors.push("O nome de usuário não deve conter espaços.");
        }
        if (!/^[a-z0-9._]+$/.test(username)) {
            errors.push("O nome de usuário deve conter apenas letras minúsculas, números, pontos e underlines.");
        }

        const email = document.getElementById('email').value;
        if (!/^[a-z0-9._]+@[a-z0-9._]+\.[a-z]{2,}$/.test(email)) {
            errors.push("O e-mail deve estar no formato válido e em minúsculas.");
        }

        const password1 = document.getElementById('password1').value;
        if (password1.length < 8 || password1.length > 15) {
            errors.push("A senha deve ter entre 8 e 15 caracteres.");
        }
        if (!/[A-Z]/.test(password1)) {
            errors.push("A senha deve conter pelo menos uma letra maiúscula.");
        }
        if (!/[1-9]/.test(password1)) {
            errors.push("A senha deve conter pelo menos um número (exceto zero).");
        }
        if (!/[!@#$%^&*(),.?":{}|<>]/.test(password1)) {
            errors.push("A senha deve conter pelo menos um caractere especial.");
        }
        if (/0/.test(password1)) {
            errors.push("A senha não pode conter o número zero.");
        }

        const password2 = document.getElementById('password2').value;
        if (password1 !== password2) {
            errors.push("As senhas não correspondem.");
        }

        exibirErros(errors);
    });

    btnLimpar.addEventListener('click', function() {
        form.reset();
    });
});
