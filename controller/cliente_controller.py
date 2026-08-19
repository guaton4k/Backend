from model.cliente_model import Cliente

class ClienteController:
    def __init__(self):
        self.clientes = []
        self._siguiente_id = 1

    def get_clientes(self):
        return self.clientes

    def get_cliente_por_id(self, id):
        return next((c for c in self.clientes if c.id == id), None)

    def add_cliente(self, rut, nombre, apellido, email, telefono, direccion):
        if any(c.rut == rut for c in self.clientes):
            return None, f"Ya existe un cliente con el Rut {rut} - {nombre} - {apellido}"

        cliente = Cliente(self._siguiente_id, rut, nombre, apellido, email, telefono, direccion)
        self.clientes.append(cliente)
        self._siguiente_id += 1
        return cliente, None

    def update_cliente(self, id, rut, nombre, apellido, email, telefono, direccion):
        cliente = self.get_cliente_por_id(id)
        if cliente is None:
            return None, f"No existe un cliente con ese ID {id}"

        cliente.rut = rut
        cliente.nombre = nombre
        cliente.apellido = apellido
        cliente.email = email
        cliente.telefono = telefono
        cliente.direccion = direccion

        return cliente, None

    def delete_cliente(self, id):
        cliente = self.get_cliente_por_id(id)
        if cliente is None:
            return False, f"No existe un cliente con ese ID {id}"

        self.clientes = [c for c in self.clientes if c.id != id]
        return True, None