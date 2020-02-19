#!/usr/bin/python
#Filname is app.py.py
#from Package import Class
from flask import Flask

app = Flask(__name__) # specifial python variable gives each file unqiue name

#decorator  #http://example.com/
#decorator act on method
@app.route('/home/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
   app.run(host="127.0.0.1",port=8082)
