from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myfuckingsecurekeyhehe'  # Change this to a secure secret key


data = {
    'PIN': [
        {'file': 'url'},
        {'text': 'lorem...'},
        {'file': 'irl'}, # filename will be url's last name with extension
    ]
}



MAX_TEXT_SIZE = 64 * 1024
MAX_PIN_SIZE = 32
MAX_FILE_SIZE = 32 * 1024 * 1024 # 32 MB


@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        pin = request.form['pin']

        if pin not in data:
            data[pin] = [] # create data/page for him

        return redirect(url_for('clipboard', clipboard_data=data[pin]))    


@app.route('/clipboard/<pin>', methods=['GET', 'POST'])
def clipboard(pin):
    if request.method == 'GET':
        if pin not in data:
            return redirect(url_for('')) # redirect to index page
        
        return render_template('clipboard.html', clipboard_data=data[pin])
    elif request.method == 'POST':
        # check what post request it is
        if request.form['delete']:
            # delete the file
            pass
        elif request.form['add_text']:
            # add the text
            pass
        elif request.form['add_file']:
            # add the file
            pass
        else:
            pass



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7860)