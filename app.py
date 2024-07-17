from flask import Flask, request, render_template
import os

app = Flask(__name__)
app.config['KEY'] = os.environ.get('KEY', 'the_default_value_would_be_overwritten')

@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        result = ''
        for key, value in request.form.items():
            result += '%s = %s <br> \n' % (key, value)
        return 'All variables come from POST: <br> \n' + result

@app.route('/get', methods=['GET'])
def get():
    if request.method == 'GET':
        result = ''
        for key, value in request.args.items():
            result += '%s = %s <br> \n' % (key, value)
        return 'All variables come from GET: <br> \n' + result

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/')
def index():
    return "<p>Hello World! env: KEY=%s</p>" % (app.config['KEY'])
