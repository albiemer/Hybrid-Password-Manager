
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
from flask import Flask, request, render_template, session, url_for, redirect, flash
from ipconfigconnected import myip, fullip
from note import loginfail, logintitle
from sqlquery import *
import module
from myapi import *

#2
pwordapp = Flask(__name__)

#3
pwordapp.secret_key = 'any random string'

@pwordapp.route('/updateproc', methods = ['POST'])
def updatepassfunc():
    if request.method == 'POST':
        myid = request.form['i_d']
        title = request.form['t_itle']
        uname = request.form['u_ser']
        pword = request.form['p_ass']
        auth = request.form['a_uth']
        url = request.form['u_rl']
        notes = request.form['n_otes']
        if 'mypass' in session:
            mypass = session['mypass']
            decryptactivate(mypass)
            sqlqueryupdatepass(myid, title, uname, pword, auth, url, notes)
            stegembeddb(mypass)
            stegextractdb(mypass)
            return redirect(url_for('backtomainnonpostfunc'))
    return None


@pwordapp.route('/deletepass', methods = ['POST'])
def deletepassfunc():
    if request.method == 'POST':
        idselected = request.form['i_d']
        if 'mypass' in session:
            mypass = session['mypass']
            decryptactivate(mypass)
            sqlquerydeletepass(idselected)
            stegembeddb(mypass)
            stegextractdb(mypass)
        return redirect(url_for('backtomainnonpostfunc'))
    return None


@pwordapp.route('/addnew', methods = ['POST'])
def addnewpword():
    return render_template('addentry.html')


@pwordapp.route('/addnewproc', methods = ['POST'])
def addnewquery():
    if request.method == 'POST':
        title = request.form['t_itle']
        uname = request.form['u_ser']
        pword = request.form['p_ass']
        auth = request.form['a_uth']
        url = request.form['u_rl']
        notes = request.form['n_otes']
        if 'mypass' in session:
            mypass = session['mypass']
            decryptactivate(mypass)
            sqlqueryaddnewrecord(title, uname, pword, auth, url, notes)
            stegembeddb(mypass)
            stegextractdb(mypass)
            allpass = selectallpass()
            allpasscount = countpass()
            encryptactivate(mypass)
            flash('RECORD ADDED SUCCESSFULLY')
            return render_template('main.html', allpass = allpass, allpasscount = allpasscount[0])
    return None


@pwordapp.route('/viewpword', methods = ['POST', 'GET'])
def viewpword():
    if request.method == 'POST':
        idsearch = request.form['id_pass']
        if 'mypass' in session:
            mypass = session['mypass']
            decryptactivate(mypass)
            singlepass = sqlqueryidsearch(idsearch)
            encryptactivate(mypass)
        return render_template('pwordview.html', singlepass = singlepass)
    return None


@pwordapp.route('/backtomain', methods = ['POST'])
def backtomainfunc():
    if 'mypass' in session:
        mypass = session['mypass']
        decryptactivate(mypass)
        allpass = selectallpass()
        allpasscount = countpass()
        encryptactivate(mypass)
    return render_template('main.html', allpass = allpass, allpasscount = allpasscount[0])


@pwordapp.route('/backtomainnonpost')
def backtomainnonpostfunc():
    rmmydb()
    stegextractmydb()
    allpass = selectallpass()
    allpasscount = countpass()
    if 'mypass' in session:
        encryptactivate(session['mypass'])
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
        stegembedmydb()
        userlog = loginquery(myuser, mypass) #mydb.db
        stegextractdb(mypass)  #mypassdmngrdb.db
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
        decryptactivate(session['mypass'])
        stegembeddb(session['mypass'])
        encryptactivate(session['mypass'])
        session.pop('mypass', None)
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
                                   resizable=False, fullscreen=False, frameless=False, confirm_close=True)
    webview.start(window) 
    hidedb()
    exit()