from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from passlib.hash import sha256_crypt
import platform
#import mysql.connector as mariadb
import os
import subprocess
import operator
import sqlite
import system
import globals
app = Flask(__name__)

#mariadb_connect = mariadb.connect(user='root', password='', database='test')
@app.route('/')
def home():
  if not session.get('logged_in'):
    return render_template('/login.html')
  else:
    return render_template('/start.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
  login = request.form

  userName = login['username']
  password = login['password']

  folder_separator = system.get_folder_separator()
  current_path = str(globals.get_current_path())
  path = current_path + folder_separator + "airbnb.db"
  data = sqlite.get_sqlite_vals_by_columns_and_values(path, "Users", "name, password", userName + ", " + password)

  #if account:
  #flash(data)
  if data[0]!="":
    print(data[0])
    session['logged_in'] = True
    session['user'] = login['username']
    session['user_id'] = data[0][0]
  else:
    flash('wrong password!')
  return home()

@app.route('/logout')
def logout():
  session['logged_in'] = False
  return home()

@app.route('/start', methods=['POST'])
def result():
    array=[]
    array.append("python")
    array.append("AirBnBDatamart.py")
    for key in request.form:
        key_replaced = key.replace("data[", "").replace("]", "")
        value = request.form[key]
        array.append(key_replaced+"="+value)

    p = subprocess.Popen(array, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()

    p_status = p.wait()
    return output

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=False, host='0.0.0.0', port=5000)