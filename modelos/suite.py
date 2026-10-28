#Punto A: Dominio y reglas de ocupación
#  - Crear la excepción CapacidadExcedidaError. OK
#  - Clase base Habitacion (numero, precio_noche, capacidad). El atributo de
#    huéspedes debe ser privado y solo modificarse mediante una property.
#    Si se intenta asignar menos de 0 huéspedes o más que la capacidad, se lanza
#    CapacidadExcedidaError. OK
#  - Método costo_estadia(noches) y método __str__ con la descripción. OK
#  - Clase Suite (hereda de Habitacion), agrega tiene_jacuzzi y
#    desayuno_incluido. Redefine costo_estadia (recargo del 20%, + $5000 por
#    noche y por huésped si incluye desayuno) y __str__.

import modelos

class Suite(modelos.Habitacion): 
    tiene_jacuzzi: bool
    desayuno_incluido: bool

    def __init__()