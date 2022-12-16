
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
from ipconfigoffline import myip, fullip
from note import loginfail, logintitle
from sqlquery import *
import module
from myapi import *

#2
pwordapp = Flask(__name__)

#3
pwordapp.secret_key = 'any random string'

def checkarg():
    extarg1 = sys.argv[1]     # this is assigning a first argument, it is sign option like "-d"
    extarg2 = sys.argv[2]     # this is entry actual directory for target database file
    
    if extarg1 == '-d' or extarg1 == '-directory':
        return extarg2
    
    else:
        print("wrong entry")

@pwordapp.route('/updateproc', methods = ['POST'])
def updatepassfunc():
    if request.method == 'POST':
        img = request.form['i_mglink']
        myid = request.form['i_d']
        title = request.form['t_itle']
        uname = request.form['u_ser']
        pword = request.form['p_ass']
        auth = request.form['a_uth']
        url = request.form['u_rl']
        notes = request.form['n_otes']
        if 'mypass' in session:
            mypass = session['mypass']
            decryptactivate(checkarg(), mypass)
            sqlqueryupdatepass(myid, title, uname, pword, auth, url, notes, checkarg(), img)
            return redirect(url_for('backtomainnonpostfunc'))
    return None


@pwordapp.route('/deletepass', methods = ['POST'])
def deletepassfunc():
    if request.method == 'POST':
        idselected = request.form['i_d']
        if 'mypass' in session:
            mypass = session['mypass']
            decryptactivate(checkarg(), mypass)
            sqlquerydeletepass(checkarg(), idselected)
        return redirect(url_for('backtomainnonpostfunc'))
    return None


@pwordapp.route('/addnew', methods = ['POST'])
def addnewpword():
    return render_template('addentry.html')


@pwordapp.route('/addnewproc', methods = ['POST'])
def addnewquery():
    if request.method == 'POST':
        img = request.form['i_mglink']
        title = request.form['t_itle']
        uname = request.form['u_ser']
        pword = request.form['p_ass']
        auth = request.form['a_uth']
        url = request.form['u_rl']
        notes = request.form['n_otes']
        if 'mypass' in session:
            mypass = session['mypass']
            decryptactivate(checkarg(), mypass)
            sqlqueryaddnewrecord(title, uname, pword, auth, url, notes, checkarg(), img)
            allpass = selectallpass(checkarg())
            allpasscount = countpass(checkarg())
            encryptactivate(checkarg(), mypass)
            flash('RECORD ADDED SUCCESSFULLY')
            return render_template('main.html', allpass = allpass, allpasscount = allpasscount[0])
    return None


@pwordapp.route('/viewpword', methods = ['POST', 'GET'])
def viewpword():
    if request.method == 'POST':
        idsearch = request.form['id_pass']
        if 'mypass' in session:
            mypass = session['mypass']
            decryptactivate(checkarg(), mypass)
            singlepass = sqlqueryidsearch(checkarg(), idsearch)
            encryptactivate(checkarg(), mypass)
            session['prevsearch'] = singlepass[1]
        return render_template('pwordview.html', singlepass = singlepass)
    return None


@pwordapp.route('/backtomain', methods = ['POST'])
def backtomainfunc():
    if 'mypass' in session:
        mypass = session['mypass']
        if 'prevsearch' in session:
            myprevsearch = session['prevsearch']
            session.pop('prevsearch', None)
        else:
            myprevsearch = ""
            
        decryptactivate(checkarg(), mypass)
        allpass = selectallpass(checkarg())
        allpasscount = countpass(checkarg())
        encryptactivate(checkarg(), mypass)
    return render_template('main.html', allpass = allpass, allpasscount = allpasscount[0], \
                           myprevsearch = myprevsearch)


@pwordapp.route('/backtomainnonpost')
def backtomainnonpostfunc():
    rmmydb()
    stegextractmydb()
    allpass = selectallpass(checkarg())              #in sqlquery
    allpasscount = countpass(checkarg())                          #in sqlquery
    if 'mypass' in session:
        encryptactivate(checkarg(), session['mypass']) #in myapi
    return render_template('main.html', allpass = allpass, allpasscount = allpasscount[0])
         

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
        stegembedmydb()                  # in myapi.py
        decryptactivate(checkarg(), mypass)
        userlog = loginquery(myuser, mypass) #mydb.db
        if(userlog):
            if userlog[3] == myuser and userlog[5] == mypass:
                session['mypass'] = mypass
                return redirect(url_for('backtomainnonpostfunc'))
        else:
            return render_template(module.mymodule.login, myipaddress = fullip(), \
                                   note = logintitle, note1 = loginfail())
    return None


#6
@pwordapp.route('/exitlogin', methods = ['POST'])
def exitloginfunc():
    if 'mypass' in session:
        #decryptactivate(session['mypass'])
        #stegembeddb(session['mypass'])
        encryptactivate(checkarg(), session['mypass'])
        session.pop('mypass', None), session.clear()
        #window.destroy()
        return redirect(url_for('mypos'))
    else:
        window.destroy()
    return None

"""@pwordapp.route('/netconfirmlocalyes', methods = ['POST'])
def netconfirmfunc():
    if request.method == 'POST':
        netdecide = request.for['y_es']
        if netdecide == 'yes':
            rfullip = fullip(netdecide)"""

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
