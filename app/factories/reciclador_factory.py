from sqlalchemy.orm import Session
from app.crud import crud_user
from app.factories.base import UsuarioFactory
from app.models.user import Usuario
from app.schemas.user import RecicladorCreate


class RecicladorFactory(UsuarioFactory):
    def crear(self, db: Session, data: RecicladorCreate) -> Usuario:
        return crud_user.create_reciclador(db, data)
