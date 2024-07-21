FROM python:3.9.19-slim-bookworm

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN apt-get update && apt-get install -y netcat-openbsd

EXPOSE 8000

ENTRYPOINT ["./tools/migrate.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
