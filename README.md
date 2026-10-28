# EJERCICIO DE PRÁCTICA: Reservas, Excepciones y Persistencia

## La cadena hotelera "Andes Lodge" necesita un sistema para administrar sus habitaciones, que no permita alojar más huéspedes de los que entran en la habitación y que guarde y recupere el estado del hotel desde un archivo.

### - Punto A: Dominio y reglas de ocupación
  - Crear la excepción CapacidadExcedidaError.
  - Clase base Habitacion (numero, precio_noche, capacidad). El atributo de
    huéspedes debe ser privado y solo modificarse mediante una property.
    Si se intenta asignar menos de 0 huéspedes o más que la capacidad, se lanza
    CapacidadExcedidaError.
  - Método costo_estadia(noches) y método __str__ con la descripción.
  - Clase Suite (hereda de Habitacion), agrega tiene_jacuzzi y
    desayuno_incluido. Redefine costo_estadia (recargo del 20%, + $5000 por
    noche y por huésped si incluye desayuno) y __str__.

### - Punto B: Persistencia
  - Clase GestorHotel con:
      guardar_json(habitaciones, ruta)  -> guarda en hotel_andes.json
      cargar_json(ruta)                 -> devuelve la lista de objetos
                                           (reconstruyendo Habitacion o Suite)
  - Bloque de prueba: capturar CapacidadExcedidaError ante una asignación
    inválida, guardar las habitaciones válidas y volver a cargarlas.