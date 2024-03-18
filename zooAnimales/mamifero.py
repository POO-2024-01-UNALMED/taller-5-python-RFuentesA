from zooAnimales.animal import Animal

class Mamifero(Animal):

    _listado = []
    caballos = 0
    leones = 0
    

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):

        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas

    
    def isPelaje(self):
        return self._pelaje
    
    def getPatas(self):
        return self._patas

    @staticmethod
    def crearCaballo(nombre, edad, genero):

        
        nuevo_caballo = Mamifero(
            nombre,
            edad,
            "pradera",
            genero,
            True,
            4 
        )


        Mamifero.caballos += 1

        Mamifero._listado.append(nuevo_caballo)

        return nuevo_caballo

        


    @staticmethod
    def crearLeon(nombre, edad, genero):
        
        nuevo_leon = Mamifero(
            nombre,
            edad,
            "selva",
            genero,
            True,
            4 
        )   

        Mamifero.leones += 1

        Mamifero._listado.append(nuevo_leon)

        return nuevo_leon

        

    @staticmethod
    def cantidadMamiferos():
        return len(Mamifero._listado)
    