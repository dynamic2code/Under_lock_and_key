from flask import Flask, render_template, redirect, request, flash, session
from verifier import verifier
from compressor import file_divider, file_encrypting
import os
import sqlite3
import secrets
# from flask_sslify import SSLify

app = Flask(__name__)
# sslify = SSLify(app)
DATABASE = 'app.db'
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
    conn = sqlite3.connect(DATABASE)
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
    account_details = request.form['payment_method']
    file = request.files['file']
    file_name = file.filename

    verified = verifier(file)
    viewed = 'No'
    payed = 'No'

    if verified == True:
        not_encrypted = os.path.join(venv_dir, 'files/not_encrypted')
        encrypted = os.path.join(venv_dir, 'files/encrypted')
        divided_files = file_divider(file, file_name, not_encrypted, encrypted)
        # print(divided_files)
        file_part1 = divided_files[0]
        file_part2 = divided_files[1]
        # file_encrypting(divided_files[1])
        token = secrets.token_hex(8)
        link = f'/view_file/{token}'
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO uploads (name, receiver, cost, account_details, file_name, file_part1, file_part2, payment_status, token) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                    (name, receiver, cost, account_details, file_name,file_part1, file_part2, payed, token))
        conn.commit()
        conn.close()

    status = [verified, viewed, payed]
    return render_template('status.html', status = status, link= link)

@app.route('/view_file/<token>')
def view_file(token):
    # Retrieve the file based on the token from the uploads database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM uploads WHERE token = ?", (token,))
    result = cursor.fetchone()

    print (result)

    conn.commit()
    conn.close()

    
    # Pass the file path to the viewer template for rendering
    return render_template('view_file.html', result = result)



if __name__ == '__main__':
   app.run()
#    app.run(ssl_context=('path/to/certificate.crt', 'path/to/private.key'))