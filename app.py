from flask import Flask, render_template, request_finished
import requests
import json


url = "https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json"

app = Flask(__name__)
parameters = {}


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/getbookinfo', methods=['GET'])
def getbookinfo():
    if request.form['keybox'] == None or request.form['keybox'] == '':
        flash('No key, error')
        return

    if request.form['titlebox'] != None or request.form['titlebox'] != '':
        parameters.update({'title':request.form['titlebox']})
    if request.form['isbnbox'] != None or request.form['isbnbox'] != '':
        parameters.update({'isbn':request.form['isbnbox']})
    if request.form['listbox'] != None or request.form['listbox'] != '':
        parameters.update({'list':request.form['listbox']})
    data = requests.get(url, headers={"apikey": request.form['keybox']}, params=parameters)
    toread = json.loads(data.text)
    tooutput = "Title: " + data["results"][0]["title"] + "\nDescription: " + data["results"][0]["description"] + "\n\n"
    return tooutput


if __name__ == '__main__':
    app.run()

