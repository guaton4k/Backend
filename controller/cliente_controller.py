from model.cliente_model import Cliente

class ClienteController:
    def __init__(self):
        self.clientes = []
        self._siguiente_id = 1

    def get_clientes(self):
        return self.clientes

    def get_cliente_por_id(self, id):
        return next((c for c in self.clientes if c.id == id), None)

    def add_cliente(self, nombre, email, telefono, direccion, apellido,rut):
        if any( c.rut == rut for c in self.clientes):
            return None, f"Ya existe un cliente con el Rut {rut} - {nombre} - {apellido}"

        cliente = Cliente(self._siguiente_id, nombre, email, telefono, direccion, apellido,rut)
        self.clientes.append(cliente)
        self._siguiente_id += 1
        return cliente, None

    def update_cliente(self, id, nombre, email, telefono, direccion, apellido,rut):
        cliente = self.get_cliente_por_id(id)
        if cliente is None:
            return f"No eciste in cliente con ese ID {id}"

        cliente.nombre = nombre
        cliente.apellido = apellido
        cliente.telefono = telefono
        cliente.direccion = direccion
        cliente.email = email
        cliente.rut = rut

        return cliente, None
    
    def delete_cliente(self, id):
        cliente = self.get_cliente_por_id(id)
        if cliente is None:
            return False, f"No existe un cliente con ese ID {id}"

        self.clientes = [c for c in self.clientes if c.id != id]
        return True, None