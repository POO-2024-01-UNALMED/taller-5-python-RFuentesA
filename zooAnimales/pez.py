from zooAnimales.animal import Animal

class Pez(Animal):


    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):

        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def getCantidadAletas(self):
        return self._cantidadAletas
    

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        
        nuevo_salmon = Pez(
            nombre,
           edad,
            "oceano",
            genero,
            "rojo",
            6
        )

        Pez.salmones += 1

        Pez._listado.append(nuevo_salmon)
        
        return nuevo_salmon

    
    @staticmethod
    def crearBacalao(nombre, edad, genero):
        
        nuevo_bacalao = Pez(
            nombre,
            edad,
            "oceano",
            genero,
            "gris",
            6
        )

        Pez.bacalaos += 1

        Pez._listado.append(nuevo_bacalao)

        return nuevo_bacalao

    @staticmethod
    def cantidadPeces():
        return len(Pez._listado)