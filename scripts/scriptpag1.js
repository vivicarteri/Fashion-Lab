document.addEventListener('DOMContentLoaded', () => {
    const btnSubmeter = document.getElementById('btnSubmeter');
    const textArea = document.getElementById('textArea');
    const selecionado = document.querySelectorAll('input[name="verificacao"]');

    btnSubmeter.addEventListener('click', () => {
        const text = textArea.value;

        let selecionados = '';
        selecionado.forEach(radio => {
            if (radio.checked) {
                selecionados = radio.value;
                selecionadoId = radio.id;
            }
        });

        if (!selecionados) {
            alert('Por favor, selecione um padrão de busca.');
            return;
        }

        const regex = new RegExp(selecionados, 'g');
        const matches = text.match(regex);

        if (matches) {
            alert(`Padrão ${selecionadoId} encontrado, quantidade de ocorrências ${matches.length}`);
        } else {
            alert(`Padrão ${selecionadoId} não encontrado`);
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const limpar = document.getElementById('btnLimpar');
    const textBox = document.getElementById('textArea');
    const radioButtons = document.querySelectorAll('input[type="radio"][name="verificacao"]');

    limpar.addEventListener('click', () => {
        textBox.value = '';

        radioButtons.forEach(radio => radio.checked = false);
    });
});
