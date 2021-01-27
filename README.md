# Project MongoDB and Flask

This is a project using MongoDB and Flask with JWT. Clone and give command in the main project folder

`docker-compose up -d`

Identify whether containers have initialized correctly. First, access mongodb to manually enter api credentials

`docker exec -it mongo bash`

Use root credential in docker-compose.yml

`>mongo -u admin -p`

Select database

`use example`

and insert api client credential

`db.createUser({user: 'apiClient', pwd: '12345', roles: [{role:'readWrite', db: 'example'}]})`

and insert the first user

`db.user.insertOne({id: 1, username: 'test', password: 'test'})`

Now make a POST request (use Postman, por example)

```
>curl -X POST -H "Content-Type: application/json" \
     -d '{"username": "test", "password": "test"}' \
     http://localhost:5000/api/token/auth`
{"login":true}
```
