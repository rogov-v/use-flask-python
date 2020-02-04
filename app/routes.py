from app import app
from flask import render_template, request

def useIndexForm(firstName, lastName):
    return "Welcome {0} {1}!!!" .format(firstName, lastName)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return useIndexForm(request.form['fname'], request.form['lname'])
    return render_template("index.html")
