# Autor: Hector y Esther
# version: 0.0.1
# data: 23/03/2022

from python_herencia.reto2.Serie import Serie

if __name__ == '__main__':
    ser1 = Serie('Lost', 6, 'Terror', 'Pepito')

    print(ser1)

    print(ser1.titulo)

    print(dir(ser1))

    ser1.titulo = 'Ark'
    ser1.genero = 'Accion'

    print(ser1)


