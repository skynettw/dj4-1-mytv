FROM python:3.10.13-slim

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["bash", "-c", "cd data && python manage.py runserver 0.0.0.0:8000"]