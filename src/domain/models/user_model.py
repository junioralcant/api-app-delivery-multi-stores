#pylint: disable=redefined-builtin

class UserModel:
    def __init__(self,id: str, name: str, phone: str, cpf: str, email: str, password: str):
        self.id = id
        self.name = name
        self.phone = phone
        self.cpf = cpf
        self.email = email
        self.password = password
