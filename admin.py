from flask import *
from database import *
admin=Blueprint('admin',__name__)

@admin.route("/admin")
def adminhome():
   

    return render_template("adminhome.html")

@admin.route("/adminmanaging",methods=['get','post'])

def adminmanagement():
    data={}
    qry5="select * from doctor"
    data['user']=select(qry5)
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=='Reject':
        qry="update doctor set status='Rejected' where login_id='%s'"%(id)
        update(qry)
        qry9="update login set usertype='pending' where login_id='%s'"%(id)
        update(qry9)

    if action=='Approve':
        qry1="update doctor set status='Approved' where login_id='%s'"%(id)
        update(qry1)
        qry6="update login set usertype='doctor' where login_id='%s'"%(id)
        update(qry6)




    


        
    
    return render_template("adminmanagement.html",data=data)


@admin.route("/diseasemanaging",methods=['get','post'])
def diseasemanagement():
    data={}
    qry3="select * from diseases"
    data['user']=select(qry3)
    
    if 'submit' in request.form:
        Diseasename=request.form['Diseasename']
        description=request.form['description']
        uploadimage=request.form['image']
        qry1="insert into diseases values(null,'%s','%s','%s')"%(Diseasename, description,uploadimage)
        insert(qry1)
        return '''<script>alert("Add successfull");window.locatioin="/registration"</script>'''

    if 'action'in request.args:
        action=request.args['action']
        id=request.args['id']


        if action=='delete':
            qry2="delete from diseases where disease_id='%s'"%(id)
            delete(qry2)
            return '''<script>alert("Delection successfull");window.locatioin="/registration"</script>'''
        if action=='update':
             qry6="select * from diseases where disease_id='%s'"%(id)
             data['up']=select(qry6)
             if 'update' in request.form:
                 Diseasename=request.form['Diseasename']
                 description=request.form['description']
                 uploadimage=request.form['image']
                 q="update diseases set disease_name='%s',description='%s',image='%s' where disease_id='%s'"%( Diseasename,description,uploadimage,id)
                 update(q)
                 return '''<script>alert("update successfull");window.locatioin="/registration"</script>'''
                    
        

    return render_template("diseasemanagement.html",data=data)
@admin.route("/viewuser",methods=['get','post'])
def viewuser():
    data={}
    qry2="select * from patient"
    data['user']=select(qry2)
   

    return render_template("viewusers.html",data=data)


@admin.route("/viewfeedback",methods=['get','post'])
def viewfeedback():
    data={}
    qry9="select * from feedback"
    data['user']=select(qry9)
   

    return render_template("viewfeedback.html",data=data)



@admin.route("/viewdoctorreviews",methods=['get','post'])
def viewreview():
    data={}
    qry8="select * from review"
    data['user']=select(qry8)
   

    return render_template("viewreview.html",data=data)



@admin.route("/symptommanagement",methods=['get','post'])
def symptommanagement():
    data={}
    qry3="select *  from symptom"
    data['user']=select(qry3)
    if 'submit' in request.form:
        symptomname=request.form['name']
        description=request.form['des']
        
        qry1="insert into symptom values(null,'%s','%s')"%(symptomname,description)
        insert(qry1)
        return '''<script>alert("Add successfull");window.locatioin="/registration"</script>'''
    
    if 'action'in request.args:
        action=request.args['action']
        id=request.args['id']


        if action=='delete':
            qry2="delete from symptom where symptom_id='%s'"%(id)
            delete(qry2)

        if action=='update':
             qry6="select * from symptom where symptom_id='%s'"%(id)
             data['up']=select(qry6)
             if 'update' in request.form:
                 sname=request.form['name']
                 description=request.form['des']
                 q="update diseases set symptom_name='%s',symptom_description='%s' where symptom_id='%s'"%( sname,description,id)
                 update(q)
                 return '''<script>alert("update successfull");window.locatioin="/registration"</script>'''
                    
    
    return render_template("symptom.html",data=data)


