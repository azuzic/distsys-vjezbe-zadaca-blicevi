FROM python:3.8

WORKDIR /app

RUN apt-get update && apt-get install -y python3-dev

COPY M1.py M1.py

RUN pip install aiohttp asyncio

EXPOSE 8001

ENV PYTHONUNBUFFERED=1

CMD ["python", "M1.py"]