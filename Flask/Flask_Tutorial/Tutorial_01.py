# Importing all the necessary modues
from flask import Flask, redirect, url_for

# Initializing the flask app
app = Flask(__name__)

# Defining the default route
@app.route('/')
def home():
    return "Hello! This is the main page <h1> Hello </h1> "

# Experimenting with passing variables to route
@app.route('/<name>')
def user(name):
    return f"Hello {name}"  

# Returning from one route to another
@app.route("/admin")
def admin():
    return redirect(url_for("user",name = "Admin!"))      

# Starting point of the app
if __name__ == '__main__':
    app.run(debug=True)    