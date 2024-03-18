class Zona:
    def __init__(self, nombre, zoo = None, animales = None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = animales or []

    def agregarAnimales(self, animal = None):
        if animal != None:
            self._animales.append(animal)
        
    def cantidadAnimales(self):
        return len(self._animales)

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def setZoo(self, zoo):
        self._zoo = zoo
    
    def getZoo(self):
        return self._zoo