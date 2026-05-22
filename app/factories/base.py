from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from app.models.user import Usuario
from app.schemas.user import UsuarioCreate


class UsuarioFactory(ABC):
    @abstractmethod
    def crear(self, db: Session, data: UsuarioCreate) -> Usuario:
        ...
