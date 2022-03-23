# Autor: Hector y Esther
# version: 0.0.1
# data: 15/03/2022

class Serie():

    # atributos

    __titulo: str
    __numtemp = 3
    entregado = 'false'
    __genero: str
    __creador: str

    # constructores

    # def __init__(self):
    #     pass
    #
    # def __init__(self, newTit, newCreador):
    #     self.__titulo = newTit
    #     self.creador = newCreador

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

    @titulo.setter
    def set_titulo(self, newtitulo):
        self.__titulo = newtitulo

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



    @numtemp.setter
    def set_numtemp(self, numtemp):
        self.__numtemp = numtemp

    @genero.setter
    def set_genero(self, genero):
        self.__genero = genero

    @creador.setter
    def set_creador(self, creador):
        self.__creador = creador



    # str

    def __str__(self):
        return (f'[{self.__titulo}, {self.__numtemp}, {self.__genero}, {self.__creador}]')