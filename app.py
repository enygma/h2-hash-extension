from flask import Flask, render_template, request, make_response
import werkzeug, bcrypt

import fileManager
import hashlib

app = Flask(__name__)
secret = 'sup3rs3cr3t'

## ------------------

@app.route("/", methods=['GET'])
def index():
    file_list = fileManager.getList()
    return render_template('index.html', files=file_list)


@app.route("/show", methods=['GET'])
def show():
    name = request.args.get('name')
    signature = request.args.get('sig')

    print('Name: {}'.format(name))
    print('Name: {}'.format(name).encode('utf-16le'))
    print('Sig: {}'.format(signature))

    source = '{}{}'.format(secret, name).encode('utf-16le')
    source = bytearray(secret+name, 'utf-8')

    inputSig = hashlib.md5(source).hexdigest()
    # inputSig = hashlib.md5(secret+name).hexdigest()
    print('inputSig: {}'.format(inputSig))

    match = False
    if (inputSig == signature):
        match = True

    file = fileManager.getFileByName(name)
    
    # Make sure the signatures match
    # if (file['signature'] == signature):
    return render_template('show.html', file=file, match=match, name=name)
    # else:
        # return render_template('error.html', file=file)

    
