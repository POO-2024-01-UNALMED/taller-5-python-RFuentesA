from zooAnimales.animal import Animal

class Reptil(Animal):

    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):

        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola

    def getColorEscamas(self):
        return self._colorEscamas
    
    def getLargoCola(self):
        return self._largoCola

    @staticmethod
    def crearIguana(nombre, edad, genero):
        
        nueva_iguana = Reptil(
            nombre,
           edad,
            "humedal",
           genero,
            "verde",
            3
        )
    
        Reptil.iguanas += 1

        Reptil._listado.append(nueva_iguana)

        return nueva_iguana

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        
        nueva_serpiente = Reptil(
            nombre,
            edad,
            "jungla",
            genero,
            "blanco",
             1
        )

        Reptil.serpientes += 1

        Reptil._listado.append(nueva_serpiente)

        return nueva_serpiente


    @staticmethod
    def cantidadReptiles():
        return len(Reptil._listado)