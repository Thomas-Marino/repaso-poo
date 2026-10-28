import excepciones

class Habitacion:
    numero: int 
    precio_noche: float
    capacidad: int
    __huespedes: int

    def __init__(self, numero: int, precio_noche: float = 80000, capacidad: int = 1):
        self.numero = numero
        self.precio_noche = precio_noche
        self.capacidad = capacidad
        self.huespedes = 0

    def __str__(self):
        return f"numero: {self.numero}, "\
            f"precio por noche: {self.precio_noche}, "\
            f"capacidad: {self.capacidad}, "\
            f"huespedes: {self.huespedes}"

    @property
    def huespedes(self): 
        return self.__huespedes

    @huespedes.setter
    def huespedes(self, cantidad: int):
        if cantidad < 0 or cantidad > self.capacidad: 
            raise excepciones.CapacidadExcedidaError(
                f"cantidad de huespedes ({cantidad}) no válida para la habitación: {self.numero} (capacidad de {self.capacidad})"
            )

        self.__huespedes = cantidad

    def costo_estadia(self, noches: int)-> float:
        """Calcula el costo de estadia multiplicando precio por noche de la instancia por las noches pasadas por parametro"""
        return self.precio_noche * noches

    def to_dict(self)-> dict:
        return {
            "numero": self.numero,
            "precio_noche": self.precio_noche,
            "capacidad": self.capacidad,
            "huespedes": self.huespedes
        }
