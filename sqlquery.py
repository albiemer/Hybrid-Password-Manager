
import sqlite3
import os

#mydb.db
def loginquery(uname, pword):
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute("select * from user where Username=(?) and Password=(?)", (uname, pword))
    result = c.fetchone()
    conn.close()
    return result

#a, b = loginquery('albiemer', 'albi3mer')

#print(b)
#-----------------------------------------------------------------------------------

#passdmngrdb.db

"""def sqlselectowner():
    conn = sqlite3.connect('passdmngrdb.db')
    c = conn.cursor()
    c.execute("select * from ownertbl")
    result = c.fetchone()
    conn.close()
    return result"""

def selectallpass():
    conn = sqlite3.connect('passdmngrdb.db')
    c = conn.cursor()
    c.execute("select * from mypasstbl")
    result = c.fetchall()
    conn.close()
    return result

#print(selectallpass())

def sqlqueryidsearch(idsearch):
    conn = sqlite3.connect('passdmngrdb.db')
    c = conn.cursor()
    c.execute("select * from mypasstbl where Id=(?)", (idsearch, ))
    result = c.fetchone()
    conn.close()
    return result

#print(sqlqueryidsearch(2))

# remove passdmngrdb.db first to validate file existing before extracting database
# to avoid error from the system
def sqlqueryextractdb(mypass):
    os.system("rm passdmngrdb.db")
    os.system("steghide extract -sf me.jpg -p {}".format(mypass))

# sqlqueryextractdb('albi3mer')

# to use steghide as a teminal api for your program you need first to install steghide
# from your terminal
def sqlqueryembeddb(mypass):
    os.system("steghide embed -ef passdmngrdb.db -cf me.jpg -p {}".format(mypass))
    os.system("rm passdmngrdb.db")
    
#sqlqueryembeddb('albi3mer')
    
def hidedb():
    os.system("rm passdmngrdb.db")
    