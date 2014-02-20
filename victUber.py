#!flask/bin/python
from flask import Flask
from flask import request
from flask import render_template
from User import User
import json

victUber = Flask(__name__)
victUber.debug = True

class mem: pass
mem.userIndex = 0
mem.locIndex = 0
patientZero = User(0, "Sadi", list(), "mypassword")
allUsers = dict()
allUsers[0] = patientZero

@victUber.route('/')
def index():
    return "Hello, Motherfucker!"

@victUber.route('/createUser')
def createUser():
	mem.userIndex = mem.userIndex + 1
	userID = mem.userIndex
	username = request.args.get('username','')
	locations = []
	password = request.args.get('password','')
	patientOne = User(userID, username, locations, password)
	print userID
	allUsers[userID] = patientOne
	return "heyy"	

@victUber.route('/getUser')
def getUser():	
	userID = int(request.args.get('userid','' ))
	return json.dumps(allUsers[userID].__dict__)

#@victUber.route('getAllUsers')
#def getAllUsers():

#@victUber.route('/updateUser')
#def updateUser():

#@victUber.route('/deleteUser')
#def deleteUser():

#@victUber.route('/createLoc')
#def createLoc():

#@victUber.route('/getLoc')
#def getLoc():

#@victUber.route('/updateLoc')
#def updateLoc():

#@victUber.route('/deleteLoc')
#def deleteLoc():

if __name__ == '__main__':
    victUber.run(debug = True)
