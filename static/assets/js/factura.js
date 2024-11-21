const facturaInput = document.getElementById('facturaInput');
const interesadoCheckbox = document.getElementById('interesadoCheckbox');
const facturaHiddenInput = document.getElementById('facturaHiddenInput');

// Función para habilitar/deshabilitar el campo de email
function toggleEmailInput() {
    if (interesadoCheckbox.checked) {
        facturaInput.disabled = false;
        facturaHiddenInput.disabled = true; // Deshabilitar el campo oculto cuando el campo visible esté habilitado
    } else {
        facturaInput.disabled = true;
        facturaInput.value = 'SF'; // Limpia el campo si se deshabilita
        facturaHiddenInput.value = 'SF'; // Enviar un valor por defecto en el campo oculto
        facturaHiddenInput.disabled = false; // Habilitar el campo oculto cuando el campo visible esté deshabilitado
    }
}

// Escuchar cambios en el checkbox
interesadoCheckbox.addEventListener('change', toggleEmailInput);

// Llamada inicial para configurar el estado del input
toggleEmailInput();