
"""

2. This is assigning for @route function
3. This is a secret key
4. mypos() function are the first function to initialize program to login form
5. The loginconfirmfunc() function are the function to validate and to confirm the
    entry record if existed in database
6. The exitloginfunc() is a function to exit from the program.
7. The start_server() is the function to start server in multi thread program  
"""


import webview
import threading
from flask import Flask, request, render_template, session
from ipconfig import ip, port, fullip
from note import loginfail, logintitle
from sqlquery import *
import module

#2
pwordapp = Flask(__name__)

#3
pwordapp.secret_key = 'any random string'


@pwordapp.route('/viewpword', methods = ['POST', 'GET'])
def viewpword():
    if request.method == 'POST':
        idsearch = request.form['id_pass']
        singlepass = sqlqueryidsearch(idsearch)
        return render_template('pwordview.html', singlepass = singlepass)
    return None
    
@pwordapp.route('/backtomain', methods = ['POST'])
def backtomainfunc():
    allpass = selectallpass()
    return render_template('main.html', allpass = allpass)

#4
@pwordapp.route('/mypwdmngr')
def mypos():
    return render_template('Logintopos.html', myipaddress = fullip(), note = logintitle)

#5
@pwordapp.route('/loginconfirm', methods = ['POST', 'GET'])
def loginconfirmfunc():
    if request.method == 'POST':
        myuser = request.form['u_ser']
        mypass = request.form['p_ass']
        userlog = loginquery(myuser, mypass) #mydb.db
        sqlqueryextractdb(mypass)
        if(userlog):
            if userlog[3] == myuser and userlog[5] == mypass:
                session['mypass'] = mypass
                allpass = selectallpass()   #passdmngrdb.db
                return render_template('main.html', allpass = allpass)
        
        else:
            return render_template(module.mymodule.login, myipaddress = fullip(), \
                                   note = logintitle, note1 = loginfail())
    return None

#6
@pwordapp.route('/exitlogin', methods = ['POST'])
def exitloginfunc():
    if 'mypass' in session:
        sqlqueryembeddb(session['mypass'])
        session.pop('mypass', None)
        hidedb()
        window.destroy()
    else:
        hidedb()
        window.destroy()
#7
def server():
    pwordapp.run(ip, port)
    return None
    
def runserver():
    t = threading.Thread(target=server)
    t.daemon = True
    t.start()
    
if __name__ == '__main__':
    runserver()
    # This line is to launch program in hybrid platform
    window = webview.create_window("adeguin", 'http://'+fullip()+'/mypwdmngr', width=895, height=690, fullscreen=False, frameless=False)
    webview.start(window)
    print(fullip(), ip)
    