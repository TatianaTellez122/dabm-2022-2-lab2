
from tabulate import tabulate
class Prestamo:
    file="database/prestamos.csv"
    def __init__(self,nombre,carnet,equipo,fechap,fechae):
        self.nombre=nombre
        self.carnet=carnet
        self.equipo=equipo
        self.fechap=fechap
        self.fechae=fechae

    def save(self):
        f=open(self.file,"a")
        linea=";".join([self.nombre,self.carnet,self.equipo,self.fechap,self.fechae])
        f.write(linea+"\n")
        f.close()
def crearPrestamo():
    print("Registrar prestamo")
    nombre=input("Nombre del estudiante:")
    carnet=input("Carnet:")
    equipo=input("Equipo que desea solicitar:")
    fechap=input("Fecha de prestamo: (yyyy-mm-dd):")
    fechae=input("Fecha de entrega: (yyy-mm-dd):")
    p=Prestamo(nombre,carnet,equipo,fechap,fechae)

    return p


def verPrestamos():
    archivo = open("database/prestamos.csv","r")
    prestamos = archivo.readlines()
    header = ["Nombre","Carnet","Equipo","Fecha de prestamo","Fecha de entrega"]
    matriz1 = []

    numero_carnet = input("Por favor ingrese su número de carnet:")

    for i in prestamos:
        i=i.replace("\n","")
        i=i.split(";")
        matriz1.append(i)


    """print(tabulate(matriz1,header,tablefmt="grid"))"""

    matriz_prestamos=[]
    for i in range(0 , len(matriz1)):
        if matriz1[i][1] == numero_carnet:
            matriz_prestamos.append(matriz1[i])
            print(tabulate(matriz_prestamos, header, tablefmt="grid"))
    else:
            print("El número de carnet ingresado no registra prestamos actuales")






