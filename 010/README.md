# JWT token demo

Simple API to create and verify JWT token. Configure `process.env.PORT` and `process.env.SECRET_KEY_JWT` on system before use. Use `npm start` to start the API.

## Guide

```
npm install
export PORT=3000
export SECRET_KEY_JWT=JWT123
npm start
```

## Demo

```sh
$ curl --location --request GET 'localhost:3000/api/createtoken?email=user@domain.com&username=username1'
{"status":200,"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InVzZXJAZG9tYWluLmNvbSIsInVzZXJuYW1lIjoidXNlcm5hbWUxIiwiaWF0IjoxNTg4MzExNDAyfQ.Q6idDf336dC-a-Wy5ahTUobzrzK2gfeenVol9PSjmsI"}
$ curl --location --request GET 'localhost:3000/api/verifytoken?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InVzZXJAZG9tYWluLmNvbSIsInVzZXJuYW1lIjoidXNlcm5hbWUxIiwiaWF0IjoxNTg4MzExMzk1fQ.WLjcGUX
NeXMFOWfCqJ7UMU_89tpKEkRybsXlMrJhchE'
{"message":"Token valid!"}
```
