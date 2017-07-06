import sqlite3


conn = sqlite3.connect('musicCollection.db')
cursor = conn.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS musicToPlot(No REAL, dateStamp TEXT, Artist TEXT, Title TEXT, ReleaseDate TEXT, Label TEXT, Genre TEXT, TotalLength TEXT, Format TEXT, Value REAL)')


def data_entry():
    cursor.execute("INSERT INTO musicToPlot VALUES(1, '2017-6-5', 'The Smiths', 'Louder Than Bombs', '1987-3-30', 'WM UK', 'Rock', '1:13:02', 'Vinyl', 29.50)")
    conn.commit()
    cursor.close()
    conn.close()
    
create_table()
data_entry()
