from web_system import *
from community import *
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from mocking_data import *
from module.product import Product

app = FastAPI()
TEMPLATE = Jinja2Templates("HTML")

# don't forget this -> from fastapi.staticfiles import StaticFiles
css_folder = "Style"  # folder that contain your css file
css_path = "/" + css_folder  # MAJIK

app.mount(css_path, StaticFiles(directory=css_folder), name="Style")

# ==== System Init ==== #
community = Community()
product_catalog = ProductCatalog()

all_post = Board("all")
artwork = Board("artwork")
news = Board("news")
manual = Board("manual")


community.add_board(all_post, artwork, news, manual)
steen_system = System(product_catalog, community)

# ==== register ==== #
steen_system.register(user_name="Best", email="dark97975@gmail.com",
                      password1="123Paul!", password2="123Paul!")
steen_system.register(user_name="Tony", email="tony789@gmail.com",
                      password1="Paulo789$", password2="Paulo789$")
steen_system.register(user_name="Best", email="ggwellplay@gmail.com",
                      password1="465Paul#", password2="456Paul#")
steen_system.register(user_name="Rosey", email="rosenne@gmail.com",
                      password1="redRose123?", password2="redRose123?")

# ==== init product ==== #
dota_2 = Product(dota_2)
let_build_a_zoo = Product(let_build_a_zoo)
tribes_of_midgard = Product(tribes_of_midgard)
fifa_23 = Product(fifa_23)
planet_zoo = Product(planet_zoo)
sea_of_thieves_2023 = Product(sea_of_thieves_2023)


steen_system.add_product(dota_2)
steen_system.add_product(let_build_a_zoo)
steen_system.add_product(tribes_of_midgard)
steen_system.add_product(fifa_23)
steen_system.add_product(planet_zoo)
steen_system.add_product(sea_of_thieves_2023)

post1 = Post(steen_system.get_current_user(
), "https://steamuserimages-a.akamaihd.net/ugc/2066632296410876700/2AFC974AEFE4A02515EF7245082FEB33A69809FA/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false", "Garry Mod")

all_post.add_post(post1)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    page_data = {"request": request}

    recommend_product = steen_system.get_recommend_product()
    discount_product = steen_system.get_discount_product()

    page_data["discount_product"] = discount_product
    page_data["recommend_product"] = recommend_product

    page_data["user"] = steen_system.get_current_user()
    print(page_data["user"])
    return TEMPLATE.TemplateResponse("index.html", page_data)


@app.get("/product/{product_id}", response_class=HTMLResponse)
async def view_product(request: Request, product_id):
    product = steen_system.get_product(product_id)

    page_data = {"request": request, "product": product.get_info(
    ), "user": steen_system.get_current_user()}
    return TEMPLATE.TemplateResponse("product.html", page_data)


@app.post("/product/{product_id}", response_class=HTMLResponse)
async def view_product(request: Request, product_id):
    product = steen_system.get_product(product_id)

    page_data = {"request": request, "product": product.get_info(
    ), "user": steen_system.get_current_user()}
    return TEMPLATE.TemplateResponse("product.html", page_data)


@app.get("/profile/{user_id}", response_class=HTMLResponse)
async def view_profile(request: Request, user_id):
    user = steen_system.search_profile(search_id=user_id)
    page_data = {"request": request, "user": user}
    return TEMPLATE.TemplateResponse("profile.html", page_data)


@app.get("/library/{user_id}", tags=["Library"], response_class=HTMLResponse)
async def library(user_id, request: Request):
    user = steen_system.search_profile(search_id=user_id)
    page_data = {"request": request, "user": user}
    return TEMPLATE.TemplateResponse("library.html", page_data)


@app.get("/login", response_class=HTMLResponse)
async def login(request: Request, status=None):
    page_data = {"request": request}
    page_data["status"] = status
    return TEMPLATE.TemplateResponse("login.html", page_data)  # new front-end


@app.get("/verify_login", response_class=HTMLResponse)
async def verify_login(request: Request, email, password):
    status, user = steen_system.login(email=email, password=password)
    if status == LoginStatus.SUCCES:
        print("verify", user)
        redirect_url = request.url_for("index")
        return RedirectResponse(redirect_url)
    else:
        redirect_url = request.url_for(
            "login").include_query_params(status=status)
        return RedirectResponse(redirect_url)


@app.get("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    steen_system.logout()
    redirect_url = request.url_for("index")
    return RedirectResponse(redirect_url)


@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    page_data = {"request": request}
    # new front-end
    return TEMPLATE.TemplateResponse("register.html", page_data)


@app.get("/verify_register", response_class=HTMLResponse)
async def verify_register(request: Request, username, email, pass1, pass2):
    status = steen_system.register(
        user_name=username, email=email, password1=pass1, password2=pass2)

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
        # new front-end
        return TEMPLATE.TemplateResponse("register.html", page_data)


@app.get("/search_product/result", response_class=HTMLResponse)
async def search_product(request: Request, keyword=""):
    found_products = steen_system.search_product(search_name=keyword)
    print(found_products, keyword, type(keyword))
    page_data = {"request": request,
                 "found_products": found_products, "kw": keyword}
    # new front-end
    return TEMPLATE.TemplateResponse("search_product.html", page_data)


@app.get("/cart/{user_id}", response_class=HTMLResponse)
async def cart(request: Request, user_id):
    user = steen_system.search_profile(search_id=user_id)
    page_data = {"request": request, "user": user}

    return TEMPLATE.TemplateResponse("cart.html", page_data)  # new front-end


@app.post("/add_to_cart/{product_id}", tags=["Cart"])
async def add_to_cart(product_id):
    product = steen_system.get_product(product_id)
    user = steen_system.get_current_user()
    if user:
        print(">>", user.get_cart())
        steen_system.add_to_cart(product, user)
        print(">>", user.get_cart())
    url = app.url_path_for("view_product", product_id=product_id)
    return RedirectResponse(url=url)


@app.get("/remove_from_cart/{user_id}/{product_id}", tags=["Cart"])
async def remove_from_cart(product_id, user_id):
    product = steen_system.get_product(product_id)
    user = steen_system.search_profile(search_id=user_id)
    user.get_cart().remove_product(product)
    url = app.url_path_for("cart", user_id=user_id)
    return RedirectResponse(url=url)


@app.get("/payment/{user_id}", tags=["Payment"], response_class=HTMLResponse)
async def payment_detail(request: Request, user_id):
    user = steen_system.search_profile(search_id=user_id)
    page_data = {"request": request, "user": user}
    return TEMPLATE.TemplateResponse("payment.html", page_data)


@app.get("/confirmation/{user_id}", response_class=HTMLResponse)
async def confirm_purchase(request: Request, user_id, method, card_number, expiration_month, expiration_year, first_name, last_name,
                           billing_address1, billing_address2, country, city, postal_code, phone_number):
    user = steen_system.search_profile(search_id=user_id)
    page_data = {"request": request, "user": user}
    
    cart = user.get_cart()
    library = user.get_library()
    for product in cart.get_products():
        if product.get_name() not in [item.get_name() for item in library.get_products()]:
            library.add_product(product)
    return TEMPLATE.TemplateResponse("library.html", page_data)

# ==================== Community Route ==================== #


@app.get("/community/{board_name}", response_class=HTMLResponse)
async def community(request: Request, board_name="all"):
    page_data = {"request": request}

    board = steen_system.get_board(board_name)

    page_data["board"] = board
    print(board)

    return TEMPLATE.TemplateResponse("community.html", page_data)


@app.get("/setting_profile/{user_id}", tags=["User"], response_class=HTMLResponse)
async def setting_profile(request: Request, user_id):
    user = steen_system.search_profile(search_id=user_id)
    page_data = {"request": request, "user": user}
    return TEMPLATE.TemplateResponse("setting_profile.html", page_data)


@app.get("/edit_profile/{user_id}", tags=["User"], response_class=HTMLResponse)
async def edit_profile(request: Request, name, picture_profile, description, user_id):
    user = steen_system.search_profile(search_id=user_id)
    if name != "":
        user.set_name(name)

    if picture_profile != "":
        user.set_picture_profile(picture_profile)

    if description != "":
        user.set_description(description)

    page_data = {"request": request, "user": user}
    return TEMPLATE.TemplateResponse("profile.html", page_data)


@app.put("/chat/{user_id}/{target_id}", tags=["Chat"], response_class=HTMLResponse)
async def chat_with(request: Request, user_id, target_id):
    user = steen_system.search_profile(search_id=user_id)
    target = steen_system.search_profile(search_id=target_id)
    page_data = {"request": request, "user": user, "target": target}
    return TEMPLATE.TemplateResponse("Chat.html", page_data)
