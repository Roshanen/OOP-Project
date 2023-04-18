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
    page_data = {"request" : request}

    recommend_product = steen_system.get_recommend_product()
    discount_product = steen_system.get_discount_product()

    page_data["discount_product"] = discount_product
    page_data["recommend_product"] = recommend_product
    page_data["user"] = None

    return TEMPLATE.TemplateResponse("index.html",page_data)

@app.get("/product/{prod_id}",response_class=HTMLResponse)
async def view_product(request : Request, prod_id):
    product = steen_system.get_product(prod_id)

    page_data = {"request" : request, "product":product.get_info()}
    return TEMPLATE.TemplateResponse("product.html",page_data)

@app.get("/profile/{user_id}",response_class=HTMLResponse)
async def view_profile(request : Request, user_id):
    user = steen_system.search_profile(search_id = user_id)

    page_data = {"request": request, "user": user}
    return TEMPLATE.TemplateResponse("profile.html",page_data)

@app.get("/login",response_class=HTMLResponse)
async def login(request: Request):
    page_data = {"request": request}
    return TEMPLATE.TemplateResponse("login.html",page_data) # new front-end

@app.post("/verify_login",response_class=HTMLResponse)
async def register(request: Request, email,password):
    status, user = steen_system.login(email=email,password=password)

    page_data = {"request": request}
    if status == LoginStatus.SUCCES:
        page_data["user"] = user
        return TEMPLATE.TemplateResponse("index.html", page_data)
    else:
        page_data["login_status"] = status
        return TEMPLATE.TemplateResponse("login.html", page_data) # new front-end

@app.get("/register",response_class=HTMLResponse)
async def register(request : Request):
    page_data = {"request": request}
    return TEMPLATE.TemplateResponse("register.html",page_data) # new front-end

@app.post("/verify_register",response_class=HTMLResponse)
async def register(request: Request, username,email,pass1,pass2):
    status = steen_system.register(user_name=username,email=email,password1=pass1,password2=pass2)

    page_data = {"request": request}
    if status == LoginStatus.SUCCES:
        # this is the same as index function maybe find some alt
        recommend_product = steen_system.get_recommend_product()
        discount_product = steen_system.get_discount_product()

        page_data["discount_product"] = discount_product
        page_data["recommend_product"] = recommend_product
        page_data["user"] = None

        return TEMPLATE.TemplateResponse("index.html", page_data)
        # end index function

    else:
        page_data["register_status"] = status
        return TEMPLATE.TemplateResponse("register.html", page_data) # new front-end

@app.get("/search_product/result/search_name={name}",response_class=HTMLResponse)
async def search_product(request: Request, name = None):
    found_products = steen_system.search_product(search_name=name)

    page_data = {"request": request}
    return TEMPLATE.TemplateResponse("show_search_result.html",page_data) # new front-end

@app.get("/cart/{user_id}",response_class=HTMLResponse)
async def cart(request: Request, user_id):
    user = steen_system.search_profile(search_id=user_id)
    page_data = {"request": request, "user": user}

    return TEMPLATE.TemplateResponse("cart.html", page_data) # new front-end
