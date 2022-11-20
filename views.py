from django.shortcuts import render
import mysql.connector as sql
# Create your views here.
first_name=""
last_name=""
sex=""
email_address=""
password=""
def action_login(request):
    global first_name,last_name,sex,email_address,password
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="vivek",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                first_name=value
            if key=="last_name":
                last_name=value
            if key=="sex":
                sex=value
            if key=="email":
                email_address=value
            if key=="password":
                password=value
        
        c="insert into users Values('{}','{}','{}','{}','{}')".format(first_name,last_name,sex,email_address,password)
        cursor.execute(c)
        m.commit()
    return render(request,'signup_page.html')