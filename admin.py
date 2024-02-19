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
        qry="update doctor set status='Rejected' where doctor_id='%s'"%(id)
        update(qry)
    if action=='Approve':
        qry1="update doctor set status='Approved' where doctor_id='%s'"%(id)
        update(qry1)
    


        
    
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

    if 'action'in request.args:
        action=request.args['action']
        id=request.args['id']


        if action=='delete':
            qry2="delete from diseases where disease_id='%s'"%(id)
            delete(qry2)
        if action=='update':
             qry6="select * from diseases where disease_id='%s'"%(id)
             data['up']=select(qry6)
             if 'update' in request.form:
                 Diseasename=request.form['Diseasename']
                 description=request.form['description']
                 uploadimage=request.form['image']
                 q="update diseases set disease_name='%s',description='%s',image='%s' where disease_id='%s'"%( Diseasename,description,uploadimage,id)
                 update(q)
                    
        

    return render_template("diseasemanagement.html",data=data)
