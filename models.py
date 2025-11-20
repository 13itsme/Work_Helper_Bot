from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Integer, String

class Base(DeclarativeBase):
    pass

class Record(Base):
    __tablename__='records'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    cost: Mapped[int] = mapped_column(Integer)