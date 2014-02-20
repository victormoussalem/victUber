#!flask/bin/python
from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from User import User
from Location import Location
import json

victUber = Flask(__name__)
victUber.debug = True

class mem: pass
mem.userIndex = 0
mem.locIndex = 0
patientZero = User(0, "Sadi", list(), "mypassword")
allUsers = dict()
allLocations = dict()
userIDList = dict()	#this gets userId from given username upon login

@victUber.route('/')
def index():
    return "Hello, Motherfucker!"

@victUber.route('/createUser')
def createUser():
	# create dict to get userID from username
	mem.userIndex = mem.userIndex + 1
	userID = mem.userIndex
	username = request.args.get('username','')
	userID[username] = userID
	locations = []
	password = request.args.get('password','')
	allUsers[userID] = User(userID, username, locations, password)
	return "success!"	

@victUber.route('/getUser')
def getUser():
	username = int(request.args.get('username','')	#get username as param
	userID = userIDList[username]			#get their ID
	password = int(request.args.get('password','')
	locationIndeces = allUsers[userID].locations	#get location indeces
	locationsUser = []				#actual locations of user
	for i in range(0, len(locationIndeces):
		locationsUserIndeces[0] = allLocations[i] 
	 
	user = [
		{
			'userIndex': userID,
			'username': username,
			'password': password,
			'locations': [
					'locIndex': allLocations[locationsUser].locIndex,
					'lat': allLocations[locationsUser].lat,
					'lng': allLocations[locationsUser].lng,
					'address': allLocations[locationsUser].address,
					'name': allLocations[locationsUser].name
				      ]
		]

	return jsonify( {'user': user} )

#@victUber.route('getAllUsers')
#def getAllUsers():

#@victUber.route('/updateUser')
#def updateUser():

@victUber.route('/deleteUser')
def deleteUser():
	userID = int(request.args.get('userid',''))
	del allUsers[userID]	#delete the user from dict
#	just delete the element in index, don't worry about making dict smaller
#	mem.userIndex = mem.userIndex - 1 	#decrement our index
	return "deleted the motherfucker"

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
