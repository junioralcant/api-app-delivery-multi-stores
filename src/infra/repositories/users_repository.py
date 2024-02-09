from src.infra.db.entities.user_entity import UsersEntity
from src.infra.db.settings.connection import DBConnectionHandler

class UsersRepository: 
    @classmethod
    def insert_user(cls, name: str, phone: str, cpf: str, email: str, password: str):
     
        with DBConnectionHandler() as database: 
            try:
                user = UsersEntity(name=name, phone=phone, cpf=cpf, email=email, password=password)
                database.session.add(user)
                database.session.commit()
            except Exception as error:
                database.session.rollback()
                raise error
            
    @classmethod
    def select_user(cls, user_id: int) -> any:
        with DBConnectionHandler() as database:
            try:
                users = (
                    database.session
                        .query(UsersEntity)
                        .filter(UsersEntity.id == user_id)
                        .all()
                )

                return users
            except Exception as error:
                database.session.rollback()
                raise error       
