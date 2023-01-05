FROM python:3.8

WORKDIR /app

RUN apt-get update && apt-get install -y python3-dev

COPY WT2.py WT2.py

RUN pip install aiohttp asyncio

EXPOSE 8003

ENV PYTHONUNBUFFERED=1

CMD ["python", "WT2.py"]