FROM python3:12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

COPY mysite/mysite/secrets/.env /app/mysite/mysite/secrets/.env

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]