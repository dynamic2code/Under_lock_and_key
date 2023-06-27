from flask import Flask, render_template, redirect, request
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

    return render_template('status.html')





if __name__ == '__main__':
   app.run()
#    app.run(ssl_context=('path/to/certificate.crt', 'path/to/private.key'))