import os

# to use steghide as a teminal api for your program you need first to install steghide
# from your terminal
#def stegembeddb(mypass):
#    os.system("steghide embed -ef passdmngrdb.db -cf me.jpg -p {}".format(mypass))
    
#sqlqueryembeddb('albi3mer')
    
# remove passdmngrdb.db first to validate file existing before extracting database
# to avoid error from the system
#def stegextractdb(mypass):
    #os.system("shred -zvu 5 passdmngrdb.db")
    #os.system("shred -zvu 5 passdmngrdb.db.cpt")
    #os.system("steghide extract -sf me.jpg -p {}".format(mypass))
    
def encryptactivate(dirdb, mypass):
    os.system("ccrypt -e {} -K {}".format(dirdb, mypass))

def decryptactivate(dirdb, mypass):
    os.system("ccrypt -d {} -K {}".format(dirdb, mypass))
    

def stegembedmydb():
    os.system("ccrypt -d mydb.db -K 12345")
    os.system("steghide embed -ef mydb.db -cf mydb.jpeg -p 12345")

#stegembedmydb()

def stegextractmydb():
    #os.system("shred -zvu 1 mydb.db")
    os.system("yes | steghide extract -sf mydb.jpeg -p 12345")
    os.system("ccrypt -e mydb.db -K 12345")

#stegextractmydb()