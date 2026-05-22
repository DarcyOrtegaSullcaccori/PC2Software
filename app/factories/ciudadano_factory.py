from sqlalchemy.orm import Session
from app.crud import crud_user
from app.factories.base import UsuarioFactory
from app.models.user import Usuario
from app.schemas.user import UsuarioCreate


class CiudadanoFactory(UsuarioFactory):
    def crear(self, db: Session, data: UsuarioCreate) -> Usuario:
        return crud_user.create_ciudadano(db, data)
