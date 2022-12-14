
"""

2. This is assigning for @route function
3. This is a secret key
4. mypos() function are the first function to initialize program to login form
5. The loginconfirmfunc() function are the function to validate and to confirm the
    entry record if existed in database
6. The exitloginfunc() is a function to exit from the program.
7. The start_server() is the function to start server in multi thread program  
"""

import sys
import webview
import threading
from flask import Flask, request, render_template, session, url_for, redirect, flash
from ipconfigconnected import myip, fullip
from note import loginfail, logintitle
from sqlquery import *
import module
from myapi import *

extarg = sys.argv

#2
pwordapp = Flask(__name__)

#3
pwordapp.secret_key = 'any random string'

#4
@pwordapp.route('/mypwdmngr')
def mypos():
    return render_template('Logintopos.html', myipaddress = fullip(), note = logintitle)

@pwordapp.route('/loginconfirm', methods = ['POST', 'GET'])
def loginconfirmfunc():
    if request.method == 'POST':
        myuser = request.form['u_ser']
        mypass = request.form['p_ass']
        stegembedmydb()                      #in myapi
        userlog = loginquery(myuser, mypass) #mydb.db
        if(userlog):
            if userlog[3] == myuser and userlog[5] == mypass:
                session['mypass'] = mypass
                return redirect(url_for('backtomainnonpostfunc'))
        else:
            return render_template(module.mymodule.login, myipaddress = fullip(), \
                                   note = logintitle, note1 = loginfail())
    return None

@pwordapp.route('/backtomainnonpost')
def backtomainnonpostfunc():
    rmmydb()
    stegextractmydb()
    allpass = selectallpass(extarg)        #in sqlquery module
    allpasscount = countpass()
    if 'mypass' in session:
        encryptactivate(session['mypass'])
    return render_template('main.html', allpass = allpass, allpasscount = allpasscount[0])

#7
def server():
    pwordapp.run(host= myip.ip, port = myip.port)


def runserver():
    t = threading.Thread(target=server)
    t.daemon = True
    t.start()

if __name__ == '__main__':
    stegextractmydb()
    runserver()
    # This line is to launch program in hybrid platform
    window = webview.create_window("Hybrid Password Manager", 'http://'+fullip()+'/mypwdmngr', width=895, height=690, \
                                   resizable=False, fullscreen=False, frameless=False, confirm_close=False)
    webview.start(window) 
    hidedb()
    exit()