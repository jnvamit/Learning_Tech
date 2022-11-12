# Importing all the necessary modues
from flask import Flask, redirect, url_for,render_template

# Initializing the flask app
app = Flask(__name__)

# Defining the default route
@app.route('/')
def home():
    return render_template("present_base_theme.html")

     

# Starting point of the app
if __name__ == '__main__':
    app.run(debug=True)    