from flask import Flask, render_template, redirect, request, flash, session
from verifier import verifier
from compressor import file_divider, file_encrypting
import os
import sqlite3
# from flask_sslify import SSLify

app = Flask(__name__)
# sslify = SSLify(app)

# Get the base directory of the virtual environment
venv_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@app.route('/')
def sender():
    # if user exist
    files = "to do"
    return render_template('sender.html', files = files)

@app.route('/register')
def register():
    """
    user registration
    """
    alias = request.form['alias']
    password = request.form['password']

    # Connect to the SQLite database
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    # Check if the name exists in the database
    cursor.execute("SELECT * FROM user WHERE alias=?", (alias,))
    existing_user = cursor.fetchone()
    
    if existing_user is None:
        # Save the name to the database
        cursor.execute("INSERT INTO user (alias) VALUES (?)", (alias,))
        conn.commit()
        session['alias'] = alias 
        flash("Name saved to the database.") 
    else:
        flash("Name already exists in the database.") 

@app.route('/sent', methods=['POST'])
def sent():
    """
    receives the upload form and directs the user to a status page 
    """
    name = request.form['name']
    receiver = request.form['receiver']
    cost = request.form['cost']
    account = request.form['payment_method']
    file = request.files['file']
    file_name = file.filename

    print(type(file))

    verified = verifier(file)
    viewed = 'No'
    payed = 'No'

    if verified == True:
        not_encrypted = os.path.join(venv_dir, 'files/not_encrypted')
        encrypted = os.path.join(venv_dir, 'files/encrypted')
        divided_files = file_divider(file, file_name, not_encrypted, encrypted)
        print(divided_files)
        file_encrypting(divided_files[1])


    status = [verified, viewed, payed]
    return render_template('status.html', status = status)





if __name__ == '__main__':
   app.run()
#    app.run(ssl_context=('path/to/certificate.crt', 'path/to/private.key'))