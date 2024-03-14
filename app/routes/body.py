from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234")
mycursor=mydb.cursor()


#To create instance of APIRouter
router=APIRouter()


#To access the html folder
templates = Jinja2Templates(directory="Templates")


#To access the css folder and pics
router.mount("/static", StaticFiles(directory="static"), name="static")

#Home page router to get the home page visible on browser
@router.get("/home")
def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


#Breeds page router to get the breeds page visible on browser
@router.get("/breeds")
def get_breeds(request: Request):
    return templates.TemplateResponse("breeds.html", {"request": request})


#About page router to get the about paga visible on browser
@router.get("/about")
def get_About(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

#Contact page router to get the contact paga visible on browser
@router.get("/contact")
def get_Contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

#gotoLogin page router to get the gotoLogin paga visible on browser
@router.get("/gotoLogin")
def get_Contact(request: Request):
    return templates.TemplateResponse("gotoLogin.html", {"request": request})

#User Home page router
@router.get("/userHome")
def UserHome(request:Request):
    return templates.TemplateResponse("userHome.html",{"request":request})

#UserContact page router to get the UserContact paga visible on browser
@router.get("/UserContact")
def get_Contact(request: Request):
    return templates.TemplateResponse("UserContact.html", {"request": request})

#UserAbout page router to get the UserAbout paga visible on browser
@router.get("/UserAbout")
def get_Contact(request: Request):
    return templates.TemplateResponse("UserAbout.html", {"request": request})

#UserBreeds page router to get the UserBreeds paga visible on browser
@router.get("/UserBreeds")
def get_Contact(request: Request):
    return templates.TemplateResponse("UserBreeds.html", {"request": request})