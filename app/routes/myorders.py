from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Depends, Request
# from routes.user import logged_user
# from routes.user import cache
from routes.user import get_logged_user

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234")
mycursor=mydb.cursor()

#To create instance of APIRouter
router=APIRouter()

#To access the html folder
templates = Jinja2Templates(directory="Templates")

#To access the css folder and pics
router.mount("/static", StaticFiles(directory="static"), name="static")


#Myorders page router to get the Myorders page visible on browser
@router.get("/myorder")
async def get_myorder(request: Request,username: str = Depends(get_logged_user)):
    myorder=[]
    mycursor.execute("SELECT * FROM petshop.orders")   
    order = mycursor.fetchall()
    for i in order:
        # if i[0]==logged_user:
        # if i[0] == cache.get("logged_username"):
        if i[1] == username:
            # print(username)
            myorder.append(i)
    # print("myorder",myorder)
    print(get_logged_user)
    print(myorder)
    return templates.TemplateResponse("Myorder.html", {"request": request,"myorder":myorder})

