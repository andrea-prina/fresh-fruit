FROM python:3.8-alpine3.17

RUN addgroup app && adduser -S -G app app

USER app

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]



