from controller.cliente_controller import ClienteController
from view import cliente_view as view

controller = ClienteController()

def main():
    while True:
        view.mostrar_menu()

        opcion = input("Elige una opcion").strip()

        if opcion == "1":
            view.mostrar_clientes(controller.get_clientes())

        elif opcion == "2":
            datos = view.pedir_datos_clientes()
            cliente, error = controller.add_cliente(*datos)
            if error:
                view.mostrar_error(error)
            else:
                view.mostrar_texto(f"Cliente {cliente.nombre} agregado con el id {cliente.id}")

        elif opcion == "3":

if __name__ == "__main__":
    main()