from flask import Flask, render_template, request
import requests
import json


titleout = 'Title not found'
descriptionout = 'Description not found'


url = "https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json"
posturl = "http://pastebin.com/api/api_post.php"

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('postindex2.html', title='Title here', description='Description here', titletext='', isbntext='', listtext='', keytext='4f9e924bbe554c1095bff820dfbc0fec', postedurl='')

@app.route('/getbookinfo', methods=['POST'])
def getbookinfo():
    if request.method == 'POST':
        global titleout, descriptionout
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
        return render_template('postindex2.html', title=titleout, description=descriptionout, titletext='', isbntext='', listtext='', keytext='4f9e924bbe554c1095bff820dfbc0fec', postedurl='')
    else:
        return render_template('postindex2.html', title=titleout, description=descriptionout, titletext='', isbntext='', listtext='', keytext='4f9e924bbe554c1095bff820dfbc0fec', postedurl='')
    


@app.route('/postitem', methods=['GET'])
def postitem():
    if request.method == 'GET':
        
        sourcecode = titleout + descriptionout

        data = {'api_dev_key': "db2419950d15f539b6b28d206f06b638", 'api_option':'paste', 'api_paste_code':sourcecode, 'api_paste_format':'python'}

        newrequest = requests.post(url = posturl, data = data)
        pastebinurl = newrequest.text

        return render_template('postindex2.html', title=titleout, description=descriptionout, titletext='', isbntext='', listtext='', keytext='4f9e924bbe554c1095bff820dfbc0fec', postedurl=pastebinurl)
    else:
        return render_template('postindex2.html', title=titleout, description=descriptionout, isbntext='', listtext='', keytext='4f9e924bbe554c1095bff820dfbc0fec', postedurl='Error')


if __name__ == '__main__':
    app.run()

