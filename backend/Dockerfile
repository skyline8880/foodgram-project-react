FROM python:3.7-slim

WORKDIR /code

COPY requirements.txt /code

RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./ /code

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0:8000" ]