# Autor: Hector y Esther
# version: 0.0.1
# data: 23/03/2022

from python_herencia.reto2.Entregable import Entregable

class Serie(Entregable):

    # atributos

    __titulo: str
    __numtemp = 3
    entregado = False
    __genero: str
    __creador: str

    # constructores

    # def __init__(self):
    #     pass
    #
    # def __init__(self, newTit, newCreador):
    #     self.__titulo = newTit
    #     self.__creador = newCreador

    def __init__(self, newTit, newNumTemp, newGen, newCreador):
        self.__titulo = newTit
        self.__creador = newCreador
        self.__numtemp = newNumTemp
        self.__genero = newGen


    # metodos

    # gets

    @property
    def titulo(self):
        return self.__titulo

    @property
    def numtemp(self):
        return self.__numtemp

    @property
    def genero(self):
        return self.__genero

    @property
    def creador(self):
        return self.__creador

    # sets

    @titulo.setter
    def titulo(self, newtitulo):
        self.__titulo = newtitulo

    @numtemp.setter
    def numtemp(self, numtemp):
        self.__numtemp = numtemp

    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @creador.setter
    def creador(self, creador):
        self.__creador = creador



    # str

    def __str__(self):
        return (f'[{self.__titulo}, {self.__numtemp}, {self.__genero}, {self.__creador}, {self.entregado}]')

    # metodos propios