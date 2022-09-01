# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 21:45:33 2022

@author: Tatiana Téllez
"""

class Menu:
    def __init__(self, laboratorio):
        self.laboratorio=laboratorio
    
    def ver(self):
        print("BIENVENIDO AL SISTEMA".center(50,"*"))
        print("Laboratorio:"+self. laboratorio)
        print("1.Tecnicos")
        print("2.Estudiantes")
        op=input(">>>")
        
        return op

class MenuTecnicos:
    def ver(self):
        print("MENU TECNICOS DE LABORATORIO".center(20,"*"))
        print("1.Registrar equipos")
        print("2.Registrar prestamo")
        op=input(">>>")
        print(op)
        return op

'''
if __name__=='__main__' :
    menu= Menu("Escuela de Ingenieros")
    op=menu.ver()
    if op=="1":
        menu2=MenuTecnicos()
        op2=menu2.ver()
'''