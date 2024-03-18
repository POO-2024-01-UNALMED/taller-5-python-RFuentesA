from zooAnimales.animal import Animal

class Ave(Animal):

    _listado = []
    halcones = 0 
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):

        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas

    def getColorPlumas(self):
        return self._colorPlumas

    @staticmethod
    def crearHalcon(nombre, edad, genero):

        nuevo_alcohon = Ave(
            nombre,
            edad,
            "montanas",
            genero,
            "café glorioso"
        )

        Ave.halcones += 1

        Ave._listado.append(nuevo_alcohon)

        return nuevo_alcohon  

    @staticmethod
    def crearAguila(nombre, edad, genero):

        nueva_aguila = Ave(
            nombre,
            edad,
            "montanas",
            genero,
            "blanco y amarillo"
        )

        Ave.aguilas += 1

        Ave._listado.append(nueva_aguila)

        return nueva_aguila

    @staticmethod
    def cantidadAves():
        return len(Ave._listado)