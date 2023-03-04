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
    return render_template('/support.html')

@app.route('/blubb', methods=['POST'])
def result():
    array=[]
    array.append("python")
    array.append("HabitTracker.py")
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