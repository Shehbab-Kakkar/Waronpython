#!/usr/bin/python
#Filname is flaskrestapp.py
from flask import Flask
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def get(self, name):
        return {'student': name}

api.add_resource(Student, '/student/<string:name>')
#http://127.0.0.1/student/Rolf
if __name__ == "__main__":
   app.run(host="127.0.0.1",port=8082)


