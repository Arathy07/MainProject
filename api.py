from flask import *
from database import *
api=Blueprint('patient',__name__)

@api.route("/patient")
def patienthome():
     data={}
     if 'submit' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        age=request.form['age']
        uname=request.form['uname']
        pass=request.form['pass']
        email=request.form['email']
        phone=request.form['pass']
        return render_template()






    
   