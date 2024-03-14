from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request, Form

#To Store Logged UserName in cache data for 3600[1 hour]
# from cachetools import TTLCache
# cache = TTLCache(maxsize=100, ttl=60)

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234")
mycursor=mydb.cursor()

#To create instance of APIRouter
router=APIRouter()

#To access the html folder
templates = Jinja2Templates(directory="Templates")

#To access the css folder and pics
router.mount("/static", StaticFiles(directory="static"), name="static")


class LoggedUser:
    def __init__(self):
        self.username = None

logged_user = LoggedUser()

# Dependency to get and set logged-in username
def get_logged_user(request: Request):
    return logged_user.username

# logged_user=""

#register page router to get the register page visible on browser
@router.get("/register")
def get_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

#register page router to push data to the database-->mysql workbentch
@router.post("/register")
def register(request: Request, Username:str = Form(...), Email:str = Form(...), Phone_Number: str = Form(...),Password:str = Form(...), Retype_password:str = Form(...) ):

    #Checking username length
    if len(Username)<6:
        return templates.TemplateResponse("register.html",{"request":request,"message":"Username must have more than 6 characters....."})
    
    #Checking password and retype_password are same or not
    elif Password != Retype_password:
        return templates.TemplateResponse("register.html",{"request":request,"message":"Password and Re-type Password should be same....."})
    
    #Checking Phone number length
    elif len(Phone_Number)!=10:
        return templates.TemplateResponse("register.html",{"request":request,"message":"Phone Number must have 10 digits....."})
    
    #Checking user already exists are not
    elif True:
        mycursor.execute("SELECT * FROM petshop.register")        
        user = mycursor.fetchall()

        #Iterates the users_data table to fetech the user's data
        for i in user:
            if i[0]== Username :
                return templates.TemplateResponse("register.html",{"request":request,"message":"User already exists[Goto Login Page]....."})


    mycursor.execute("Insert into petshop.register(username,email,phone_number,password)values('{}','{}','{}','{}')".format(Username,Email,Phone_Number,Password))
    mydb.commit()
    return templates.TemplateResponse("register.html", {"request": request, "success":"Registered Successfully....."})


#login page router to get the login paga visible on browser
@router.get("/login")
def get_loginPage(request: Request):
    return templates.TemplateResponse("account.html", {"request": request})

#login page router to check Login_Page Credentials
@router.post("/login")
def login(request: Request, username:str = Form(...), password:str = Form(...) ):
    # global logged_user
    mycursor.execute("SELECT * FROM petshop.register")        
    user = mycursor.fetchall()
    for i in user:
        if i[0]==username and i[3]==password:
            # logged_user = i[0]
            # cache["logged_username"] = i[0]
            logged_user.username = username
            return templates.TemplateResponse("userHome.html", {"request": request})
    
    return templates.TemplateResponse("account.html",{"request":request, "message":"Invalid Username or Password...."})

