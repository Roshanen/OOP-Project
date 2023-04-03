import datetime
from WebSystem import *
from Community import *
from User import *


steen_system = System()

steen_system.register(user_name = "Best",email = "dark97975@gmail.com",password1 = "12345Best",password2 = "12345Best")

steen_system.add_product({
            "name": "Mario",
            "price": 219,
            "os_support": "WINDOW-MACOS-LINUX",
            "system_req": "2.4GHz-NVIDIA1050",
            "tags": "KUECHIARAI",
            "cover_image": None,
            "lang_sup": "Thai-Bangladesh-English-Japanese",
            "ban_country": None,
            "exc_country": "Thailand",
            "age_rate": "20+",
            "discount": 0,
            "description": "This is not suit you",
            "release_date": datetime.datetime.now()
            })
steen_system.add_product({
            "name": "Dog",
            "price": 399,
            "os_support": "WINDOW-MACOS",
            "system_req": "3.2GHz-NVIDIA3050",
            "tags": "KUECHIARAI",
            "cover_image": None,
            "lang_sup": "English-Japanese",
            "ban_country": None,
            "exc_country": None,
            "age_rate": "5+",
            "discount": 0,
            "description": "Play this till the end of da day",
            "release_date": datetime.datetime.now()
            })

print(steen_system.search_product("Mario"))