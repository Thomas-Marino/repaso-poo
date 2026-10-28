import modelos, persistencia

# BLOQUE DE PRUEBA
habitacion_1 = modelos.Habitacion(1, capacidad=4)
habitacion_2 = modelos.Habitacion(2, capacidad=6, precio_noche=150000)
suite_1 = modelos.Suite(3, 200000, 5, False, False)
suite_2 = modelos.Suite(4, 200000, 5, True, True)

# INSTANCIAS
print(habitacion_1)
print(habitacion_2)
print(suite_1)
print(suite_2)

# ASIGNACIÓN DE HUESPEDES
habitacion_1.huespedes = 3
habitacion_2.huespedes = 3
suite_1.huespedes = 4
suite_2.huespedes = 5

# COSTOS POR ESTADIA
print(f"estadia de 5 noches en habitación 1: ${habitacion_1.costo_estadia(5)}")
print(f"estadia de 5 noches en habitación 2: ${habitacion_2.costo_estadia(5)}")
print(f"estadia de 5 noches en suite 1: ${suite_1.costo_estadia(5)}")
print(f"estadia de 5 noches en suite 2: ${suite_2.costo_estadia(5)}")

# CONVERSIÓN A DICT
print(habitacion_1.to_dict())
print(suite_1.to_dict())

# PRUEBA PERSISTENCIA
persistencia.GestorHotel.guardar_json(
    "hotel_andes.json", [habitacion_1, habitacion_2, suite_1, suite_2]
)