class Caja:
    def __init__(self,  contenido, peso):
        self.contenido = contenido
        self.peso = peso
    
    def __str__(self):
        return (f"Caja de {self.contenido} que pesa {self.peso} kg")
    
class Camion:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cajas = []
    
    def agregar_caja(self, caja):
        peso_actual = 0
        for c in self.cajas:
            peso_actual += c.peso
        
        if peso_actual + caja.peso <= self.capacidad:
            self.cajas.append(caja)
            print(f"Caja de {caja.contenido} agregada al camión.")
        else:
            print(f"No se puede agregar la caja de {caja.contenido}. Capacidad máxima alcanzada.")
        
    def mostrar_carga(self):
        print("Cajas en el camión:")
        for caja in self.cajas:
            print(f"- {caja}")

# PROGRAMA PRINCIPAL

c1 = Caja("libros", 10)
c2 = Caja("ropa", 5)
c3 = Caja("herramientas", 15)

camion = Camion(capacidad = 35)
camion.agregar_caja(c1)
camion.agregar_caja(c2)
camion.agregar_caja(c3)

camion.mostrar_carga()
