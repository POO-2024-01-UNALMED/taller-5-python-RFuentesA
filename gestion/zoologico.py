class Zoologico:

    def __init__(self, nombre, ubicacion, zonas = None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas or []

    def agregarzonas(self, zona = None):
        if zona != None:
            self._zonas.append(zona)

    def getZona(self):
        return self._zonas
    
    def getNombre(self):
        return self._nombre


    def cantidadTotalAnimales(self):
        
        if self._zonas != None:
            total_animales = 0
            for zona in self._zonas:
                total_animales += zona.cantidadAnimales()

        return total_animales
    