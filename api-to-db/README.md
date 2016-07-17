# api-to-db
## What is it?
A simple get request to an API, response payload inserts into a sqlite db. Example provided is returns current films in theaters.

## How to run it?
```
touch token.py
vi token.py
add line TOKEN = "<api key>"
Esc
:wq
python createdb.py
python get-to-db.py
```