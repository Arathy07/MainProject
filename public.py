from flask import *
from database import *
public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template("home.html")


@public.route('/login',methods=['post','get'])
def login():
    if 'submit' in request.form:
        uname=request.form['username']
        password=request.form['password']
        query="select * from login where username='%s' and password='%s'"%(uname,password)
        res=select(query)
        print(res)
        if res[0]['usertype']=='admin':
            return redirect(url_for('admin.adminhome'))
        elif res[0]['usertype']=='doctor':
            return redirect(url_for('doctor.doctorhome'))
        
    return render_template("login.html")



    
        

