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
        linea=";".join([self.nombre,self.referencia,self.cantidad,self.proveedor,self.ciclo,self.fum])
        f.write(linea+"\n")
        f.close()

    def consulta(self,nombre):
        pass

def crearEquipo():
    print("REGISTRAR UN NUEVO EQUIPO")
    nombre = input("Nombre del equipo:")
    proveedor = input("Proveedor:")
    referencia = input("Referencia:")
    ciclo = input("Ciclo de mantenimiento (dias):")
    cantidad = input("Cantidad:")
    fum=input("Fecha de último mantenimiento:(yyyy-mm-dd)")

    e = Equipo(nombre, proveedor,cantidad,referencia,ciclo,fum)
    return e


"""def verPrestamos():
    archivo = open("database/prestamos.csv","r")
    prestamos = archivo.readlines()
    header = ["Nombre","Carnet","Equipo","Fecha de prestamo","Fecha de entrega"]
    matriz1 = []

    numero_carnet = input("Por favor ingrese su número de carnet:")

    for i in prestamos:
        i=i.replace("\n","")
        i=i.split(";")
        matriz1.append(i)

    print(tabulate(matriz1,header,tablefmt="grid"))

    matriz_prestamos=[]
    for i in range(0 , len(matriz1)):
        if matriz1[i][1] == numero_carnet:
            matriz_prestamos.append(matriz1[i])
            

    print(tabulate(matriz_prestamos, header, tablefmt="grid"))
"""
def consultarEquipo():
    a=open("database/equipos.csv","r")
    disponibilidad=a.readlines()
    header=["Nombre","Proveedor","Referencia","Ciclo","Cantidad","Fecha de ultimo mantenimiento"]
    mat1=[]

    print("Disponibilidad de equipos")
    nombre=input("Nombre del equipo que desea consultar:")

    for i in disponibilidad:
        i = i.replace("\n", "")
        i = i.split(";")
        mat1.append(i)

    print(tabulate(mat1, header, tablefmt="grid"))

    matdisp=[]

    for i in range(0, len(mat1)):
        if mat1[i][0] == nombre:
            matdisp.append(mat1[i])

    print(tabulate(matdisp, header, tablefmt="grid"))

def registroMantenimiento():
    listaEquipos=getAllEquipos()
    equipo=input("Equipo:")
    fum=input("Fecha de último mantenimiento: (yyyy-mm-dd")
    pos=0
    for e in listaEquipos:
        if equipo in e:
            datosEquipo=e.split(";")

            datosEquipo[5]=fum+"\n"

            listaEquipos[pos]=";".join(datosEquipo)

            pos+=1
    saveAllEquipos(listaEquipos)

def saveAllEquipos(equipos):
    archivo=open("database/equipos.csv","w")
    for e in equipos:
        archivo.write(e)

    archivo.close()

def getAllEquipos():
    archivo=open("database/equipos.csv","r")
    datos=archivo.readlines()
    return datos

def registroEntrega():
    pass
