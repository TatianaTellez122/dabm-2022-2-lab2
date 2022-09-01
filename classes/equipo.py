# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 21:44:42 2022

@author: Tatiana Téllez
"""

from tabulate import tabulate
class Equipo:
    file="database/equipos.csv"
    def __init__(self, nombre, proveedor, cantidad, referencia, ciclo, fum=""):
        self.nombre = nombre
        self.proveedor = proveedor
        self.cantidad = cantidad
        self.referencia = referencia
        self.ciclo = ciclo
        self.fum = fum

    def verDatos(self):
        header = ["NOMBRE", "REFERENCIA", "CANTIDAD", "PROVEEDOR", "CICLO", "FUM"]
        datos=[[self.nombre, self.referencia,self.cantidad , self.proveedor, self.ciclo, self.fum]]
        print(tabulate(datos, header, tablefmt="grid"))

    def save(self):
        f=open(self.file,'a')
        linea=";".join(self.nombre,self.referencia,self.cantidad)
        f.write(linea+"\n")
        f.close()

    def consulta(self,nombre):
        pass

def crearEquipo():
    print("REGISTRAR NUEVO EQUIPO")
    nombre = input("Nombre:")
    proveedor = input("Proveedor:")
    referencia = input("Referencia:")
    ciclo = input("Ciclo de mantenimiento (dias):")
    cantidad = input("Cantidad")

    e = Equipo(nombre, proveedor,cantidad,referencia,ciclo,fum)
    
    return e

def consultarEquipo():
    print("Consulta de equipos")
    nombre=input("Nombre del equipo")

def registroMantenimiento():
    pass

def registroEntrega():
    pass
