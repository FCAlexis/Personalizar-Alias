import os
import os.path
import shutil

from src.style import st
from src import archivo


def presentacion():
    st.logo()


def menu():
    st.sep()
    msj = '\nElige algunas de las opciones a instalar\n'
    msj += '\n1) Alias por defecto, derivados de Debian, Ubuntu..'
    msj += '\n2) Asignar otro alias'
    msj += '\n0) Salir\n'
    msj += '\n> Ingresa una opcion: '

    return int(input(msj))


def backup(directorio):
    shutil.copy(directorio + '/.bashrc', directorio +
                '/.personalizar-alias/src/backup/.bashrc')


def insertar(vector1, vector2):
    for x in vector2:
        vector1.append(x)


def opcion_1(directorio, bashrc):
    st.sep()

    principal = archivo.vectorizar(bashrc)

    defecto = archivo.vectorizar('src/data/buntu.dat')

    insertar(principal, defecto)

    m = open(bashrc, 'w')

    for x in principal:
        m.write(x)
        #print(x, end='')

    m.close()
    st.sep('-')
    print('\n Se pasaron los alias de forma directa!!\n')
    st.sep('-')


def opcion_2(bashrc):
    st.sep()
    print('A continuacion ingresa los valores del Alias a crear')
    nombre_alias = input('Alias: ')
    comando = input('Comando (sin comilla): ')

    alias = "alias {0}='{1}'\n".format(nombre_alias, comando)

    m = open(bashrc, 'a+')
    m.write(alias)
    m.close()

    st.sep('-')
    print('\nEl siguiente alias ya fue agregado\n')
    print(alias)
    st.sep('-')


def main():
    directorio = os.path.expanduser("~{0}".format(os.getenv("USER")))
    bashrc = directorio + '/.bashrc'

    presentacion()
    backup(directorio)

    opcion = -1

    while opcion != 0:
        opcion = menu()

        if opcion == 1:
            opcion_1(directorio, bashrc)
        elif opcion == 2:
            opcion_2(bashrc)


if __name__ == "__main__":
    main()
