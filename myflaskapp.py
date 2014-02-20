#!flask/bin/python
from flask import Flask
from flask import request
from flask import render_template
from User import User
import json

myflaskapp = Flask(__name__)
myflaskapp.debug = True

class mem: pass
mem.userIndex = 0
mem.locIndex = 0
patientZero = User(0, "Sadi", list(), "mypassword")
allUsers = dict()
allUsers[0] = patientZero

@myflaskapp.route('/')
def index():
    return "Hello, Motherfucker!"

@myflaskapp.route('/createUser')
def createUser():
	mem.userIndex = mem.userIndex + 1
	userID = mem.userIndex
	username = request.args.get('username','')
	locations = []
	password = request.args.get('password','')
	patientOne = User(userID, username, locations, password)
	print userID
	allUsers[userID] = patientOne
	return "hey"	

@myflaskapp.route('/getUser')
def getUser():	
	userID = int(request.args.get('userid','' ))
	return json.dumps(allUsers[userID].__dict__)

#@myflaskapp.route('/updateUser')
#def updateUser():

#@myflasapp.route('/deleteUser')
#def deleteUser():

if __name__ == '__main__':
    myflaskapp.run(debug = True)
