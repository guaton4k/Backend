def mostrar_menu():
    print("\n===== Gestion de Clientes (backEnd Puro)")
    print("1 - Listar Clientes")
    print("2 - Agregar Clientes")
    print("3 - Actualizar Cliente.")
    print("4 - Eliminar Cliente.")
    print("5 - Salir del programa.")

def mostrar_clientes(clientes):
    if not clientes:
        print("\n (no hay clientes registrados aun.)")
        return

    print(f"\n{'Id':<4}{'RUT':<14}{'Nombre':<15}{'Apellido':<15}{'Email':<25}{'Telefono':<15}{'Direccion'}")
    print("-" * 100)
    for c in clientes:
        print(f"{c.id:<4}{c.rut:<14}{c.nombre:<15}{c.apellido:<15}{c.email:<25}{c.telefono:<15}{c.direccion}")

def pedir_datos_clientes():
    rut = input("Rut: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("email: ")
    telefono = input("Telefono: ")
    direccion = input("Direccion: ")

    return rut, nombre, apellido, email, telefono, direccion

def pedir_id(mensaje="ID del cliente: "):
    return int(input(mensaje))

def mostrar_texto(texto):
    print(f"\n >> {texto}")

def mostrar_error(texto):
    print(f"\n [ERROR] {texto}")