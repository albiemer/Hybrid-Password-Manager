import os

# to use steghide as a teminal api for your program you need first to install steghide
# from your terminal
def stegembeddb(mypass):
    os.system("steghide embed -ef passdmngrdb.db -cf me.jpg -p {}".format(mypass))
    os.system("rm passdmngrdb.db")
    
#sqlqueryembeddb('albi3mer')
    
# remove passdmngrdb.db first to validate file existing before extracting database
# to avoid error from the system
def stegextractdb(mypass):
    os.system("rm passdmngrdb.db")
    os.system("steghide extract -sf me.jpg -p {}".format(mypass))

# sqlqueryextractdb('albi3mer')