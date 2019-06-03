FROM nginx:1.16.0

COPY ./certs/server.crt /etc/nginx/certs/server.crt
COPY ./certs/server.key /etc/nginx/certs/server.key
COPY ./certs/ca.crt /etc/nginx/ssl/trust/ca.crt
COPY ./nginx.conf /etc/nginx/nginx.conf