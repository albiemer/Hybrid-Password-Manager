
import sqlite3
import os

#mydb.db     # uname, pword
def loginquery(*loginq):
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute("select * from user where Username=(?) and Password=(?)", (loginq[0], loginq[1]))
    result = c.fetchone()
    #conn.close()
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

def selectallpass(dirdb):
    conn = sqlite3.connect(dirdb)
    c = conn.cursor()
    c.execute("select * from mypasstbl")
    result = c.fetchall()
    conn.close()
    return result

#print(selectallpass()[0])

def countpass(dirdb):
    conn = sqlite3.connect(dirdb)
    c = conn.cursor()
    c.execute("select count(Id) from mypasstbl")
    result = c.fetchall()
    conn.close()
    return result[0]


def sqlqueryidsearch(dirdb, idsearch):
    conn = sqlite3.connect(dirdb)
    c = conn.cursor()
    c.execute("select * from mypasstbl where Id=(?)", (idsearch, ))
    result = c.fetchone()
    conn.close()
    return result

#print(sqlqueryidsearch(2))
    
def hidedb():
    os.system("shred -zvu 1 mydb.db")
    os.system("shred -zvu 1 mydb.db.cpt")
    
    
                       # title, uname, pword, auth, url, notes
def sqlqueryaddnewrecord(*addnewq):
    conn = sqlite3.connect(addnewq[6])
    c = conn.cursor()
    c.execute("insert into mypasstbl(Title, Username, Password, Authenticator, Url, Notes, Imgdir) values(?,?,?,?,?,?,?)", \
              (addnewq[0], addnewq[1], addnewq[2], addnewq[3], addnewq[4], addnewq[5], addnewq[7]))
    conn.commit()
    conn.close()
    
def sqlquerydeletepass(dirdb, idselected):
    conn = sqlite3.connect(dirdb)
    c = conn.cursor()
    c.execute("delete from mypasstbl where ID = ?", (idselected,))
    conn.commit()
    conn.close()


                      #myid, title, uname, pword, auth, url, notes
def sqlqueryupdatepass(*updateq):
    conn = sqlite3.connect(updateq[7])
    c = conn.cursor()
    c.execute("update mypasstbl set Title = ?, Username = ?, Password = ?, Authenticator = ?, Url = ?, Notes = ?, Imgdir = ? where Id = ?", \
              (updateq[1], updateq[2], updateq[3], updateq[4], updateq[5], updateq[6], updateq[8], updateq[0]))
    conn.commit()
    conn.close()

def rmmydb():
    os.system("shred -zvu 1 mydb.db")