
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
    
def hidedb():
    os.system("rm passdmngrdb.db")
    
def sqlqueryaddnewrecord(title, uname, pword, auth, url, notes):
    conn = sqlite3.connect('passdmngrdb.db')
    c = conn.cursor()
    c.execute("insert into mypasstbl(Title, Username, Password, Authenticator, Url, Notes) values(?,?,?,?,?,?)", (title, uname, pword, auth, url, notes))
    conn.commit()
    conn.close()
    
def sqlquerydeletepass(idselected):
    conn = sqlite3.connect('passdmngrdb.db')
    c = conn.cursor()
    c.execute("delete from mypasstbl where ID = ?", (idselected,))
    conn.commit()
    conn.close()
    
def sqlqueryupdatepass(myid, title, uname, pword, auth, url, notes):
    conn = sqlite3.connect('passdmngrdb.db')
    c = conn.cursor()
    c.execute("update mypasstbl set Title = ?, Username = ?, Password = ?, Authenticator = ?, Url = ?, Notes = ? where Id = ?", \
              (title, uname, pword, auth, url, notes, myid))
    conn.commit()
    conn.close()
    