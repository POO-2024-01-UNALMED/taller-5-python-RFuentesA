from zooAnimales.animal import Animal

class Anfibio(Animal):

    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):

        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso

    def getColorPiel(self):
        return self._colorPiel
    
    def isVenenoso(self):
        return self._venenoso

    @staticmethod
    def crearRana(nombre, edad, genero):
        
        nueva_rana = Anfibio(
            nombre,
            edad,
            "selva",
            genero,
            "rojo",
            True
        )

        Anfibio.ranas += 1

        Anfibio._listado.append(nueva_rana)

        return nueva_rana

    
    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        
        nueva_salamandra = Anfibio(
            nombre,
            edad,
            "selva",
            genero,
            "negro y amarillo",
            False
        )

        Anfibio.salamandras += 1

        Anfibio._listado.append(nueva_salamandra)

        return nueva_salamandra

    @staticmethod
    def cantidadAnfibios():
        return len(Anfibio._listado)