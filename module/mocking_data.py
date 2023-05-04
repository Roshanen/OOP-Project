from module.product import Product
from module.user import User


keys = ["name", "price", "os_support", "system_req",
        "pre_vid", "cover_image", "lang_sup",
        "age_rate", "discount", "description"]

fifa_23 = {
            "name": "EA SPORTS™ FIFA 23",
            "price": 1899.00,
            "os_support": [" Windows 10 64-bit"],
            "system_req":
            {
                "Processor": "Intel Core i5 6600k or AMD Ryzen 5 1600",
                "Memory": "8 GB RAM",
                "Graphics": "NVIDIA GeForce GTX 1050 Ti or AMD Radeon RX 570",
                "DirectX": "Version 12",
                "Storage": "100 GB available space"
            },
            "pre_vid" : "https://cdn.cloudflare.steamstatic.com/steam/apps/256942523/movie480_vp9.webm?t=1682117044",
            "cover_image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1811260/header.jpg?t=1682117049",
            "lang_sup": ["English", "French", "Italian", "German", "Spanish - Spain", "Arabic", "Czech", "Danish", "Dutch", "Japanese","Chinese", "Thai"],
            "age_rate": "Pegi 3",
            "discount": 0,
            "description": "FIFA 23 brings The World Game to the pitch, with HyperMotion2 Technology, mens and womens FIFA World Cup™coming during the season, womens club teams, cross-play features*, and more.",
            "release_date": [29, 9, 2022]
}
planet_zoo = {
            "name": "Planet Zoo",
            "price": 975.00,
            "os_support": [" Windows 7 (SP1+)/8.1/10 64bit"],
            "system_req":
            {
                "Processor": "Intel i5-2500 / AMD FX-6350",
                "Memory": "8 GB RAM",
                "Graphics": "NVIDIA GeForce GTX 770 (2GB) / AMD Radeon R9 270X (2GB)",
                "Additional Notes": "Minimum specifications may change during development",
                "Storage": "16 GB available space"
            },
            "pre_vid" : "https://cdn.cloudflare.steamstatic.com/steam/apps/256766382/movie480.webm?t=1572955356",
            "cover_image": "https://cdn.cloudflare.steamstatic.com/steam/apps/703080/header.jpg?t=1680775682",
            "lang_sup": ["English", "French", "Korean", "German", "Spanish - Spain", "Arabic", "Czech", "Danish", "Dutch", "Japanese","Chinese", "Dutch", "Norwegian", "Polish", "Russian", "Swedish"],
            "age_rate": "Pegi 3",
            "discount": 0,
            "description": "Build a world for wildlife in Planet Zoo. From the developers of Planet Coaster and Zoo Tycoon comes the ultimate zoo sim. Construct detailed habitats, manage your zoo, and meet authentic living animals who think, feel and explore the world you create around them.",
            "release_date": [5, 1, 2019]
}
sea_of_thieves_2023 = {
            "name": "Sea of Thieves 2023 Edition",
            "price": 129.00,
            "os_support": [" Windows 10"],
            "system_req":
            {
                "Processor": "Intel Q9450 @ 2.6GHz or AMD Phenom II X6 @ 3.3 GHz",
                "Memory": "4 GB RAM",
                "Graphics": "Nvidia GeForce GTX 650 or AMD Radeon 7750",
                "DirectX": "Version 11",
                "Storage": "50 GB available space"
            },
            "pre_vid" : "https://cdn.cloudflare.steamstatic.com/steam/apps/256936077/movie480_vp9.webm?t=1678968012",
            "cover_image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1172620/header.jpg?t=1682374543",
            "lang_sup": ["English", "French", "Iitalian", "German", "Spanish - Spain", "Protuguese-Brazil", "Russian", "Thai", "Turkish", "Japanese", "Polish"],
            "age_rate": "Pegi 12",
            "discount": 0,
            "description": "Celebrate five years since Sea of Thieves' launch with this special edition, including a copy of the game with all permanent content added since launch, plus a 10,000 gold bonus and a selection of Hunter cosmetics: the Hunter Cutlass, Pistol, Compass, Hat, Jacket and Sails.",
            "release_date": [3, 6, 2020]
}
xcom_2 = {
            "name": "XCOM® 2",
            "price": 1499.00,
            "os_support": [" Windows® 7, 64-bit"],
            "system_req":
            {
                "Processor": "Intel Core 2 Duo E4700 2.6 GHz or AMD Phenom 9950 Quad Core 2.6 GHz",
                "Memory": "4 GB RAM",
                "Graphics": "1GB ATI Radeon HD 5770, 1GB NVIDIA GeForce GTX 460 or better",
                "DirectX": "Version 11",
                "Storage": "45 GB available space",
                "Sound Card": "DirectX compatible sound card"
            },
            "pre_vid" : "https://cdn.cloudflare.steamstatic.com/steam/apps/256660486/movie480.webm?t=1454708337",
            "cover_image": "https://cdn.cloudflare.steamstatic.com/steam/apps/268500/header.jpg?t=1646157374",
            "lang_sup": ["English", "French", "Iitalian", "German", "Spanish - Spain", "Russian", "Japanese", "Polish", "Korean"],
            "age_rate": "Pegi 16",
            "discount": 0,
            "description": "XCOM 2 is the sequel to XCOM: Enemy Unknown, the 2012 award-winning strategy game of the year. Earth has changed and is now under alien rule. Facing impossible odds you must rebuild XCOM, and ignite a global resistance to reclaim our world and save humanity.",
            "release_date": [5, 2, 2016]
}
no_man_sky = {
            "name": "No Man's Sky",
            "price": 1100.00,
            "os_support": [" Windows 10/11 (64-bit versions)"],
            "system_req":
            {
                "Processor": "Intel Core i3",
                "Memory": "8 GB RAM",
                "Graphics": "Nvidia GTX 1060 3GB, AMD RX 470 4GB, Intel UHD graphics 630",
                "Storage": "15 GB available space",
                "VR Support": "SteamVR"
            },
            "pre_vid" : "https://cdn.cloudflare.steamstatic.com/steam/apps/256939398/movie480_vp9.webm?t=1680700853",
            "cover_image": "https://cdn.cloudflare.steamstatic.com/steam/apps/275850/header_alt_assets_17.jpg?t=1680700860",
            "lang_sup": ["English", "French", "Iitalian", "German", "Spanish - Spain", "Russian", "Japanese", "Polish", "Korean", "Dutch"],
            "age_rate": None,
            "discount": 0,
            "description": "No Man's Sky is a game about exploration and survival in an infinite procedurally generated universe.",
            "release_date": [12, 8, 2016]
}
contraband_police = {
            "name": "Contraband Police",
            "price": 400.00,
            "os_support": [" Windows 10 (64-bit versions only)"],
            "system_req":
            {
                "Processor": "Intel Core i5-6600 @ 3.3 GHz or AMD Ryzen 5 1600 @ 3.2 GHz or equivalent",
                "Memory": "12 GB RAM",
                "Graphics": "NVIDIA GeForce GTX 1050 or AMD RX 560 (3GB VRAM with Shader Model 5.0 or better)",
                "DirectX": "Version 11",
                "Storage": "12 GB available space"
            },
            "pre_vid" : "https://cdn.cloudflare.steamstatic.com/steam/apps/256934475/movie480_vp9.webm?t=1678273751",
            "cover_image": "https://cdn.cloudflare.steamstatic.com/steam/apps/756800/header.jpg?t=1682493533",
            "lang_sup": ["English", "French", "Iitalian", "German", "Spanish - Spain", "Russian", "Japanese", "Polish", "Korean", "Dutch", "Thai", "Ukrainian", "Traditional Chinese"],
            "age_rate": None,
            "discount": 0.15,
            "description": "Take over the duties of a border guard inspector in a communist country of the 80's. Smuggling, corruption and forgery are the order of the day here. Be vigilant and earn the respect of your superiors.",
            "release_date": [8, 3, 2023]
}
football_manager_2023 = {
            "name": "Football Manager 2023",
            "price": 1459.00,
            "os_support": [" Windows 7"],
            "system_req":
            {
                "Processor": "Intel Core 2 or AMD Athlon 64 X2",
                "Memory": "4 GB RAM",
                "Graphics": "Intel GMA X4500, NVIDIA GeForce 9600M GT, AMD/ATI Mobility Radeon HD 3650",
                "DirectX": "Version 11",
                "Storage": "7 GB available space"
            },
            "pre_vid" : "https://cdn.cloudflare.steamstatic.com/steam/apps/256932241/movie480_vp9.webm?t=1677520640",
            "cover_image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1904540/header.jpg?t=1680627762",
            "lang_sup": ["English", "French", "Iitalian", "German", "Spanish - Spain", "Russian", "Japanese", "Polish", "Korean", "Dutch", "Norwegian", "Greek", "Swedish", "Simplified Chinese"],
            "age_rate": "pegi 13",
            "discount": 0,
            "description": "Build your dream squad, outsmart your rivals and experience the thrill of big European nights in the UEFA Champions League. Your journey towards footballing glory awaits.",
            "release_date": [8, 11, 2022]
}
this_war_of_mine = {
            "name": "This War of Mine",
            "price": 400.00,
            "os_support": ["  Windows 7/8/10"],
            "system_req":
            {
                "Processor": "2.4 GHz Dual Core",
                "Memory": "2 GB RAM",
                "Graphics": "GeForce GTX 260, Radeon HD 5770, 1024 MB, Shader Model 3.0",
                "Sound Card": "DirectX compatible"
            },
            "pre_vid" : "https://cdn.cloudflare.steamstatic.com/steam/apps/256864956/movie480_vp9.webm?t=1639476352",
            "cover_image": "https://cdn.cloudflare.steamstatic.com/steam/apps/282070/header.jpg?t=1680610841",
            "lang_sup": ["English", "French", "Iitalian", "German", "Spanish - Spain", "Russian", "Japanese", "Portuguese - Brazil	", "Korean", "Turkish", "Simplified Chinese"],
            "age_rate": None,
            "discount": 0,
            "description": "In This War Of Mine you do not play as an elite soldier, rather a group of civilians trying to survive in a besieged city; struggling with lack of food, medicine and constant danger from snipers and hostile scavengers. The game provides an experience of war seen from an entirely new angle.",
            "release_date": [15, 11, 2014]
}
twelve_minutes = {
            "name": "Twelve Minutes",
            "price": 429.00,
            "os_support": [" Windows 7"],
            "system_req":
            {
                "Processor": "Intel Core i5-2300 | AMD Phenom II X4 965",
                "Memory": "2 GB RAM",
                "Graphics": "Nvidia GeForce GTS 450, 1 GB | AMD Radeon HD 5770, 1 GB"
            },
            "pre_vid" : "https://cdn.cloudflare.steamstatic.com/steam/apps/256847082/movie480_vp9.webm?t=1629391267",
            "cover_image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1097200/header.jpg?t=1660852645",
            "lang_sup": ["English", "French", "Iitalian", "German", "Spanish - Spain", "Russian", "Japanese", "Portuguese - Brazil	", "Korean", "Turkish", "Simplified Chinese", "Portuguese - Portugal"],
            "age_rate": None,
            "discount": 0,
            "description": "An interactive thriller about a man trapped in a time loop. Featuring James McAvoy, Daisy Ridley, and Willem Dafoe.",
            "release_date": [19, 8, 2021]
}
cyberpunk_2077 = {
            "name": "Cyberpunk 2077",
            "price": 1799.00,
            "os_support": [" Windows 10"],
            "system_req":
            {
                "Processor": " Intel Core i5-3570K or AMD FX-8310",
                "Memory": "8 GB RAM",
                "Graphics": "NVIDIA GeForce GTX 970 or AMD Radeon RX 470",
                "DirectX": "Version 12",
                "Storage": "70 GB available space",
                "Additional Notes": "In this game you will encounter a variety of visual effects that may provide seizures or loss of consciousness in a minority of people. If you or someone you know experiences any of the above symptoms while playing, stop and seek medical attention immediately."
            },
            "pre_vid" : "https://cdn.akamai.steamstatic.com/steam/apps/1091500/header.jpg?t=1680026109",
            "cover_image": "https://cdn.akamai.steamstatic.com/steam/apps/256904408/movie480_vp9.webm?t=1662480409",
            "lang_sup": ["English", "French", "Iitalian", "German", "Spanish - Spain", "Russian", "Japanese", "Portuguese - Brazil	", "Korean", "Turkish", "Hungarian", "Arabic", "Thai", "Czech"],
            "age_rate": "pegi 18",
            "discount": 0,
            "description": "Cyberpunk 2077 is an open-world, action-adventure RPG set in the dark future of Night City — a dangerous megalopolis obsessed with power, glamor, and ceaseless body modification.",
            "release_date": [10, 12, 2020]
}
detroit_become_human = {
            "name": "Detroit: Become Human",
            "price": 809.99,
            "os_support": [" Windows 10 (64 bit)"],
            "system_req":
            {
                "Processor": " Intel Core i5-2300 @ 2.8 GHz or AMD Ryzen 3 1200 @ 3.1GHz or AMD FX-8350 @ 4.2GHz",
                "Memory": "8 GB RAM",
                "Graphics": "Nvidia GeForce GTX 780 or AMD HD 7950 with 3GB VRAM minimum (Support of Vulkan 1.1 required)",
                "Storage": "55 GB available space"
            },
            "pre_vid" : "https://cdn.akamai.steamstatic.com/steam/apps/256784014/movie480_vp9.webm?t=1590429401",
            "cover_image": "https://cdn.akamai.steamstatic.com/steam/apps/1222140/header.jpg?t=1667468479",
            "lang_sup": ["English", "French", "Iitalian", "German", "Spanish - Spain", "Russian", "Japanese", "Portuguese - Brazil	", "Korean", "Turkish", "Hungarian", "Arabic", "Finnish", "Czech", "Spanish - Latin America	", "Norwegian"],
            "age_rate": "pegi 18",
            "discount": 0,
            "description": "Detroit: Become Human puts the destiny of both mankind and androids in your hands, taking you to a near future where machines have become more intelligent than humans. Every choice you make affects the outcome of the game, with one of the most intricately branching narratives ever created.",
            "release_date": [18, 6, 2020]
}
phasmophobia = {
            "name": "Phasmophobia",
            "price": 229.00,
            "os_support": ["Windows 10 64Bit"],
            "system_req":
            {
                "Processor": " Intel Core i5-4590 / AMD Ryzen 5 2600",
                "Memory": "8 GB RAM",
                "Graphics": "NVIDIA GTX 970 / AMD Radeon R9 390",
                "DirectX": "Version 11",
                "Storage": "21 GB available space",
                "VR Support": "OpenXR",
                "Additional Notes": "Minimum Specs are for VR, lower specs may work for Non-VR."
            },
            "pre_vid" : "https://cdn.akamai.steamstatic.com/steam/apps/256906135/movie480_vp9.webm?t=1663254571",
            "cover_image": "https://cdn.akamai.steamstatic.com/steam/apps/739630/header.jpg?t=1674232976",
            "lang_sup": ["English", "French", "Iitalian", "German", "Spanish - Spain", "Russian", "Japanese", "Portuguese - Brazil	", "Korean", "Turkish", "Hungarian", "Catalan", "Finnish", "Czech", "Ukrainian", "Norwegian", "Romanian"],
            "age_rate": None,
            "discount": 0,
            "description": "Phasmophobia is a 4 player online co-op psychological horror. Paranormal activity is on the rise and it’s up to you and your team to use all the ghost-hunting equipment at your disposal in order to gather as much evidence as you can.",
            "release_date": [19, 9, 2020]
}
grand_theft_auto_V = {
            "name": "Grand Theft Auto V",
            "price": 1587.00,
            "os_support": [" Windows 10 64 Bit, Windows 8.1 64 Bit, Windows 8 64 Bit, Windows 7 64 Bit Service Pack 1"],
            "system_req":
            {
                "Processor": "Intel Core 2 Quad CPU Q6600 @ 2.40GHz (4 CPUs) / AMD Phenom 9850 Quad-Core Processor (4 CPUs) @ 2.5GHz",
                "Memory": "4 GB RAM",
                "Graphics": "NVIDIA 9800 GT 1GB / AMD HD 4870 1GB (DX 10, 10.1, 11)",
                "Storage": "72 GB available space",
                "Sound Card": "100% DirectX 10 compatible"
            },
            "pre_vid" : "https://cdn.akamai.steamstatic.com/steam/apps/256921436/movie480_vp9.webm?t=1671116368",
            "cover_image": "https://cdn.akamai.steamstatic.com/steam/apps/271590/header.jpg?t=1678296348",
            "lang_sup": ["English", "Chinese", "French", "German", "Japanese", "Spanish", "Simplified Chinese", "Spanish - Latin America"],
            "age_rate": "Pegi 18",
            "discount": 0.67,
            "description": "Grand Theft Auto V for PC offers players the option to explore the award-winning world of Los Santos and Blaine County in resolutions of up to 4k and beyond, as well as the chance to experience the game running at 60 frames per second.",
            "release_date": [14, 4, 2015]
}
rainbow_six = {
            "name": "Tom Clancy's Rainbow Six® Siege",
            "price": 540.00,
            "os_support": ["Originally released for Windows 7, the game can be played on Windows 10 and Windows 11 OS"],
            "system_req":
            {
                "Processor": "Intel Core i3 560 @ 3.3 GHz or AMD Phenom II X4 945 @ 3.0 GHz",
                "Memory": "6 GB RAM",
                "Graphics": "NVIDIA GeForce GTX 460 or AMD Radeon HD 5870 (DirectX-11 compliant with 1GB of VRAM)",
                "Network": "Broadband Internet connection",
                "Storage": "61 GB available space",
                "Sound Card": "DirectX® 9.0c compatible sound card with latest drivers"
            },
            "pre_vid" : "https://cdn.akamai.steamstatic.com/steam/apps/256854738/movie480_vp9.webm?t=1633533753",
            "cover_image": "https://cdn.akamai.steamstatic.com/steam/apps/359550/header.jpg?t=1680010421",
            "lang_sup": ["English", "Chinese", "French", "German", "Japanese", "Thai", "Spanish", "Czech", "Dutch", "Polish", "Portuguese - Brazil", "Traditional Chinese"],
            "age_rate": "Pegi 18",
            "discount": 0.60,
            "description": "Tom Clancy's Rainbow Six® Siege is an elite, tactical team-based shooter where superior planning and execution triumph.",
            "release_date": [2, 12, 2015]
}
pubg = {
            "name": "PUBG: BATTLEGROUNDS",
            "price": 0,
            "os_support": ["64-bit Windows 10"],
            "system_req":
            {
                "Processor": "Intel Core i5-4430 / AMD FX-6300",
                "Memory": "8 GB RAM",
                "Graphics": "NVIDIA GeForce GTX 960 2GB / AMD Radeon R7 370 2GB",
                "Network": "Broadband Internet connection",
                "Storage": "40 GB available space",
                "DirectX": "Version 11"
            },
            "pre_vid" : "https://cdn.akamai.steamstatic.com/steam/apps/256868780/movie480_vp9.webm?t=1641965538",
            "cover_image": "https://cdn.akamai.steamstatic.com/steam/apps/578080/header.jpg?t=1681115546",
            "lang_sup": ["English", "Chinese", "French", "German", "Japanese", "Thai", "Spanish", "Czech", "Dutch", "Polish", "Portuguese - Brazil", "Traditional Chinese"],
            "age_rate": "Pegi 15",
            "discount": 0,
            "description": "Play PUBG: BATTLEGROUNDS for free. Land on strategic locations, loot weapons and supplies, and survive to become the last team standing across various, diverse Battlegrounds. Squad up and join the Battlegrounds for the original Battle Royale experience that only PUBG: BATTLEGROUNDS . ",
            "release_date": [21, 12, 2017]
}
let_build_a_zoo = {
            "name": "Let's Build a Zoo",
            "price": 249.00,
            "os_support": [" Windows 7 or later"],
            "system_req":
            {
                "Processor": "Intel Core i5",
                "Memory": "2 GB RAM",
                "Graphics": "NVIDIA GeForce GTX 550/equivalent or higher",
                "DirectX": "Version 10",
                "Storage": "738 MB available space"
            },
            "pre_vid" : "https://cdn.cloudflare.steamstatic.com/steam/apps/256859844/movie480_vp9.webm?t=1636563244",
            "cover_image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1547890/header_alt_assets_1.jpg?t=1681145279",
            "lang_sup": ["English", "Chinese", "French", "German", "Japanese", "THai", "Spanish"],
            "ban_country" : None,
            "exc_country": None,
            "age_rate": "Pegi 7",
            "discount": 0.45,
            "description": "It's time to build a zoo! Let out your wild side, and create your own animal empire with this cute, expansive management sim. Import and breed rare creatures, hire the right staff, keep your visitors happy, and deal with plenty of weird and wonderful events. Then try your hand at DNA Splicing, and stitch together over 300,000 different types of animal, ranging from the majestic Giraffephant to the peaceful PandOwl!",
            "release_date": [5, 11, 2021]
}
tribes_of_midgard = {
            "name": "Tribes of Midgard",
            "price": 369.00,
            "os_support": ["Windows 7 64 Bits"],
            "system_req":
            {
                "Processor": "Intel Quad Core i5-2300 or AMD FX-6300",
                "Memory": "8 GB RAM",
                "Graphics": "Nvidia GeForce GTX 560 (1GB) or AMD Radeon HD 7770 (1GB)",
                "DirectX": "Version 11",
                "Network": "Broadband Internet connection",
                "Storage": "8 GB available space",
                "Sound Card": "DirectX® Compatible"
            },
            "pre_vid" : "https://cdn.cloudflare.steamstatic.com/steam/apps/570/ss_ad8eee787704745ccdecdfde3a5cd2733704898d.600x338.jpg?t=1678300512",
            "cover_image": "https://cdn.cloudflare.steamstatic.com/steam/apps/858820/header.jpg?t=1681224766",
            "lang_sup": ['English', 'French', 'Spanish-Spain', 'Dutch', 'Portuguese-Portugal', 'Russian', 'Ukrainian', 'Italian', 'German', 'Japanese', 'Korean', 'Polish', 'Portuguese-Brazil', 'SimplifiedChinese', 'Swedish', 'Thai', 'TraditionalChinese', 'Turkish', 'Afrikaans'],
            "ban_country" : None,
            "exc_country": None,
            "age_rate": "Pegi 12",
            "discount": 0.6,
            "description": "Tribes of Midgard’s Valhalla Saga update is HERE! This Saga represents the culmination of the Einherjar’s fate-defying quest to stop Ragnarök. Mount up and journey across Midgard (and beyond!) in this epic Survival ARPG adventure. Build, craft, and explore, as you fight your way through towering creatures of legend to discover the secrets of the Sanctuary stones. Valhalla awaits, Einherjar!",
            "release_date": [28, 7, 2021]
}
dota_2 = {
            "name": "Dota 2",
            "price": 0,
            "os_support": ["Windows 7 or newer"],
            "system_req":
            {
                'Processor': 'Dual core from Intel or AMD at 2.8 GHz',
                'Memory': '4 GB RAM',
                'Graphics': 'NVIDIA GeForce 8600/9600GT, ATI/AMD Radeon HD2600/3600',
                'DirectX': 'Version 11',
                'Network': 'Broadband Internet connection',
                'Storage': '60 GB available space',
                'Sound Card': 'DirectX Compatible'
            },
            "pre_vid" : "https://cdn.cloudflare.steamstatic.com/steam/apps/256692021/movie_max.webm?t=1599609272",
            "cover_image": "https://cdn.cloudflare.steamstatic.com/steam/apps/570/header.jpg?t=1682639497",
            "lang_sup": ['English', 'Bulgarian', 'Czech', 'Danish', 'Dutch', 'Finnish', 'French', 'German', 'Greek', 'Hungarian', 'Italian', 'Japanese', 'Korean', 'Norwegian', 'Polish', 'Portuguese-Portugal', 'Portuguese-Brazil', 'Romanian', 'Russian', 'SimplifiedChinese', 'Spanish-Spain', 'Swedish', 'Thai', 'TraditionalChinese', 'Turkish', 'Ukrainian', 'Spanish-LatinAmerica', 'Vietnamese'],
            "age_rate": "Pegi 12",
            "discount": 0,
            "description":
            """The most-played game on Steam.
Every day, millions of players worldwide enter battle as one of over a hundred Dota heroes. And no matter if it's their 10th hour of play or 1,000th, there's always something new to discover. With regular updates that ensure a constant evolution of gameplay, features, and heroes, Dota 2 has truly taken on a life of its own.
One Battlefield. Infinite Possibilities.
When it comes to diversity of heroes, abilities, and powerful items, Dota boasts an endless array—no two games are the same. Any hero can fill multiple roles, and there's an abundance of items to help meet the needs of each game. Dota doesn't provide limitations on how to play, it empowers you to express your own style.
All heroes are free.
Competitive balance is Dota's crown jewel, and to ensure everyone is playing on an even field, the core content of the game—like the vast pool of heroes—is available to all players. Fans can collect cosmetics for heroes and fun add-ons for the world they inhabit, but everything you need to play is already included before you join your first match.
Bring your friends and party up.
Dota is deep, and constantly evolving, but it's never too late to join.
Learn the ropes playing co-op vs. bots. Sharpen your skills in the hero demo mode. Jump into the behavior- and skill-based matchmaking system that ensures you'll
be matched with the right players each game.""",
            "release_date": [10, 7, 2013]
}

all_product_info = [fifa_23, planet_zoo, sea_of_thieves_2023, xcom_2, no_man_sky, contraband_police,
               football_manager_2023, this_war_of_mine, twelve_minutes, cyberpunk_2077,
               detroit_become_human, phasmophobia, grand_theft_auto_V, rainbow_six,
               pubg, let_build_a_zoo, tribes_of_midgard, dota_2]