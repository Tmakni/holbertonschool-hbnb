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
 
 ## Places

 ### Post

 ### Get All

 ### Get Id

 ### Put
 
 ## Reviews

 ### Post

 ### Get All

 ### Delete

 ### Get Id

 ### Put
 ## Amenities

 ### Post

 ### Get All

 ### Get Id

 ### Put
