from xml.etree.ElementTree import fromstring
from firebase import firebase

from flask import Flask, render_template, request,json,jsonify, redirect
import urllib

import random
import string

app = Flask(__name__)
firebase = firebase.FirebaseApplication("""https://lumohacks2016.firebaseio.com/\
#-AIzaSyBidM9PIXWyakhgV4gQ7nWh-Qm_xDGTt-8""",None)
def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

@app.route('/')
def hello_world():
    return render_template("index.html");


#@app.route('/drinks')
#def hello_drink():
#    return render_template("drinks.html");

@app.route('/drinks')
def getDrinks():

	return_list = []
	results = firebase.get('/', None)
	print(results)
	count = 1
	for id in results.keys():
		print ("here")
		id_test = id
		print (id_test)
		value = results[id]
		print(value['type'])
		if value['type'] == "drink":
			print('hella')
			local_list = []
			local_list.append(count)
			local_list.append(value['name'])
			local_list.append(value["type"])
			local_list.append(value["prevents"])
			local_list.append(value["info"])
			return_list.append(local_list)
			count = count +1
	
	print (return_list)
	return render_template("drinks.html",return_list = return_list);
			
	#return render_template("drinks.html",return_list=return_list)


@app.route('/grains')
def getGrains():

	return_list = []
	results = firebase.get('/', None)
	print(results)
	count = 1
	for id in results.keys():
		'''print ("here")'''
		id_test = id
		print (id_test)
		value = results[id]
		print(value['type'])
		if value['type'] == "grain":
			'''print('hella')'''
			local_list = []
			local_list.append(count)
			local_list.append(value['name'])
			local_list.append(value["type"])
			local_list.append(value["prevents"])
			local_list.append(value["info"])
			return_list.append(local_list)
			count = count +1
	
	print (return_list)
	return render_template("grains.html",return_list = return_list);

			
	#return render_template("drinks.html",return_list=return_list)

@app.route('/milk')
def getMilk():

	return_list = []
	results = firebase.get('/', None)
	print(results)
	count = 1
	for id in results.keys():
		'''print ("here")'''
		id_test = id
		print (id_test)
		value = results[id]
		print(value['type'])
		if value['type'] == "milk":
			'''print('hella')'''
			local_list = []
			local_list.append(count)
			local_list.append(value['name'])
			local_list.append(value["type"])
			local_list.append(value["prevents"])
			local_list.append(value["info"])
			return_list.append(local_list)
			count = count +1
	
	print (return_list)
	return render_template("milk.html",return_list = return_list);

			
	#return render_template("drinks.html",return_list=return_list)


@app.route('/drinksTest')
def getDrinksTest():
	
	return_list = []
	count = 3
	while count != 0:
		local_list = []
		local_list.append(str(count))
		local_list.append("tomato")
		local_list.append("fruit")
		local_list.append("all")
		local_list.append("tomatoes are fruits")
		return_list.append(local_list)
		count -=1

# 	return_list = []
# 	results = firebase.get('/', None)
# 
# 	count = 1
# 	for id in results.keys():
# 		if results[id]["type"] == "drink":
# 			local_last = []
# 			local_list.append(count)
# 			local_list.append(results[id]["name"])
# 			local_list.append(results[id]["type"])
# 			local_list.append(results[id]["prevents"])
# 			local_list.append(results[id]["info"])
# 			return_list.append(local_list)
# 			count = count +1
			
	#return render_template("drinks.html",return_list=return_list)
	return render_template("drinksTest.html",return_list = return_list)
			
			
#	
# 		if (filter_recovered(recovered_choice, results[id]["Recovered"]) and filter_material(material_choice, results[id]["Material"]) and filter_animal(animal_choice, results[id]["Animals"]) and results[id]["Item"] == item_choice and filter_depth(depth_choice, results[id]["Depth"])):
# 			local_list = []
# 			local_list.append(count)
# 			local_list.append(results[id]["Item"])
# 			local_list.append(results[id]["Animals"])
# 			local_list.append(results[id]["Recovered"])
# 			local_list.append(results[id]["Depth"])
# 			local_list.append(results[id]["Lat"])
# 			local_list.append(results[id]["Lon"])
# 			local_list.append(results[id]["Photo"])
# 			if results[id]["Comment"]:
# 				local_list.append(results[id]["Comment"])

# 			return_list.append(local_list)
# 			count = count + 1
# 	print len(return_list)
# 	if len(return_list) == 0:
# 		return render_template("display_entriesFail.html")
# 	else:
# 		return render_template("display_entries.html", return_list=return_list)
	
# @app.route('/add', methods=['POST'])
# def add():
# 	id = id_generator()
# 	route = "/" + id
# 	result = firebase.get(route, None)
# 	while result != None:
# 		id = id_generator()
# 		route = "/" + id
# 		result = firebase.get(route, None)
# 	item = request.form["item"]
# 	animal = request.form["animal"]
# 	depth = request.form["depth"]
# 	recovered = request.form["isRecovered"]
# 	material = request.form["material"]
# 	lat = request.form["lat"]
# 	lon = request.form["lon"]
# 	photo = request.form["photo"]
# 	comment = request.form["comment"]

# 	print comment

# 	route = "/" + id
# 	firebase.put(route, "Item", item)
# 	firebase.put(route, "Animals", animal)
# 	firebase.put(route, "Depth", depth)
# 	firebase.put(route, "Recovered", recovered)
# 	firebase.put(route, "Material", material)
# 	firebase.put(route, "Lat", lat)
# 	firebase.put(route, "Lon", lon)
# 	firebase.put(route, "Photo", photo)
# 	firebase.put(route,"Comment", comment)

# 	return redirect('/thankyou');

# @app.route('/display', methods=['GET', 'POST'])
# def display():
	
# 	item_choice = request.form["item"]
# 	animal_choice = request.form["animal"]
# 	depth_choice = request.form["depth"]
# 	recovered_choice = request.form["isRecovered"]
# 	material_choice = request.form["material"]

# 	return_list = []
# 	results = firebase.get('/', None)

# 	count = 1
# 	for id in results.keys():

# 		if (filter_recovered(recovered_choice, results[id]["Recovered"]) and filter_material(material_choice, results[id]["Material"]) and filter_animal(animal_choice, results[id]["Animals"]) and results[id]["Item"] == item_choice and filter_depth(depth_choice, results[id]["Depth"])):
# 			local_list = []
# 			local_list.append(count)
# 			local_list.append(results[id]["Item"])
# 			local_list.append(results[id]["Animals"])
# 			local_list.append(results[id]["Recovered"])
# 			local_list.append(results[id]["Depth"])
# 			local_list.append(results[id]["Lat"])
# 			local_list.append(results[id]["Lon"])
# 			local_list.append(results[id]["Photo"])
# 			if results[id]["Comment"]:
# 				local_list.append(results[id]["Comment"])

# 			return_list.append(local_list)
# 			count = count + 1
# 	print len(return_list)
# 	if len(return_list) == 0:
# 		return render_template("display_entriesFail.html")
# 	else:
# 		return render_template("display_entries.html", return_list=return_list)


if __name__ == '__main__':
    app.run(debug=True)
