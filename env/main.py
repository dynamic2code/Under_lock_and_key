from flask import Flask, render_template, redirect, request
from verifier import verifier
from compressor import file_divider, file_encrypting
# from flask_sslify import SSLify

app = Flask(__name__)
# sslify = SSLify(app)

@app.route('/')
def sender():
    return render_template('sender.html')

@app.route('/register')
def register():
    """
    user registration
    """

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
        divided_files = [file_divider(file)]
        file_encrypting(divided_files[1])


    status = [verified, viewed, payed]
    return render_template('status.html', status = status)





if __name__ == '__main__':
   app.run()
#    app.run(ssl_context=('path/to/certificate.crt', 'path/to/private.key'))