FROM python:3.11

WORKDIR /
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY ./app /app
COPY ./alembic.ini /alembic.ini

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]