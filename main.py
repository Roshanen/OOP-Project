from webSystem import *
from community import *
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

css_dir = "Style"  # folder that contain css file
css_path = "/" + css_dir
css_folder_name = "Style"

app.mount(css_path, StaticFiles(directory=css_dir), name=css_folder_name)

steen_system = System()

steen_system.register(user_name="Paul",email="dark97975@gmail.com",password1="123Paul!",password2="123Paul!")

template = Jinja2Templates("Template")

@app.get("/",response_class=HTMLResponse)
async def show_default(request : Request):
    return template.TemplateResponse("index.html",{"request" : request})

@app.get("/search_profile")
async def search_profile(name = None,id = None):
    found_user = steen_system.search_profile(search_name=name,search_id=id)
    return found_user

@app.get("/search_product")
async def search_product(name = None):
    found_products = steen_system.search_product(search_name=name)
    return found_products

@app.post("/register")
async def register(username,email,pass1,pass2):
    status = steen_system.register(user_name=username,email=email,password1=pass1,password2=pass2)
    return status

@app.post("/login")
async def register(email,password):
    status = steen_system.login(email=email,password=password)
    return status

@app.post("/view_user_profile")
async def register(email,password):
    status = steen_system.login(email=email,password=password)
    return status

# DEBUGGING ZONE

@app.get("/see_current_user")
async def see_current_user():
    return steen_system.get_current_user()

@app.get("/see_all_user")
async def see_all_user():
    return steen_system.get_all_user()

