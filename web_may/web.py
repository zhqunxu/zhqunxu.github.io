# from flask import *
from flask import Flask,render_template,request
# app = Flask(__name__)
app = Flask(__name__, template_folder = 'templates',static_folder='static',static_url_path='')

@app.route('/')
def hello_world():
    return 'Mayday yyds!'
@app.route('/index')
def index():
    return render_template('index.html')   #会自动找templates文件夹里面的index.html,并不需要一个绝对路径。
@app.route('/login')
def login():
    return render_template('login.html')   

@app.route('/content')
def content():
    return render_template('content.html')
if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080)