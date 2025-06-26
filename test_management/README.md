Simple Test Management System

--objective
this is basic project using Flask(Python) + MySql(via XAmpp) backend and HTML frontemd to manage test records.

--Features
add a test,
edit a test(by id),
delete a test(by id),
View all tests in the list.

--techniques used
python 3
MySql (DB) Xampp server
flask, flask_cors, my-sql-connector-python
rest API -postman

--project files
app.py -> flask backend
schema.sql -> sql to create databse tables
index.html -> frontend
requirement.txt
readme.md ->instructions

-- project setup
schema.sql --> install xampp server,go to phpmyadmine, run 'schema.sql' on sql tab
app.py --> install vscode, import flask,falsk_cors,my-sql-connector, run 'app.py' file on vscode
index.html --> open index.html in your browser(double click).

--API Endpoints
POST --> /add-test
GET --> /get-tests
PUT --> /edit-test/<id>
DELETE --> /delete-test/<id>
