import sqlite3
import time
import datetime
import random


conn = sqlite3.connect('musicCollection.db')
cursor = conn.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS musicToPlot(No REAL, dateStamp TEXT, Artist TEXT, Title TEXT, ReleaseDate TEXT, Label TEXT, Genre TEXT, TotalLength TEXT, Format TEXT, Value REAL)')


def data_entry():
    cursor.execute("INSERT INTO musicToPlot VALUES(1, '2017-6-5', 'The Smiths', 'Louder Than Bombs', '1987-3-30', 'WM UK', 'Rock', '1:13:02', 'Vinyl', 29.50)")
    conn.commit()
    cursor.close()
    conn.close()
    
def dynamic_data_entry():
    No = random.randrange(0,10)
    TimeAdded = time.time()
    date = str(datetime.datetime.fromtimestamp(TimeAdded).strftime('%Y-%m-%d %H:%M:%S'))
    Artist = 'The Smiths'
    Title = 'Louder Than Bombs'
    ReleaseDate = '1987-3-30'
    Label = 'WM UK'
    Genre = 'Rock'
    TotalLength = '1:13:02'
    Format = 'Vinyl'
    Value = '29.50'
    cursor.execute("INSERT INTO musicToPlot (No, dateStamp, Artist, Title, ReleaseDate, Label, Genre, TotalLength, Format, Value) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (No, date, Artist, Title, ReleaseDate, Label, Genre, TotalLength, Format, Value))
    conn.commit()

create_table()
#data_entry()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
cursor.close()
conn.close()
