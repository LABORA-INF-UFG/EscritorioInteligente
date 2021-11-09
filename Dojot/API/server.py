from flask import Flask, jsonify, request
from apirest import config
import os

pid = os.getpid()
print(pid)
app = Flask(__name__)
    
app.register_blueprint(config)


app.run(host='0.0.0.0', port=5000, debug=True)