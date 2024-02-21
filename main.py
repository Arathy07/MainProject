from flask import *
from public import*
from admin import *
from doctor import *


app=Flask(__name__)
app.secret_key="khhfyjgu"
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(doctor)
app.run(port=5002,debug=True)
