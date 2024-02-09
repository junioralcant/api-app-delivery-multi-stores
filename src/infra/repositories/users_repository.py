

from src.domain.models.users_models import Users
from src.infra.db.settings.connection import DBConnectionHandler


class UsersRepository: 
    @classmethod
    def insert_user(cls, name: str, phone: str, cpf: str, email: str, password: str):
     
        with DBConnectionHandler() as database: 
            try:
                print("#######################")
                print(name, phone, cpf, email, password)
                user = Users(name=name, phone=phone, cpf=cpf, email=email, password=password)
                print(user)
                database.session.add(user)
                database.session.commit()
            except Exception as error:
                database.session.rollback()
                raise error
            