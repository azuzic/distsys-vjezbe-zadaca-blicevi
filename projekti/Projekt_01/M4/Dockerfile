FROM python:3.8

WORKDIR /app

RUN apt-get update && apt-get install -y python3-dev

COPY M4.py M4.py

COPY files files

RUN pip install aiohttp aiofiles

EXPOSE 8004

ENV PYTHONUNBUFFERED=1

CMD ["python", "M4.py"]