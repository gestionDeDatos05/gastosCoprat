// ANIMACION PARA EL PORCENTAJE
document.addEventListener("DOMContentLoaded", function () {
    const counters = document.querySelectorAll('span[id]'); // Selecciona todos los spans con un ID

    counters.forEach(counter => {
        const target = +counter.getAttribute('data-target'); // Obtener el valor del data-target como número
        let current = 0;

        function updateCounter() {
            if (current < target) {
                current++;
                counter.textContent = current + "%"; // Actualizar con el valor actual y el símbolo de porcentaje
                setTimeout(updateCounter, 35); // Ajustar la velocidad de la animación
            } else {
                counter.textContent = target + "%"; // Mostrar el valor final con el símbolo de porcentaje
            }
        }

        updateCounter();
    });
});