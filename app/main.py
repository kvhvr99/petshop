from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234")
mycursor=mydb.cursor()

#importing router files to include routers
from routes.user import router as user_register
from routes.body import router as app_body
from routes.buying import router as buying
from routes.myorders import router as myorder


#To create instance of fastapi
#This app object is the main point of interaction of the application with the client browser. The uvicorn server uses this object to listen to client’s request.
app = FastAPI()



#To access the html folder
templates = Jinja2Templates(directory="Templates")

#To access the css and pics
app.mount("/static", StaticFiles(directory="static"), name="static")

#To include routers
app.include_router(user_register)
app.include_router(app_body)
app.include_router(buying)
app.include_router(myorder)


if __name__=='__main__':
    app.run(debug=True)