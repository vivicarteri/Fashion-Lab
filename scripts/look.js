document.addEventListener('DOMContentLoaded', () => {
    const carousels = document.querySelectorAll('.grid-container'); // Seleciona todos os carrosséis

    carousels.forEach(carousel => {
        const grid = carousel.querySelector('.grid'); // O grid atual
        const prevButton = carousel.querySelector('.prev'); // Botão "anterior"
        const nextButton = carousel.querySelector('.next'); // Botão "próximo"

        // Distância para rolar (ajuste para se alinhar perfeitamente)
        const scrollAmount = 130;

        // Evento para o botão "anterior"
        prevButton.addEventListener('click', () => {
            grid.scrollBy({
                left: -scrollAmount, // Rolagem para trás
                behavior: 'smooth', // Comportamento suave
            });
        });

        // Evento para o botão "próximo"
        nextButton.addEventListener('click', () => {
            grid.scrollBy({
                left: scrollAmount, // Rolagem para frente
                behavior: 'smooth', // Comportamento suave
            });
        });
    });
});