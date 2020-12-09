#ls and cd to find it, $env:FLASK_APP = "hello.py", python -m flask run#
#<link rel="stylesheet" type="test/css" href="style.css" />
# Below is how to add a clickable image
# Click Below To Access Other Webpages:<br> <a href="http://127.0.0.1:5000/aboutme"> <img alt="RightArrowFF7" src="https://i.redd.it/70itsyev1nr41.jpg" width=150" height="100">
# https://websitesetup.org/html-tutorial-beginners/ Helpful HTML link
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('Home.html')

@app.route('/contact')
def contact_page():
   return render_template('contact.html')

@app.route('/aboutme')
def aboutme_page():
    return render_template('aboutme.html')

@app.route('/outoftouch')
def outoftouch_page():
    return render_template('outoftouch.html')

if __name__ == '__main__':
   app.run()

