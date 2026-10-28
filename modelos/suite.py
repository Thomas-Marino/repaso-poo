#Punto A: Dominio y reglas de ocupación
#  - Crear la excepción CapacidadExcedidaError. OK
#  - Clase base Habitacion (numero, precio_noche, capacidad). El atributo de
#    huéspedes debe ser privado y solo modificarse mediante una property.
#    Si se intenta asignar menos de 0 huéspedes o más que la capacidad, se lanza
#    CapacidadExcedidaError. OK
#  - Método costo_estadia(noches) y método __str__ con la descripción. OK
#  - Clase Suite (hereda de Habitacion), agrega tiene_jacuzzi y
#    desayuno_incluido. Redefine costo_estadia (recargo del 20%, + $5000 por
#    noche y por huésped si incluye desayuno) y __str__. OK

import modelos

class Suite(modelos.Habitacion): 
    tiene_jacuzzi: bool
    desayuno_incluido: bool

    def __init__(
        self, 
        numero: int, 
        precio_noche: float, 
        capacidad: int, 
        tiene_jacuzzi: bool, 
        desayuno_incluido: bool
    ):
        super().__init__(numero, precio_noche, capacidad)
        self.tiene_jacuzzi = tiene_jacuzzi
        self.desayuno_incluido = desayuno_incluido

    def __str__(self):
        str_habitacion = super().__str__()
        return str_habitacion + f", tiene jacuzzi: {self.tiene_jacuzzi}, " \
            f"desayuno incluido: {self.desayuno_incluido}"
        

    def costo_estadia(self, noches):
        costo_base = super().costo_estadia(noches)
        costo_estadia = costo_base * 1.20

        if self.desayuno_incluido:
            costo_estadia += 5000 * noches * self.huespedes
        return costo_estadia        

    def to_dict(self):
        dict_suite = super().to_dict()
        dict_suite["tiene_jacuzzi"] = self.tiene_jacuzzi
        dict_suite["desayuno_incluido"] = self.desayuno_incluido

        return dict_suite