import datetime

from typing import Optional
from web_system import *
from community import *
from fastapi import FastAPI, Request, Cookie
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from mocking_data import *
from module.product import Product
from module.publisher import Publisher
from module.productCatalog import ProductCatalog

app = FastAPI()
TEMPLATE = Jinja2Templates("HTML")

# ==== Init CSS ==== #
# don't forget this -> from fastapi.staticfiles import StaticFiles
css_folder = "Style"  # folder that contain your css file
css_path = "/" + css_folder  # MAJIK

app.mount(css_path, StaticFiles(directory=css_folder), name="Style")

# ==== System Init ==== #
community = Community()
product_catalog = ProductCatalog()
user_holder = UserHolder()

all_post = Board("all")
artwork = Board("artwork")
news = Board("news")
manual = Board("manual")

community.add_board(all_post, artwork, news, manual)
steam = System(product_catalog, community, user_holder)

# ==== register ==== #
steam.register(
    user_name="Best",
    email="best@gmail.com",
    password1="123Best!",
    password2="123Best!",
    register_as="user",
)
steam.register(
    user_name="Boss",
    email="boss@gmail.com",
    password1="123Boss!",
    password2="123Boss!",
    register_as="user",
)
steam.register(
    user_name="Bass",
    email="bass@gmail.com",
    password1="123Bass!",
    password2="123Bass!",
    register_as="user",
)
steam.register(
    user_name="Publ",
    email="publ@gmail.com",
    password1="123Publ!",
    password2="123Publ!",
    register_as="publisher",
)
Best = steam.search_profile(search_id=IdGenerator.generate_id("best@gmail.com"))
Bass = steam.search_profile(search_id=IdGenerator.generate_id("bass@gmail.com"))
Best.add_friend(Bass)
Bass.add_friend(Best)

# ==== init product ==== #
for product_info in all_product_info:
    product = Product(product_info)
    steam.add_product(product)

post1 = Post(
    steam.get_current_user(),
    "https://steamuserimages-a.akamaihd.net/ugc/2066632296410876700/2AFC974AEFE4A02515EF7245082FEB33A69809FA/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false",
    "Garry Mod",
)

post2 = Post(
    steam.get_current_user(),
    "https://steamuserimages-a.akamaihd.net/ugc/2050870124875593567/D308C2111B90D97E35DB21CA80106A14CA34F12D/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false",
    "Phoenix",
)

all_post.add_post(post1)
all_post.add_post(post2)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    page_data = {"request": request}

    recommend_product = steam.get_recommend_product()
    discount_product = steam.get_discount_product()

    page_data["current_user"] = steam.get_current_user()
    page_data["discount_product"] = discount_product
    page_data["recommend_product"] = recommend_product
    page_data["logged_in"] = steam.is_logged_in()
    page_data["is_publisher"] = isinstance(steam.get_current_user(), Publisher)

    return TEMPLATE.TemplateResponse("index.html", page_data)


# about publisher


@app.get("/publisher", tags=["Publisher"], response_class=HTMLResponse)
async def publisher(request: Request):
    page_data = {"request": request}
    user = steam.get_current_user()

    page_data["logged_in"] = steam.is_logged_in()
    page_data["is_publisher"] = True
    if user:
        page_data["own_products"] = user.get_all_own_products()

    return TEMPLATE.TemplateResponse("view_own_product.html", page_data)


@app.get("/add_product", tags=["Publisher"], response_class=HTMLResponse)
async def add_product(request: Request):
    page_data = {"request": request}
    user = steam.get_current_user()

    page_data["logged_in"] = steam.is_logged_in()
    page_data["is_publisher"] = True
    page_data["product_info_keys"] = keys
    if user:
        page_data["own_products"] = user.get_all_own_products()

    return TEMPLATE.TemplateResponse("add_product.html", page_data)


@app.get("/add_product_to_catalog", tags=["Publisher"], response_class=HTMLResponse)
async def add_product_to_catalog(
    request: Request,
    name,
    price,
    os_support,
    system_req,
    pre_vid,
    cover_image,
    lang_sup,
    age_rate,
    discount,
    description,
):
    page_data = {"request": request}
    user = steam.get_current_user()

    page_data["user"] = user
    page_data["is_publisher"] = True

    info = {
        "name": name,
        "price": int(price),
        "os_support": os_support,
        "system_req": system_req,
        "pre_vid": pre_vid,
        "cover_image": cover_image,
        "lang_sup": lang_sup,
        "age_rate": age_rate,
        "discount": float(discount),
        "description": description,
        "release_date": datetime.datetime.now(),
    }

    product = Product(info)
    print("> ", product)
    steam.add_product(product)
    user.add_product(product)

    return TEMPLATE.TemplateResponse("add_product.html", page_data)


@app.get("/library", tags=["Library"], response_class=HTMLResponse)
async def library(request: Request):
    page_data = {"request": request}
    current_user = steam.get_current_user()

    page_data["current_user"] = current_user
    page_data["logged_in"] = steam.is_logged_in()

    return TEMPLATE.TemplateResponse("library.html", page_data)


# about product


@app.get("/product/{product_id}", tags=["Product"], response_class=HTMLResponse)
async def view_product(request: Request, product_id):
    page_data = {"request": request}
    product = steam.get_product(product_id)

    current_user = steam.get_current_user()
    is_publisher = isinstance(current_user, Publisher)
    addable = bool(current_user)
    if addable:
        if (
            product in current_user.view_cart()
            or product in current_user.get_library().get_all_products()
        ):
            addable = False

    page_data["product"] = product
    page_data["addable"] = addable
    page_data["current_user"] = current_user
    page_data["is_publisher"] = is_publisher
    page_data["logged_in"] = steam.is_logged_in()

    return TEMPLATE.TemplateResponse("product.html", page_data)


@app.get("/search_product/result", tags=["Product"], response_class=HTMLResponse)
async def search_product(request: Request, keyword=""):
    found_products = steam.search_product(search_name=keyword)
    print(found_products, keyword, type(keyword))
    page_data = {
        "request": request,
        "found_products": found_products,
        "kw": keyword,
        "logged_in": steam.is_logged_in(),
        "current_user": steam.get_current_user()
    }
    # new front-end
    return TEMPLATE.TemplateResponse("search_product.html", page_data)


@app.get("/cart/{user_id}", tags=["Cart"], response_class=HTMLResponse)
async def cart(request: Request, user_id):
    page_data = {"request": request}
    current_user = steam.get_current_user()
    is_publisher = isinstance(current_user, Publisher)

    page_data["current_user"] = current_user
    page_data["is_publisher"] = is_publisher
    page_data["logged_in"] = steam.is_logged_in()

    return TEMPLATE.TemplateResponse("cart.html", page_data)  # new front-end


@app.get("/add_to_cart/{product_id}", tags=["Cart"])
async def add_to_cart(product_id):
    product = steam.get_product(product_id)
    current_user = steam.get_current_user()
    if current_user:
        steam.add_to_cart(product, current_user)
    url = app.url_path_for("view_product", product_id=product_id)
    return RedirectResponse(url=url)


# about profile


@app.get("/profile/{user_id}", tags=["User"], response_class=HTMLResponse)
async def view_profile(request: Request, user_id):
    page_data = {"request": request}
    user = steam.search_profile(search_id=user_id)
    current_user = steam.get_current_user()
    editable = True
    own_profile = True
    if steam.get_current_user():
        editable = False
    if user != steam.get_current_user():
        own_profile = False

    is_publisher = isinstance(user, Publisher)

    page_data["logged_in"] = steam.is_logged_in()
    page_data["own_profile"] = own_profile
    page_data["user"] = user
    page_data["is_publisher"] = is_publisher
    page_data["editable"] = editable
    page_data["current_user"] = current_user

    return TEMPLATE.TemplateResponse("profile.html", page_data)


@app.get("/search_profile/result", tags=["Profile"], response_class=HTMLResponse)
async def search_profile(request: Request, keyword=""):
    page_data = {"request": request}
    found_user = steam.search_profile(search_name=keyword, search_id="")
    current_user = steam.get_current_user()
    is_publisher = isinstance(current_user, Publisher)
    page_data["found_user"] = found_user
    page_data["kw"] = keyword
    page_data["is_publisher"] = is_publisher
    page_data["current_user"] = current_user
    page_data["logged_in"] = steam.is_logged_in()

    # new front-end
    return TEMPLATE.TemplateResponse("search_profile.html", page_data)


# login register


@app.get("/login", tags=["System"], response_class=HTMLResponse)
async def login(request: Request, status=None):
    page_data = {"request": request, "status": status}

    return TEMPLATE.TemplateResponse("login.html", page_data)  # new front-end


@app.get("/verify_login", tags=["System"], response_class=HTMLResponse)
async def verify_login(request: Request, email, password):
    status, user = steam.login(email=email, password=password)
    if status == LoginStatus.SUCCES:
        redirect_url = request.url_for("index")
        return RedirectResponse(redirect_url)
    else:
        redirect_url = request.url_for("login").include_query_params(status=status)
        return RedirectResponse(redirect_url)


@app.get("/logout", tags=["System"], response_class=HTMLResponse)
async def logout(request: Request):
    steam.logout()
    redirect_url = request.url_for("index")
    return RedirectResponse(redirect_url)


@app.get("/register", tags=["System"], response_class=HTMLResponse)
async def register(request: Request):
    page_data = {"request": request}

    return TEMPLATE.TemplateResponse("register.html", page_data)


@app.get("/verify_register", tags=["System"], response_class=HTMLResponse)
async def verify_register(
    request: Request, register_as, user_name, email, password1, password2
):
    status = steam.register(
        user_name=user_name,
        email=email,
        password1=password1,
        password2=password2,
        register_as=register_as,
    )

    page_data = {"request": request}
    if status == RegistStatus.SUCCESS:
        redirect_url = request.url_for("index")
        return RedirectResponse(redirect_url)

    else:
        page_data["status"] = status
        # new front-end
        return TEMPLATE.TemplateResponse("register.html", page_data)


@app.get("/remove_from_cart/{user_id}/{product_id}", tags=["Cart"])
async def remove_from_cart(product_id, user_id):
    product = steam.get_product(product_id)
    user = steam.search_profile(search_id=user_id)
    user.get_cart().remove_product(product)
    url = app.url_path_for("cart", user_id=user_id)
    return RedirectResponse(url=url)


@app.get("/payment/{user_id}", tags=["Payment"], response_class=HTMLResponse)
async def payment_detail(request: Request, user_id):
    user = steam.search_profile(search_id=user_id)
    page_data = {"request": request, "user": user, "logged_in": steam.is_logged_in()}

    return TEMPLATE.TemplateResponse("payment.html", page_data)


@app.get("/confirmation/{user_id}", tags=["History"])
async def confirm_purchase(
    user_id,
    method,
    card_number,
    expiration_month,
    expiration_year,
    first_name,
    last_name,
    billing_address1,
    billing_address2,
    country,
    city,
    postal_code,
    phone_number,
):
    user = steam.search_profile(search_id=user_id)
    cart = user.get_cart()
    library = user.get_library()
    history = user.get_purchase_history()
    user.create_order()
    order = user.get_order()

    for product in cart.get_products():
        library.add_product(product)
        order.add_product(product)
    order.summalize(
        method,
        card_number,
        expiration_month,
        expiration_year,
        first_name,
        last_name,
        billing_address1,
        billing_address2,
        country,
        city,
        postal_code,
        phone_number,
    )
    history.add_to_history(order)
    cart.remove_all_product()

    url = app.url_path_for("library")
    return RedirectResponse(url=url)


@app.get("/purchase_history/{user_id}", tags=["History"], response_class=HTMLResponse)
async def purchase_history(request: Request, user_id):
    current_user = steam.search_profile(search_id=user_id)
    page_data = {
        "request": request,
        "current_user": current_user,
        "logged_in": steam.is_logged_in(),
    }
    return TEMPLATE.TemplateResponse("purchase_history.html", page_data)


@app.get("/order_history/{order_id}", tags=["History"], response_class=HTMLResponse)
async def view_order(request: Request, order_id):
    current_user = steam.get_current_user()
    order = current_user.get_purchase_history().search_order(order_id)
    page_data = {
        "request": request,
        "current_user": current_user,
        "logged_in": steam.is_logged_in(),
        "order": order,
    }
    return TEMPLATE.TemplateResponse("order_history.html", page_data)


@app.get("/setting_profile/{user_id}", tags=["User"], response_class=HTMLResponse)
async def setting_profile(request: Request):
    current_user = steam.get_current_user()
    page_data = {
        "request": request,
        "current_user": current_user,
        "logged_in": steam.is_logged_in(),
    }
    return TEMPLATE.TemplateResponse("setting_profile.html", page_data)


@app.get("/edit_profile/{user_id}", tags=["User"])
async def edit_profile(name, picture_profile, description, user_id):
    current_user = steam.get_current_user()
    if name != "":
        current_user.set_name(name)

    if picture_profile != "":
        current_user.set_picture_profile(picture_profile)

    if description != "":
        current_user.set_description(description)

    url = app.url_path_for("view_profile", user_id=user_id)
    return RedirectResponse(url=url)


@app.get("/pending_friend/{user_id}", tags=["Friend"], response_class=HTMLResponse)
async def pending_friend(request: Request):
    current_user = steam.get_current_user()
    page_data = {"request": request, "current_user": current_user, "logged_in": steam.is_logged_in()}
    return TEMPLATE.TemplateResponse("pending_friend.html", page_data)


@app.get("/send_invite/{user_id}/{target_id}", tags=["Friend"])
async def send_friend_invite(user_id, target_id):
    current_user = steam.get_current_user()
    target = steam.search_profile(search_id=target_id)
    target.add_invite_list(current_user)
    current_user.add_pending_list(target)
    url = app.url_path_for("pending_friend", user_id=user_id)
    return RedirectResponse(url=url)


@app.get("/clear_invite/{user_id}", tags=["Friend"])
async def clear_friend(user_id):
    current_user = steam.get_current_user()
    for others in current_user.get_invite_list():
        others.remove_invite_list(current_user)
    current_user.clear_pending_list()
    url = app.url_path_for("pending_friend", user_id=user_id)
    return RedirectResponse(url=url)


@app.get("/reject_invite/{user_id}/{target_id}", tags=["Friend"])
async def reject_invite(user_id, target_id):
    current_user = steam.search_profile(search_id=user_id)
    target = steam.search_profile(search_id=target_id)
    current_user.remove_pending_list(target)
    target.remove_invite_list(current_user)
    url = app.url_path_for("pending_friend", user_id=user_id)
    return RedirectResponse(url=url)


@app.get("/accept_invite/{user_id}/{target_id}", tags=["Friend"])
async def accept_invite(user_id, target_id):
    current_user = steam.search_profile(search_id=user_id)
    target = steam.search_profile(search_id=target_id)
    current_user.remove_invite_list(target)
    current_user.add_friend(target)
    target.remove_pending_list(current_user)
    target.add_friend(current_user)
    url = app.url_path_for("pending_friend", user_id=user_id)
    return RedirectResponse(url=url)


# ==================== Community Route ==================== #


@app.get("/community/{board_name}", tags=["Community"], response_class=HTMLResponse)
async def community(request: Request, board_name="all"):
    page_data = {"request": request}
    current_user = steam.get_current_user()
    is_publisher = isinstance(current_user, Publisher)
    board = steam.get_board(board_name)

    page_data["board"] = board
    page_data["current_user"] = current_user
    page_data["is_publisher"] = is_publisher
    page_data["logged_in"] = steam.is_logged_in()

    return TEMPLATE.TemplateResponse("community.html", page_data)


@app.get("/add_post", tags=["Community"], response_class=HTMLResponse)
async def add_post(request: Request):
    page_data = {"request": request}

    return TEMPLATE.TemplateResponse("add_post.html", page_data)


@app.get("/submit_post", tags=["Community"], response_class=HTMLResponse)
async def submit_post(board_name, image, game_name):
    post = Post(steam.get_current_user(), image, game_name)
    board = steam.get_board(board_name)
    board.add_post(post)
    url = app.url_path_for("community", board_name=board_name)
    return RedirectResponse(url=url)


@app.get(
    "/rate_up/{board_name}/{post_id}", tags=["Community"], response_class=HTMLResponse
)
async def rate_up(board_name, post_id):
    current_user = steam.get_current_user()
    board = steam.get_board(board_name)
    post = board.get_post(post_id)
    if post and current_user:
        post.rate_up(current_user)
    url = app.url_path_for("community", board_name=board_name)
    return RedirectResponse(url=url)


# ==================== Chat Route ==================== #
@app.get("/view_chat/{user_id}/{target_id}", tags=["Chat"], response_class=HTMLResponse)
async def view_chat(request: Request, user_id, target_id):
    user = steam.search_profile(search_id=user_id)
    target = steam.search_profile(search_id=target_id)
    page_data = {"request": request, "user": user, "target": target}
    # return TEMPLATE.TemplateResponse("Chat.html", page_data)
    print(user.get_chat().view_message(target))
    # return {"message_box": user.get_chat().view_message(target)}


@app.get(
    "/send_message/{user_id}/{target_id}", tags=["Chat"], response_class=HTMLResponse
)
async def send_message(user_id, target_id, message):
    user = steam.search_profile(search_id=user_id)
    target = steam.search_profile(search_id=target_id)
    user.get_chat().send_message(message, target, user)
    print("send : ", user.get_chat().view_message(target))
    print("receive : ", target.get_chat().view_message(user))
    url = app.url_path_for("view_chat", user_id=user_id, target_id=target_id)
    return RedirectResponse(url=url)


@app.get("/get_chat/{user_id}", tags=["Chat"])
async def get_chat(user_id):
    user = steam.search_profile(search_id=user_id)
    print(user.get_chat().get_message_box())
