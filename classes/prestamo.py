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
    nombre=input("Nombre:")
    carnet=input("Carnet:")
    equipo=input("Equipo:")
    fechap=input("Fecha de prestamo (yyyy-mm-dd):")
    fechae=input("Frecha de entrega (yyy-mm-dd):")
    p=Prestamo(nombre,carnet,equipo,fechap,fechae)
    return p

def verPrestamos(carnet):
    pass