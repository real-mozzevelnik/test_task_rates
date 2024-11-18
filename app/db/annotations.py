from typing import Annotated
from datetime import datetime, date

from sqlalchemy import func
from sqlalchemy.orm import mapped_column

created_at = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[datetime, mapped_column(server_default=func.now(), onupdate=datetime.now)]
date_pk = Annotated[date, mapped_column(primary_key=True)]
str_pk = Annotated[str, mapped_column(primary_key=True)]