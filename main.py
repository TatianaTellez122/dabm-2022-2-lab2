# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 21:46:56 2022

@author: Tatiana Téllez
"""

from classes.menu import *
from classes.equipo import *
from classes.prestamo import *


class MenuEstudiantes:
    pass


def main():
    menu= Menu("Escuela de Ingeniería")
    op=menu.ver()
    if op =="1":
        menu2= MenuTecnicos()
        op2=menu2.ver()

        if op2=="1":
            e=crearEquipo()
            e.save()
        elif op2=="2":
            p=crearPrestamo()
            p.save()
        elif op2=="3":
            registroMantenimiento()
        elif op2=="4":
            registroEntrega()
        else:
            print("Opción inválida")
            main()
    elif op=="2":
        menu2=MenuEstudiantes()
        op2=menu2.ver()
        if op2=="1":
            verPrestamos()
        elif op2=="2":
            consultarEquipo()
'''
if __name__=="__main__":
    main()
'''
main()


