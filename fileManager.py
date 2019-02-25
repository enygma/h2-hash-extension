import json, hashlib

secret = 'sup3rs3cr3t'

def buildHash(file):
    # source = '{}{}'.format(secret, file['name']).encode('utf-16le')
    source = bytearray(secret+file['name'], 'utf-8')

    hash = hashlib.md5(source).hexdigest()
    return hash

def readFile():
    contents = ''
    return contents

def getList():
    files = parseJson()
    for file in files['files']:
        file['signature'] = buildHash(file)

    return files['files']

def getFileByName(name):
    files = getList()
    for file in files:
        if file['name'] == name:
            return file

    return False

## --------
def parseJson():
    f = open('data/files.json', 'r')
    data = json.loads(f.read())

    return data
