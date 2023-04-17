from WebSystem import *
from Community import *
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from MockingData import *

app = FastAPI()

# don't forget this -> from fastapi.staticfiles import StaticFiles
css_folder = "Style"  # folder that contain your css file
css_path = "/" + css_folder  # MAJIK

app.mount(css_path, StaticFiles(directory=css_folder), name=css_folder)

steen_system = System()

steen_system.register(user_name="Paul",email="dark97975@gmail.com",password1="123Paul!",password2="123Paul!")

dota_2 = Product(dota_2)
let_build_a_zoo = Product(let_build_a_zoo)
tribes_of_midgard = Product(tribes_of_midgard)

steen_system.add_product(dota_2)
steen_system.add_product(let_build_a_zoo)
steen_system.add_product(tribes_of_midgard)

TEMPLATE = Jinja2Templates("HTML")

# @app.get('/favicon.ico')
# async def favicon():
#     file_name = "logo.png"
#     file_path = "Icon/"
#     return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})

@app.get("/",response_class=HTMLResponse)
async def index(request : Request):
    data_for_index_page = {"request" : request}

    recommend_product = steen_system.get_recommend_product()
    discount_product = steen_system.get_discount_product()

    data_for_index_page["discount_product"] = discount_product
    data_for_index_page["recommend_product"] = recommend_product

    return TEMPLATE.TemplateResponse("index.html",data_for_index_page)

@app.get("/product/{prod_id}",response_class=HTMLResponse)
async def view_product(request : Request, prod_id):
    product = steen_system.get_product(prod_id)
    data_for_index_page = {"request" : request, "product":product.get_info()}

    return TEMPLATE.TemplateResponse("product.html",data_for_index_page)

@app.get("/view_user_profile/{search_id}",response_class=HTMLResponse)
async def view_profile(request : Request, search_id):
    user = steen_system.search_profile(search_id = search_id)[0]
    data_for_index_page = {"request": request, "user": user}

    return TEMPLATE.TemplateResponse("profile.html",data_for_index_page)


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

# DEBUGGING ZONE

@app.get("/see_current_user")
async def see_current_user():
    return steen_system.get_current_user()

@app.get("/see_all_user")
async def see_all_user():
    return steen_system.get_all_user()

