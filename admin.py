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


@admin.route("/diseasemanaging")
def diseasemanagement():
   

    return render_template("diseasemanagement.html")
