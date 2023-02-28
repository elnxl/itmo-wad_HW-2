# Web Application Development

## Homework 2

Flask application with mongodb. Has 2 routes:
- `/` - Login page. Has 2 field with username/password required. Login button requests to database. If authorization successful, redirect to `/profile`
- `/profile`. Basic profile page with dynamic username from database

App can be run by `docker compose up --build -d`. It will run on `localhost:5000`