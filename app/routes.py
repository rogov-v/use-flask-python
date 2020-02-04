from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/etc')
def etc():
    return "new route"