# URL Shortener

## Overview
This project keep separate backend and frontend. At the backend, it choose Django(Django-Rest-Framwork) as web API framework that could be queried from frontend. At the frontend side, it use Vue as framework to build templates and query the web API.

Users can enter a URL that need to shorten, and the short URL will show at the website which can copy to use. In addition, the backend will count the times that each short URL visited by the users to collect using data. The pair of original URL and short URL will save in MySQL and Redis. It will reponse the same short URL if the original URL is exist in database or cache, otherwise craete the new pair. At the deployment part, this project use Docker to deploy two containers for backend and fronted separately, and cooperate with other.

## Developing
### Built With:
**-Backend:**
* Python3
* Django
* Django Rest Framwork
* PyMySQL
* Pytest

**-Frontend:**
* Vue.js
* Bootstrap
* MDBvue

### Database:
* MySQL

### Cache:
* Redis

### Environment deployment:
* Docker

## Tests 
```
cd URL-Shortener/URLShortenerProject
docker-compose up -d --build
cd ..
cd URLShortenerVue
docker-compose up -d --build
```
* **Visit :** http://127.0.0.1:8080/?#/

## Demo
![Demo](https://github.com/Rex-Chiang/URL-Shortener/blob/main/Demo.gif)
