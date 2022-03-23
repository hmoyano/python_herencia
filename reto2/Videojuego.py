# Autor: Hector y Esther
# version: 0.0.1
# data: 23/03/2022

class Videojuego():

    #atributos

    __titulo: str
    __horas = 10
    entregado = False
    __genero: str
    __compania: str

    # constructores

    # def __init__(self):
    #     pass
    #
    # def __init__(self, newTit, newHoras):
    #     self.__titulo = newTit
    #     self.__horas = newHoras

    def __init__(self, newTit, newHoras, newGen, newCompania):
        self.__titulo = newTit
        self.__horas = newHoras
        self.__genero = newGen
        self.__compania = newCompania

    # metodos

    #gets

    @property
    def titulo(self):
        return self.__titulo

    @property
    def horas(self):
        return self.__horas

    @property
    def genero(self):
        return self.__genero

    @property
    def compania(self):
        return self.__compania

    #sets

    @titulo.setter
    def titulo(self, newtitulo):
        self.__titulo = newtitulo

    @horas.setter
    def horas(self, horas):
        self.__horas = horas

    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @compania.setter
    def creador(self, compania):
        self.__compania = compania

    # str

    def __str__(self):
        return (f'[{self.__titulo}, {self.__horas}, {self.__genero}, {self.__compania}, {self.entregado}]')