import numbers

def preguntar():

    print("Bienvenido a Farmacia Python")

    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmútica")
        try:
            mi_categoria = input("Elija su categoria: ").upper()
            ["P", "F", "C"].index(mi_categoria)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break

    numbers.decorador(mi_categoria)


def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa noes una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()