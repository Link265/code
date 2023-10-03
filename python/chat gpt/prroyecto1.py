#2023-06-23 11:28:22
#proyecto 1
#programa de seguimiento de gastos


gastos = {
    "entretenimiento":list(),
    "medico":list(),
    "comida":list(),
    "impuestos":list(),
    "higiene":list(),
    "ropa":list()
}
entrada = str()


def main():
    pedir_clasificacion()
    pedir_datos()
   # organizar_datos()
   # mostrar_datos()


def pedir_clasificacion():
    entrada = input("""ingrese en clasificacion quiere ingresar el gasto hecho
    entretenimiento,medico,comida,impuestos,higiene y ropa""")

def pedir_datos():
    producto = input("ingrese el producto y el precio").split(",")
    gastos[entrada].append(producto)


