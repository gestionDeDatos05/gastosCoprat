function cambiarColumnas(columnas) {
    const contenedor = document.getElementById("contenedor-cards");
    const tarjetas = contenedor.querySelectorAll(".col-lg-3, .col-lg-4, .col-lg-6, .col-lg-12, .col-md-3, .col-md-4, .col-md-6, .col-md-12, .col-sm-3, .col-sm-4, .col-sm-6, .col-sm-12");

    // Calcular la nueva clase Bootstrap basada en el número de columnas
    const nuevaClaseLg = `col-lg-${Math.floor(12 / columnas)}`;
    const nuevaClaseMd = `col-md-${Math.floor(12 / columnas)}`;
    const nuevaClaseSm = `col-sm-${Math.floor(12 / columnas)}`;

    // Eliminar todas las clases relacionadas con columnas
    tarjetas.forEach(tarjeta => {
        tarjeta.classList.remove("col-lg-3", "col-lg-4", "col-lg-6", "col-lg-12",
            "col-md-3", "col-md-4", "col-md-6", "col-md-12",
            "col-sm-3", "col-sm-4", "col-sm-6", "col-sm-12");
    });

    // Agregar las nuevas clases calculadas para los diferentes tamaños de pantalla
    tarjetas.forEach(tarjeta => {
        tarjeta.classList.add(nuevaClaseLg);
        tarjeta.classList.add(nuevaClaseMd);
        tarjeta.classList.add(nuevaClaseSm);
    });
}
