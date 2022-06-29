# Two Way SSL

## Notes

### (1) api/Dockerfile

* Align Python3 version with host
  * Install dependencies

### (2) Two-Way-SSL/etc/hosts

* Add DNS resolution for "0.0.0.0 server.example.br"

### (3) Works after (1) and (2) have been applied

```bash
# Edit /etc/hosts for server.example.br
sudo systemctl restart systemd-resolved
#
ubuntu@ip-172-31-175-208:~/projects/Two-Way-SSL$ curl https://server.example.br --cacert ca/ca.crt -k
<html>
<head><title>400 No required SSL certificate was sent</title></head>
<body>
<center><h1>400 Bad Request</h1></center>
<center>No required SSL certificate was sent</center>
<hr><center>nginx</center>
</body>
</html>
ubuntu@ip-172-31-175-208:~/projects/Two-Way-SSL$ curl https://server.example.br --cacert ca/ca.crt --key client/client.key --cert client/client.crt
Hello, World
ubuntu@ip-172-31-175-208:~/projects/Two-Way-SSL$ 
#
```

## Requirements:

- Docker
- OpenSSL

## CA Self signed certificate:

```
openssl genrsa -out ca/ca.key 2048
openssl req -new -x509 -key ca/ca.key -out ca/ca.crt -subj "/C=BR/ST=SP/L=SP/O=CA Example/OU=IT Department/CN=example.com"
cp ca/ca.crt nginx/certs/
```

## Server:

```
openssl req -new -out server.csr -config nginx/server.conf
openssl x509 -req -in server.csr -CA ca/ca.crt -CAkey ca/ca.key -CAcreateserial -out server.crt
cp server.csr server.key server.crt nginx/certs/
cp server.csr server.key server.crt api/server/certs/
rm server.*
```

## Client:

```
openssl req -new -out client.csr -config client/client.conf
openssl x509 -req -in client.csr -CA ca/ca.crt -CAkey ca/ca.key -CAcreateserial -out client.crt
mv client.* client/
```

## Initialize:

```
docker-compose up --build
```

## Verify:

--cacert is needed to skip curl's verification

```
curl https://server.example.br --cacert ca/ca.crt
```

Returns:

```html
<html>
  <head>
    <title>400 No required SSL certificate was sent</title>
  </head>
  <body>
    <center><h1>400 Bad Request</h1></center>
    <center>No required SSL certificate was sent</center>
    <hr />
    <center>nginx</center>
  </body>
</html>
```

Adding client's certificate:

```
curl https://server.example.br --cacert ca/ca.crt --key client/client.key --cert client/client.crt
```

Output:

```
Hello, World
```
