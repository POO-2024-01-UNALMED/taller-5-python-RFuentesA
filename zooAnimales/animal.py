import zooAnimales
from gestio.zona import Zona

class Animal:
    _totalAnimales = 0
    _zona = ""

    def __init__ (self, totalAnimales, nombre, edad, habitat, genero, zona): 
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal._totalAnimales += 1

    def getTotalAnimales (self):
        return _totalAnimales
    

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre


    def setEdad(self, edad):
        self._edad = edad
    def getEdad(self):
        return self._edad


    def setHabitat(self, habitat):
        self._habitat = habitat

    def getHabitat(self):
        return self._habitat
    
    def setGenero(self, genero):
        self._genero = genero

    def getGenero(self):
        return self._genero

    def __Str__ (self):
        return '"Mi nombre es ' + self._nombre + ', tengo una edad de ' + self._edad + ', habito en ' + self._habitat + ' y mi genero es ' + self._genero + ', la zona en la que me ubico es ' + self._zona + ', en el ' + self._zoo