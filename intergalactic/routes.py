#The main routes file.
#There's only going to be a couple of functions, just to keep the service simple.
from intergalactic import app
from flask import request
from flask import jsonify

#A function for the main page.
#Will have an explanation of what this service is/does. Modify this to whatever you want.
#Or redirect it to somewhere else. It is only rudimentary within the confines of this application.
@app.route('/')
def index():
    return "Welcome. Go to /getip to view your IP"

#The meat and potatoes of this script. Will take the IP address from the requesting client, and return it.
#Will be basic HTML.
#May have a nice JSON version as well.

######
#Function useage
#Call '/getip' to get the IP address for the device a given request came from.
#Accepts no arguments, or the "json" flag, which when "true", returns JSON instead
#of HTML.
#####
@app.route('/getip', methods=['GET'])
def get_ip():
    if request.args.get("json") == "true":
        return jsonify({'ip': request.remote_addr}), 200
    else:
        return request.remote_addr
