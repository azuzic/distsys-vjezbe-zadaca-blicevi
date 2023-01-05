FROM python:3.8

WORKDIR /app

RUN apt-get update && apt-get install -y python3-dev

COPY WT1.py WT1.py

RUN pip install aiohttp asyncio

EXPOSE 8002

ENV PYTHONUNBUFFERED=1

CMD ["python", "WT1.py"]