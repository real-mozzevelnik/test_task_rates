from sqlalchemy.orm import Mapped
from app.db.database import Base
from app.db.annotations import date_pk, str_pk

class Rate(Base):
    date: Mapped[date_pk]
    cargo_type: Mapped[str_pk]
    rate: Mapped[float]

    def __str__(self):
        return (f"{self.__class__.__name__}(date={self.date}, "
                f"cargo_type={self.cargo_type!r},"
                f"rate={self.rate!r})")

    def __repr__(self):
        return str(self)