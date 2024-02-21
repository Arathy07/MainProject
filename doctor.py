from flask import *
from database import *
doctor=Blueprint('doctor',__name__)



@doctor.route("/doctorhome")
def doctorhome():


    return render_template("doctorhome.html")


@doctor.route("/editprofile",methods=['get','post'])
def editprofile():
    data={}
    qry8="select * from doctor"
    data['user']=select(qry8)
    if 'action'in request.args:
        action=request.args['action']
        id=request.args['id']
        
        if action=='update':
             qry6="select * from doctor where doctor_id='%s'"%(id)
             data['up']=select(qry6)
             if 'update' in request.form:
                 fname=request.form['fname']
                 lname=request.form['lname']
                 place=request.form['place']
                 email=request.form['email']
                 phone=request.form['phone']
                 designation=request.form['designation']

                 q="update doctor set fname='%s',lname='%s',place='%s',email='%s',phone='%s',designation='%s'where doctor_id='%s'"%(fname,lname,place,email,phone,designation,id)
                 update(q)
                 return '''<script>alert("update successfull");window.locatioin="/registration"</script>'''


   

    return render_template("doctorprofiledit.html",data=data)

@doctor.route("/viewdisease",methods=['get','post'])
def viewdisease():
    data={}
    qry8="select * from diseases"
    data['user']=select(qry8)
   

    return render_template("viewdisease.html",data=data)

@doctor.route("/schedulemanagement",methods=['get','post'])
def schedulemanagement():
    data={}
    if 'submit' in request.form:
        sdate=request.form['startdate']
        edate=request.form['enddate']
        stime=request.form['starttime']
        etime=request.form['endtime']
        qry1="insert into doctors_schedule values(null,'%s','%s','%s','%s','%s')"%(session['lid'],sdate,edate,stime,etime)
        insert(qry1)
    return render_template("schedulemanagement.html",data=data)





@doctor.route("/doctor",methods=['get','post'])
def doctorregistration():
    data={}
    if 'submit' in request.form:
        fn=request.form['fname']
        ln=request.form['lname']
        place=request.form['place']
        email=request.form['email']
        phone=request.form['phone']
        
        designation=request.form['designation']
        username=request.form['username']
        password=request.form['password']    

        qry="insert into login values(null,'%s','%s','pending')"%(username,password)
        login_id=insert(qry)
        qry1="insert into doctor values(null,'%s','%s','%s','%s','%s','%s','%s','pending')"%(login_id,fn,ln,place,email,phone,designation)
        insert(qry1)
        
        
        return '''<script>alert("Account created successfully");window.locatioin="/login"</script>'''
   

    return render_template("doctorregistration.html",data=data)

