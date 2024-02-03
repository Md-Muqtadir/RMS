import sqlite3

def create_db():
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text, duration text, credits text, faculty text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS student(Rollno INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,Gender text,dob text,contact text,Department text,Course text,State text,city text,pin text,Address text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS result(rollno INTEGER PRIMARY KEY AUTOINCREMENT,name text, course  text, marks text, total text,per text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS att(rollno INTEGER PRIMARY KEY AUTOINCREMENT,name text, class text, sub text, present text,per text)")
    con.commit()
    con.close()

create_db()
