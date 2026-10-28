import modelos

habitacion_1 = modelos.Habitacion(1, capacidad=4, huespedes=2)
habitacion_2 = modelos.Habitacion(2, capacidad=6, precio_noche=150000)
print(modelos.Suite())
print(habitacion_1)

print(f"estadia de 5 noches en habitación 1: ${habitacion_1.costo_estadia(5)}")
print(f"estadia de 5 noches en habitación 2: ${habitacion_2.costo_estadia(5)}")