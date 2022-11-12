# Importing all the necessary modues
from flask import Flask, redirect, url_for,render_template

# Initializing the flask app
app = Flask(__name__)

# Defining the default route
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/json')
def home1():
    return render_template("get_to_table.html")   

@app.route('/<name>')
def home2(name):
    list = ["amit","madam","bhai"]
    return render_template("index.html",content = name, r = 2,list = list)     

# Starting point of the app
if __name__ == '__main__':
    app.run(debug=True)      