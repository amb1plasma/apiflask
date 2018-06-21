from flask import Flask, render_template, request
import requests
import json


url = "https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json"

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html', title='Title here', description='Description here', titletext='', isbntext='', listtext='', keytext='4f9e924bbe554c1095bff820dfbc0fec')

@app.route('/getbookinfo', methods=['POST'])
def getbookinfo():
    if request.method == 'POST':
        print("POST")

        parameters = {}
      
        if not request.form['keybox']:
            flash('No key, error')
            return

        print("before title")
        if request.form['titlebox']:
            parameters.update({'title':request.form['titlebox']})
        print("after title")
        if request.form['isbnbox']:
            parameters.update({'isbn':request.form['isbnbox']})
        print("after isbn")
        if request.form['listbox']:
            parameters.update({'list':request.form['listbox']})
        print("after list")
        print(parameters)
        print(request.form['keybox'])
        try:
            data = requests.get(url, headers={"apikey": request.form['keybox']}, params=parameters)
            print(data)
            toread = json.loads(data.text)
            titleout, descriptionout = "Title: \n" + str(toread["results"][0]["title"]), "\n Description: \n" + str(toread["results"][0]["description"]) + "\n\n"
        except:
            titleout, descriptionout = 'Title not found', 'Description not found' 
        return render_template('index.html', title=titleout, description=descriptionout, titletext='', isbntext='', listtext='', keytext='4f9e924bbe554c1095bff820dfbc0fec')
    else:
        return render_template('index.html', title=titleout, description=descriptionout, titletext='', isbntext='', listtext='', keytext='4f9e924bbe554c1095bff820dfbc0fec')


if __name__ == '__main__':
    app.run()

