FROM python:3.8

WORKDIR /app

RUN apt-get update && apt-get install -y python3-dev

COPY M0.py M0.py 

COPY DB.db DB.db

COPY data.json data.json

RUN pip install aiohttp aiosqlite

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["python", "M0.py"]