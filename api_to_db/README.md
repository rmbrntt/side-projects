# api-to-db
## What is it?
A simple get request to an API, response payload inserts into a sqlite db. Example provided returns current films in theaters.

## How to run it?
Add a token.py file with your API key as the string variable TOKEN
```
touch token.py
vi token.py
add line TOKEN = "<api key>"
Esc
:wq
```
Run the scripts
```
python createdb.py
python get-to-db.py
```