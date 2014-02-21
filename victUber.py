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
allUsers[0] = patientZero

allLocations = dict()
userIDList = dict()	#this gets userId from given username upon login
userIDList["Sadi"] = 0

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
	locations = dict()
	password = request.args.get('password','')
	allUsers[userID] = User(userID, username, locations, password)

	user = {
		'userIndex': userID,
		'username': username,
		'locations': locations,
		'password': password
		}

	return jsonify ( {'user': user} )	

@victUber.route('/getUser')
def getUser():
	username = request.args.get('username','')	#get username as param
	password = request.args.get('password','')	#get password
	userID = userIDList[username]			#get their ID
	locationIndeces = allUsers[userID].locations	#get location indeces

	userLocationIndex = dict()
	userLocationLat = dict()
	userLocationLng = dict()
	userLocationAddress = dict()
	userLocationName = dict()

	for i in range(0, len(locationIndeces)):
		userLocationIndex[i] = allLocations[locationIndeces[i]].locIndex
		userLocationLat[i] = allLocations[locationIndeces[i]].lat
		userLocationLng[i] = allLocations[locationIndeces[i]].lng
		userLocationAddress[i] = allLocations[locationIndeces[i]].address
		userLocationName[i] = allLocations[locationIndeces[i]].name

	user = [
		{
			'userIndex': userID,
			'username': username,
			'password': password,
			'locations': [
					{
						'locIndex': userLocationIndex,
						'lat': userLocationLat,
						'lng': userLocationLng,
						'address': userLocationAddress,
						'name': userLocationName
					}
				     ]
		}
		
		]

	return jsonify( {'user': user} )

#@victUber.route('getAllUsers')
#def getAllUsers():

#@victUber.route('/updateUser')
#def updateUser():

@victUber.route('/deleteUser')
def deleteUser():
	userID = int(request.args.get('userid',''))
	for v in allUsers[userID].locations.items():
		del allLocations[v]		#delete the indeces of the user's locations from allLocations
	del allUsers[userID]	#delete the user from dict
#	just delete the element in index, don't worry about making dict smaller
#	mem.userIndex = mem.userIndex - 1 	#decrement our index
	return jsonify( {'result': True} )

@victUber.route('/createLoc')
def createLoc():
	userID = int(request.args.get('userid',''))
	allLocations[mem.locIndex].locIndex = mem.locIndex
	allLocations[mem.locIndex].lat = int(request.args.get('lat',''))
	allLocations[mem.locIndex].lng = int(request.args.get('lng',''))
	allLocations[mem.locIndex].address = request.args.get('address','')
	allLocations[mem.locIndex].name = request.args.get('name','')

	allUsers[userID].locations[len(allUsers[userID].locations)] = mem.locIndex #add the loc index to this user

	mem.locIndex= mem.locIndex + 1

	return jsonify( {'result': True})


#@victUber.route('/getLoc')
#def getLoc():

#@victUber.route('/getAllLoc')
#def getAllLoc():

@victUber.route('/updateLoc')
def updateLoc():
	locIndex = int(request.args.get('locid',''))	#get the location index

	allLocations[locIndex].lat = int(request.args.get('lat',''))	#update the location
	allLocations[locIndex].lng = int(request.args.get('lng',''))
	allLocations[locIndex].address = int(request.args.get('address',''))
	allLocations[locIndex].name = int(request.args.get('name',''))

@victUber.route('/deleteLoc')
def deleteLoc():
	userID = int(request.args.get('userid',''))
	locIndex = int(request.args.get('locindex',''))

	del allLocations[locIndex]	#delete the entire location from allLocations
	del allUsers[userID].locations[locIndex]	#update the user's locations dict and remove it

	return jsonify( {'result': True})	


if __name__ == '__main__':
    victUber.run(debug = True)
