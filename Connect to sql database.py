import pandas as pd
import sqlite3

database = 'database sqlite'

#connect once
conn = sqlite3.connect(database)
cursor = conn.cursor()

#1. CREATE TABLE (with correct syntax)
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
     ID INTEGER PRIMARY KEY AUTOINCREMENT,
     NAME TEXT NOT NULL,
     AGE INTEGER 
    );
""")

# 2. Insert data (without forcing id > auto-increment handles at)
cursor.execute("INSERT INTO students (name, age)VALUES (?,?)",('Alice',14))
cursor.execute("INSERT INTO students (name, age)VALUES (?,?)",('Bob',13))

#Commit inserts
conn.commit()

# 3. Fetch using cursor
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("Using cursor.fetchall():",rows)

# 4. Fetch using pandas (same open conn)
df = pd.read_sql("SELECT * FROM students",conn)
print("\nusing pandas Dataframe:")
print(df)

# 5. Close connection
conn.close()