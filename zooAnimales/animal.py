import zooAnimales
from gestio.zona import Zona

class Animal:
    _totalAnimales = 0
    _zona = ""

    def __init__ (self, nombre, edad, habitat, genero): 
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal._totalAnimales += 1

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getHabitat(self):
        return self._habitat
    
    def getGenero(self):
        return self._genero

    def toString(self):
        n = self._nombre
        e = self._edad
        h = self._habitat
        g = self._genero

        mensaje = "Mi nombre es " + n + "," + " tengo una edad de " + str(e) + ", habito en " + h + " y mi genero es " + g

        if isinstance(self._zona, Zona):
            zonita = self._zona[0].getNombre()
            zoo = self._zona[0].getZoo().getNombre()
            mensaje += ", la zona en la que me ubico es " + zonita + ", en el " + zoo
            return mensaje
        
        else:
            return mensaje