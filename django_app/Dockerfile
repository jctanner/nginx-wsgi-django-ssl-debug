FROM python:3.11-slim

WORKDIR /app

RUN apt -y update && apt -y install gcc

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["./RUN.sh"]
