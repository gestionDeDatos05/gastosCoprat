


// ANIMACION PARA LA ANIMACION DEL CATALOGO EN EL PRECIO
document.addEventListener("DOMContentLoaded", () => {
    const duration = 3500; // Duración de la animación en milisegundos

    function animateValue(element, start, end, duration) {
        const range = end - start;
        let startTime = null;

        function step(currentTime) {
            if (!startTime) startTime = currentTime;
            const progress = Math.min((currentTime - startTime) / duration, 1);
            const value = Math.floor(progress * range + start);
            element.textContent = `$ ${value}`;
            if (progress < 1) {
                requestAnimationFrame(step);
            }
        }

        requestAnimationFrame(step);
    }

    // Selecciona todos los elementos con clase `card-text-contenedor-1`
    document.querySelectorAll(".card-text-contenedor-1").forEach(element => {
        const endValue = parseInt(element.getAttribute("data-end-value"), 10); // Obtén el valor final
        animateValue(element, 0, endValue, duration); // Anima cada elemento
    });
});


