class Vehiculo:
    color = 'blanco'
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 110


mi_coche = Coche()
print(mi_coche)
