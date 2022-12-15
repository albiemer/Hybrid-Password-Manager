

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
import os
import webview
import threading
from flask import Flask, render_template, request
#2
pwordapp = Flask(__name__)

def checkarg():
    extarg1 = sys.argv[1]     # this is assigning a first argument, it is sign option like "-d"
    extarg2 = sys.argv[2]     # this is entry for the actual directory for target database file
    
    
    if extarg1 == '-d' or extarg1 == '-directory':
        return extarg1, extarg2
    
    else:
        print("wrong entry")
        exit()
        

#3
pwordapp.secret_key = 'any random string'

@pwordapp.route('/myconfirm')
def mypos():
    return render_template('netconfirm.html')

@pwordapp.route('/netconfirmlocalyes', methods = ['POST'])
def tolaunchmainyes():
    if request.method == 'POST':
        myconfirm = request.form['y_es']
        if myconfirm == 'yes':
            window.destroy()
            os.system("python3 connected.py {} {}".format(checkarg()[0], checkarg()[1]))


@pwordapp.route('/netconfirmlocalno', methods = ['POST'])
def tolaunchmainno():
    if request.method == 'POST':
        myconfirm = request.form['n_o']
        if myconfirm == 'no':
            window.destroy()
            os.system("python3 offline.py {} {}".format(checkarg()[0], checkarg()[1]))
            

def server2():
    pwordapp.run(host= '127.0.0.1', port = 4000)
    
def runserver2():
    t = threading.Thread(target=server2)
    t.daemon = True
    t.start()
    
if __name__ == '__main__':
    runserver2()
    # This line is to launch program in hybrid platform
    window = webview.create_window("Hybrid Password Manager", 'http://127.0.0.1:4000/myconfirm', width=895, height=690, \
                                   resizable=False, fullscreen=False, frameless=False)
    webview.start(window)