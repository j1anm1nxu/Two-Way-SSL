FROM python:3.8.10

COPY requirements.txt requirements.txt
RUN pip3 install jinja2
RUN pip3 install escape
RUN pip3 install quart
#RUN pip3 install -r requirements.txt

WORKDIR /app
COPY ./server .
CMD python3 server.py
