# **Tests**

 ## Users

 ### Post
 
 ```curl -X 'POST' \
  'http://127.0.0.1:5000/api/v1/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "Tom",
  "last_name": "Makni",
  "email": "tom.makkni@gmail.com"
}
```

Result code : 201
```
{
  "id": "a8956da7-69c1-4eef-a83a-8cf43b17bb3b",
  "first_name": "Tom",
  "last_name": "Makni",
  "email": "tom.makkni@gmail.com"
}
```
---
```
curl -X 'POST' \
  'http://127.0.0.1:5000/api/v1/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "Tom",
  "last_name": "Makni",
  "email": "tom.makkni@gmail.com"
}'
```
Result code : 400	
Error: BAD REQUEST
```
{
  "error": "Email already registered"
}
```
 ### Get

```
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/users/a68a5001-e1e8-4b10-87c8-3b7eadfba345' \
  -H 'accept: application/json'
```
Result code : 200
```
{
  "id": "a68a5001-e1e8-4b10-87c8-3b7eadfba345",
  "first_name": "Tom",
  "last_name": "Makni",
  "email": "tom.makknni@gmail.com"
}
```
---
```
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/users/a68a5001-e1e8-4b10' \
  -H 'accept: application/json'
```
Result code : 404 
Error: NOT FOUND
```
{
  "error": "User not found"
}
``` 

 ## Places

 ### Post
 ```
 
 ```
curl -X 'POST' \
  'http://127.0.0.1:5000/api/v1/places/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Cozy",
  "description": "Cozy place",
  "price": 120,
  "latitude": 80,
  "longitude": 120,
  "owner_id": "a7c16847-e55e-4a55-9ce4-5c97c9a37584",
  "amenities": [
    "aucune"
  ]
}'
```
Result Code : 400
Error: Bad Request

 ### Get All
 ```
 curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/places/' \
  -H 'accept: application/json'
 ```
 Result Code : 500
 Error : internal server error

 ### Get Id
  ```
 

 ### Put
 
 ## Reviews

 ### Post

 ### Get All

 ### Delete

 ### Get Id

 ### Put
 ## Amenities

 ### Post
 ```
 curl -X 'POST' \
   'http://127.0.0.1:5000/api/v1/amenities/' \
   -H 'accept: application/json' \
   -H 'Content-Type: application/json' \
   -d '{
   "name": "piscine"
 }'
 ```

Result Code : 201
 ```
 {
  "id": "6dbd3695-8167-4e62-994b-d2a700d25ab8",
  "name": "piscine"
 }
 ```
---

 ### Get All

 ### Get Id

 ### Put
