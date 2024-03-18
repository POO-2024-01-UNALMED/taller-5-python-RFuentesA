import zooAnimales
from gestion.zona import Zona

class Animal:

    _totalAnimales = 0
    _zona = ""


    def __init__(self, nombre, edad, habitat, genero):

        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal._totalAnimales += 1


    def agregarzonas(self, zona = None):

        if isinstance(zona, Zona):

            self._zona.pop()
            self._zona.append(zona)

    def getNombre(self):
        return self._nombre        

    def getEdad(self):
        return self._edad
    
    def getHabitat(self):
        return self._habitat

    def getGenero(self):
        return self._genero

    @staticmethod
    def totalPorTipo():

        mamiferos = str(zooAnimales.mamifero.Mamifero.cantidadMamiferos())
        aves = str(zooAnimales.ave.Ave.cantidadAves())
        reptiles = str(zooAnimales.reptil.Reptil.cantidadReptiles())
        peces = str(zooAnimales.pez.Pez.cantidadPeces())
        anfibios = str(zooAnimales.anfibio.Anfibio.cantidadAnfibios())


        mensaje = "Mamiferos : " + mamiferos 
        mensaje += "\nAves : " + aves 
        mensaje += "\nReptiles : " + reptiles
        mensaje += "\nPeces : " + peces
        mensaje += "\nAnfibios : " + anfibios

        return mensaje

    def toString(self):

        nombre = self._nombre 
        edad = self._edad
        habitat = self._habitat
        genero = self._genero

        mensaje = "Mi nombre es " + nombre + "," + " tengo una edad de " + str(edad) + ", habito en " + habitat + " y mi genero es " + genero 

        #Verificar que la zona ingresada, relamente sea un objeto de la clase Zona
        if isinstance(self._zona, Zona):

            zonita = self._zona[0].getNombre()
            zoo = self._zona[0].getZoo().getNombre()

            mensaje += ", la zona en la que me ubico es " + zonita + ", en el " + zoo

            return mensaje

        else:

            return mensaje
