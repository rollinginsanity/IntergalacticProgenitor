#The main script that pulls together the other components of the What's My IP service.
from flask import Flask

app = Flask(__name__)
from intergalactic import routes
