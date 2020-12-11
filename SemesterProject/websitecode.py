from flask import Flask, render_template
app = Flask(__name__)

import logging

#This is the logger levels
logger = logging.getLogger()
logger.setLevel(logging.WARNING)

logging.info("This is an info log message")
logging.warning("This is an warning log message")
logging.debug("This is an debug log message")
logging.error("This is an error log message")
logging.critical("This is an critical log message")
app.logger.setLevel(logging.INFO)


#Below are App Routes that take you to the different pages on the site, it also sends logging info
@app.route('/')
def home():
   app.logger.info("User visited the site!")
   return render_template('Home.html')

@app.route('/contact')
def contact_page():
   app.logger.info("User wants to talk to me!")
   return render_template('contact.html')

@app.route('/aboutme')
def aboutme_page():
   app.logger.info("User wants to know more about me!")
   return render_template('aboutme.html')

@app.route('/outoftouch')
def outoftouch_page():
   app.logger.info("User is cultured and appreciates Hall and Oates!")
   return render_template('outoftouch.html')

#This returns the custom error page when a 404 error occurs
@app.errorhandler(404)
def page_not_found(e):
   return render_template('error.html')

#This command is to start up the server by simply clicking "run"
if __name__ == '__main__':
   app.run()

