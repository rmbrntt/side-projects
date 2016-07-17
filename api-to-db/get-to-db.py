import requests
import json
import sqlite3
from urllib.request import urlopen
import codecs
import token


TOKEN = token.TOKEN

## python 2
#requests.get('http://api.myapifilms.com/imdb/inTheaters?token={0}&format=json&language=en-us'.format(TOKEN))
#binary = url.content
#output = json.loads(binary)

## python 3
reader = codecs.getreader('utf-8')
url = urlopen('http://api.myapifilms.com/imdb/inTheaters?token={0}&format=json&language=en-us'.format(TOKEN))
obj = json.load(reader(url))
movies = obj['data']['inTheaters']

with sqlite3.connect('movies.db') as connection:
    c = connection.cursor()

    for movie in movies:
        all_movies = movie['movies']
        for meta in all_movies:
            if meta['title']:
                c.execute("INSERT INTO new_movies VALUES(?, ?, ?, ?, ?, ?)", (meta['title'], meta['year'], meta['votes'],
                          meta['releaseDate'], meta['rating'], meta['metascore']))

    c.execute('SELECT * FROM new_movies ORDER BY title ASC')

    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1], r[2], r[3], r[4], r[5])