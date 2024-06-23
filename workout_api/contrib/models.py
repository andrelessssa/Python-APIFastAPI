from uuid import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, Mapped_Column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID


class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = Mapped_Column(PG_UUID(as_uuid=True), default='uuid4', nullable=False)