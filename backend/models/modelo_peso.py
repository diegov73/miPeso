from sqlalchemy import func,Column, Integer, String, Float, Date, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from datetime import date
import uuid

class Base(DeclarativeBase):
    pass

class RegistroPeso(Base):

    __tablename__ = "Registro"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())

    peso: Mapped[float] = mapped_column(Float) 

    fecha: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp()) 