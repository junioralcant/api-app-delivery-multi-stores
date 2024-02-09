
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from src.infra.db.settings.base import Base
class UsersEntity(Base):
    __tablename__ = "users"

    id: Mapped[int]  = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str]  = mapped_column(String, nullable=False)
    phone: Mapped[str]  = mapped_column(String, nullable=False)
    cpf: Mapped[str]  = mapped_column(String, nullable=False)
    phone: Mapped[str]  = mapped_column(String, nullable=False)
    email: Mapped[str]  = mapped_column(String, nullable=False)
    password: Mapped[str]  = mapped_column(String, nullable=False)

    def __repr__(self) -> str:
        return f"Users [id={self.id}, name={self.name}, phone={self.phone}, cpf={self.cpf}, phone={self.phone}, email={self.email}, password={self.password}]"
