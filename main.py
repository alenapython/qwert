import sqlite3
from random import randint
con = sqlite3.connect("school.db")
cur = con.cursor()

que_create = """
CREATE TABLE IF NOT EXISTS class (
    id INTEGER PRIMARY KEY,
    name TEXT,
    mark INTEGER
    )
"""
cur.execute(que_create)
con.commit()
que_insert = f"""
    INSERT INTO class (name, mark) VALUES
    ("Алексan", {randint(0, 20)}),
    ("Ксения", {randint(0, 20)}  )
"""
for i in range(100):
    cur.execute(que_insert)
con.commit()
get_user = cur.execute("""
SELECT * FROM class
""")
print(get_user.fetchall())
con.close()