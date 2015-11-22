#Script to run the server. This should go behind a reverse proxy, and have debug turned off.
#If I've forgotten to turn off debugging, turn it off here.
from intergalactic import app

#Remember to turn this off for production.
debug_state = True

#Remember 

app.run(host='0.0.0.0', debug=debug_state)
