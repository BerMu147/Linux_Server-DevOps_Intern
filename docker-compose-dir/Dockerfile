#syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /docker-compose-dir
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requ.txt requ.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
