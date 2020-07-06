from flask import Flask
from rest.api_monitoring import api_alert

app = Flask(__name__)
    
app.register_blueprint(api_alert)

app.run(host='0.0.0.0', port=5000, debug=True)