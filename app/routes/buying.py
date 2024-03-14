from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request, Form

import random
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234")
mycursor=mydb.cursor()

#To create instance of APIRouter
router=APIRouter()

#To access the html folder
templates = Jinja2Templates(directory="Templates")

#To access the css folder and pics
router.mount("/static", StaticFiles(directory="static"), name="static")


#Buying page router to get the Buying page visible on browser
@router.get("/buy")
def get_buy(request: Request):
    return templates.TemplateResponse("buying.html", {"request": request})

#register page router to push data to the database-->mysql workbentch
@router.post("/buy")
def post_buy(request: Request, UserName:str = Form(...), email:str = Form(...), phone: str = Form(...),pet:str = Form(...), quantity:str = Form(...),address:str = Form(...) ):
    #Checking Phone number length
    if len(phone)!=10:
        return templates.TemplateResponse("buying.html",{"request":request,"error":"Phone Number must have 10 digits....."})
    
    id=random.randint(100000,500000)
    mycursor.execute("SELECT * FROM petshop.register")        
    user = mycursor.fetchall()
    for i in user:
        if i[0]==UserName:
            mycursor.execute("Insert into petshop.orders(id,name,email,phone_number,pet_name,quantity,address,status)values('{}','{}','{}','{}','{}','{}','{}','{}')".format(id,UserName,email,phone,pet,quantity,address,"Progress.."))
            mydb.commit()
            return templates.TemplateResponse("buying.html", {"request": request, "message":"Purchasing is completed, Goto MyOrders to check your order details..."})
    return templates.TemplateResponse("buying.html",{"request":request,"error":"Please enter valid UserName"})           
    
