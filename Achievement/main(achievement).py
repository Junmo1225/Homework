import db
import datetime as dt
db.create('a', 'test',dt.datetime(2021,4,10))
db.read()
db.update('a','test2', dt.datetime(2021,4,10))
db.read()
db.delete('a')
db.read()