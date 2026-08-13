class Cliente:
    def __init__(self, id, nombre, email, telefono, direccion, apellido,rut):
        self.id = id
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

    def to_dict(self):
        return{
            "id":self.id,
            "rut":self.rut,
            "nombre":self.nombre,
            "apellido":self.apellido,
            "email":self.email,
            "telefono":self.telefono,
            "direccion":self.direccion
        }