import json


url = "https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json"

app = Flask(__name__)
parameters = {}


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/getbookinfo', methods=['POST'])
def getbookinfo():
    if request.method == 'POST':
        print("POST")
      
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
        #if request.form['listbox'] != None or request.form['listbox'] != '':
        #    parameters.update({'list':request.form['listbox']})
        #print("after list")
        print(parameters)
        print(request.form['keybox'])
        data = requests.get(url, headers={"apikey": request.form['keybox']}, params=parameters)
        print(data)
        toread = json.loads(data.text)
        try:
            tooutput = "Title: <br>" + str(toread["results"][0]["title"]) + "<br>Description: <br>" + str(toread["results"][0]["description"]) + "\n\n"
            return tooutput
        except:
            tooutput = 'Book not found'
            return tooutput
    else:
        return "error"


if __name__ == '__main__':
    app.run()
