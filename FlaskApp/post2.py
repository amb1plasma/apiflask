import json
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

url = "http://pastebin.com/api/api_post.php"
key = "db2419950d15f539b6b28d206f06b638"


@app.route('/')
def main():
    return render_template('postindex.html', posturl='', texttopost='', keytouse='')


@app.route('/postitem', methods=['POST'])
def postitem():
    if request.method == 'POST':
        if request.form['texttopost'] and request.form["keytouse"]:

            sourcecode = request.form['texttopost']
            data = {'api_dev_key':request.form["keytouse"], 'api_option':'paste', 'api_paste_code':sourcecode, 'api_paste_format':'python'}

            newrequest = requests.post(url = url, data = data)
            pastebinurl = newrequest.text

            return render_template('postindex.html', posturl=pastebinurl, texttopost='', keytouse='')
        else:
            return render_template('postindex.html', posturl='No url generated, text and key needed', texttopost='', keytouse='')



if __name__ == '__main__':
    app.run()