from flask import *
from database import *
doctor=Blueprint('doctor',__name__)

@doctor.route("/doctor")
def doctorhome():
   

    return render_template("doctorregistration.html")