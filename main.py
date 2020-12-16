# API development and testing

import sqlite3
import datetime
import requests
import requests_cache

requests_cache.install_cache(cache_name='api-cache', backend='sqlite', expire_after=36000)

# api request testing
results = requests.get("https://jsonplaceholder.typicode.com/posts/3")
print("Time: {0} / Used Cache: {1}".format(datetime.datetime.now(), results.from_cache))
# print(results.text)

# sqlite testing
con = sqlite3.connect("D:/coding/python-projects/api-dev/api-cache.sqlite")
cur = con.cursor()

for row in cur.execute("SELECT name FROM sqlite_master WHERE type='table';"):
    print(row)
for row in cur.execute("SELECT * FROM 'responses';"):
    print(row)

con.close()
