FROM python:3.7.2

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app
COPY ./server .
CMD python3 server.py