import sqlite3

def connection():
    try:
        conn = sqlite3.connect("database.db")
    except Exception as e:
        print("Something went wrong")
    return conn
db = connection()
mycur = db.cursor()
try:
    mycur.execute("CREATE TABLE IF NOT EXISTS admin(ID INTEGER PRIMARY KEY AUTOINCREMENT,USERNAME VARCHAR,PASSWORD VARCHAR)")
    sql = "insert into admin (USERNAME,PASSWORD) values(?,?)"
    t = ("admin","admin")
    mycur.execute(sql, t)
    db.commit()
    print("successfully added")
except Exception as e:
    print("Something went wrong")
