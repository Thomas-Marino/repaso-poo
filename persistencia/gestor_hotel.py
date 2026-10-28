import modelos, json

class GestorHotel:
    @staticmethod
    def guardar_json(ruta: str, habitaciones: list[modelos.Habitacion | modelos.Suite])-> None:
        with open(ruta, "w", encoding="utf-8") as archivo:
            lista = []
            for h in habitaciones:
                lista.append(h.to_dict())
            json.dump(lista, archivo)

    @staticmethod
    def cargar_json(ruta: str)-> list[modelos.Habitacion | modelos.Suite]:
        pass