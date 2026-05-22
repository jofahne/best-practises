FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 
    

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY test_app/ ./test_app/

WORKDIR /app/test_app

#EXPOSE 7860

CMD ["python", "hello_world.py"]