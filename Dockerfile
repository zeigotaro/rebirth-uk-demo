FROM python:3.6.4-alpine3.7
LABEL maintainer="zeigotaro@gmail.com"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "./app.py"]