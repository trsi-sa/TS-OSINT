try:
    import os, requests, json, time, sys, praw, socket, ipaddress, platform, psutil, subprocess, shutil, PIL.Image, PIL.ExifTags, cv2, concurrent.futures, hashlib
    from PIL import Image
    from PIL.ExifTags import TAGS, GPSTAGS
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from rich.console import Console
    from rich.table import Table    
    import phonenumbers
    from search_engines import Google, Bing, Brave
    from bs4 import BeautifulSoup
    from datetime import datetime
    from telethon.sync import TelegramClient
    from binascii import hexlify
    from phonenumbers import geocoder, carrier, timezone
    from googlesearch import search
except ModuleNotFoundError:
    os.system("pip install requests praw ipaddress psutil pillow opencv-python selenium rich phonenumbers bs4 telethon googlesearch-python")
   
    os.system("clear")

Black = "\033[1;30m"
Red = "\033[1;31m"
Green = "\033[1;32m"
Yellow = "\033[1;33m"
Blue = "\033[1;34m"
Purple = "\033[1;35m"
Cyan = "\033[1;36m"
White = "\033[1;37m"
Gray = "\033[1;39m"
DarkRed = "\033[2;31m"
DarkBlue = "\033[2;34m"
DarkPink = "\033[2;35m"
DarkCyan = "\033[2;36m"

print("""\033[1;34m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⠀⠀⠀⢢⠀⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⢣⡀⠀⠀⠀⢣⢀⠀⠘⡆⢸⡀⠀⢢⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢄⠑⣄⠀⢻⠀⠀⠀⠘⡌⡆⠀⡇⢸⡇⠀⢸⡀⡆⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⠼⣷⠼⡦⣼⣯⣧⣀⢰⡇⡇⢰⠇⣼⢳⠀⢸⡇⡇⠀⢸⡇⠀⡄⠀⢰⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⠿⠛⢉⡈⢧⡀⣸⡆⣇⣿⠃⣿⢀⣿⣻⢷⣿⣴⣇⡿⢀⣾⢠⡇⢀⣿⠀⢰⠃⠀⡜⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡿⠋⢡⡀⠙⣦⠹⣎⣧⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣾⣿⣿⣳⣿⣧⡿⣠⣾⡿⢀⢎⠀⡼⢁⠂⠀⡐⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⠟⠉⠀⠀⢠⠹⣿⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣵⡷⣫⣾⠞⣡⠏⣠⡞⠀⣠⡆
⠀⠀⠀⠀⠀⣠⡿⠋⠀⠀⠠⣱⣄⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣷⣾⣯⣶⣿⡿⠃
⠀⠀⠀⠀⣴⠟⠁⠀⢤⡱⣄⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⡿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠀⠀
⠀⠀⠀⣼⠋⠀⠀⣝⢦⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣷⣂⡙⣿⣿⡇⠀⠀⠀⠀⠀⠈⢉⣿⣿⣿⣿⣿⣿⠿⢿⣄⠀⠀⠀⠀⠀
⠀⠀⣼⠃⠀⠀⠤⣬⣿⣿⣿⣿⣿⡉⣿⣿⣄⣼⣿⣿⣿⣿⡟⠉⠀⢿⣿⡿⠀⠀⠀⠀⠀⢠⣾⣿⠿⠿⠿⠿⣟⡳⠄⠉⠀⠀⠀⠀⠀
⠀⣸⠃⠀⠀⢀⣾⣿⣿⠟⠋⢿⣥⡬⠙⣿⣿⣿⣿⣿⣿⡧⠀⠀⢲⣄⣿⠇⠀⠀⠀⢀⣴⣿⣿⣿⡿⣛⣓⠲⢤⡉⠀⠀⠀⠀⠀⠀⠀
⢰⠃⠀⠀⣠⣿⣿⠟⠁⠀⠀⠘⢿⣔⣢⡴⠛⠙⠛⠛⢁⠀⢠⣾⣦⣿⠏⠀⠀⢀⣴⣿⣿⣿⣯⡭⢍⡒⢌⠙⠦⡈⢢⡀⠀⠀⠀⠀⠀
⠁⠀⠀⣰⣿⡿⠁⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣄⣴⣷⣾⣷⣤⣿⠟⠁⠀⣠⣴⣿⣿⣿⣿⣾⣍⡻⡄⠈⠳⡅⠀⠈⠂⠀⠀⠀⠀⠀⠀
⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠉⠉⣀⣠⣶⣿⣿⣿⣿⣿⡿⢿⣿⣮⠙⢦⠀⠀⠈⠆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣸⠟⠁⠀⢀⣠⣤⣶⡶⢶⣶⣶⣦⣤⣤⣤⣤⣤⣶⣶⣾⣿⣿⣿⡿⢿⡿⣝⢫⡻⣍⠳⣝⢻⢧⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣰⠋⢀⣴⠞⠋⠉⠠⠋⠠⢋⠞⣹⢻⠏⢸⠉⡏⡿⢹⢿⢻⣿⢿⣿⡿⣦⠹⡈⠳⡘⡈⢣⠘⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠈⠀⠃⠀⠀⠘⠀⠀⡇⡜⠈⡸⢸⠀⢹⢸⠈⢆⠁⠀⢱⠁⠀⢇⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠘⠀⠘⠀⠀⢸⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           
                    \033[1;32mv1.2.2\033[1;37m

THIS TOOL WAS PROGRAMMED BY TLER AL-SHAHRANI.
PERSONAL WEBSITE : \033[1;34mhttps://tlersa.github.io/tleralshahrani/Index.html""")
print("\033[1;37m- "*35)

def main_menu():
    print("""\033[1;37m[\033[1;34m01\033[1;37m] - Dorks                  [\033[1;34m11\033[1;37m] - Deep & Dark Web
[\033[1;34m02\033[1;37m] - Search for Username    [\033[1;34m12\033[1;37m] - Monitor cameras
[\033[1;34m03\033[1;37m] - Usernames OSINT        [\033[1;34m13\033[1;37m] - WebScraping
[\033[1;34m04\033[1;37m] - Domains OSINT          [\033[1;34m14\033[1;37m] - Israeli databases \U0001F923
[\033[1;34m05\033[1;37m] - IP's OSINT             [\033[1;34m15\033[1;37m] - Verify passwords leakage
[\033[1;34m06\033[1;37m] - Networks OSINT
[\033[1;34m07\033[1;37m] - Images OSINT            
[\033[1;34m08\033[1;37m] - PhoneNumbers OSINT
[\033[1;34m09\033[1;37m] - Search engine
[\033[1;34m10\033[1;37m] - Ports scan

[\033[1;34m98\033[1;37m] - Report bug
[\033[1;34m99\033[1;37m] - Help
[\033[1;34m00\033[1;37m] - Exit""")

def submenu1():
    print("""\033[1;37m[\033[1;34m01\033[1;37m] - Instagram
[\033[1;34m02\033[1;37m] - Telegram accs
[\033[1;34m03\033[1;37m] - TikTok
[\033[1;34m04\033[1;37m] - Github
[\033[1;34m05\033[1;37m] - Reddit
[\033[1;34m06\033[1;37m] - Tellonym

[\033[1;34m99\033[1;37m] - Back""")

def submenu2():
    print("""\033[1;37m[\033[1;34m01\033[1;37m] - PhoneNumbers OSINT
[\033[1;34m02\033[1;37m] - Search for the owner of the num by name

[\033[1;34m99\033[1;37m] - Back""")

def submenu3():
    print("""\033[1;37m[\033[1;34m01\033[1;37m] - Networks OSINT
[\033[1;34m02\033[1;37m] - Show network operations

[\033[1;34m99\033[1;37m] - Back""")

def submenu4():
    print("""\033[1;37m[\033[1;34m01\033[1;37m] - Cameras around the world
[\033[1;34m02\033[1;37m] - Cameras of places

[\033[1;34m99\033[1;37m] - Back""")

def handle_selection(selection):
    if selection == "1" or selection == "01" or selection == "Dorks" or selection == "DORKS" or selection == "dorks":
        class dorks():
            def __init__(self):
                self.fristname = None
                self.FName = None
                self.GFName = None
                self.lastname = None
                self.output = ""
                self.admin()

            def set_info(self):
                fristname = input("\n\033[1;37m[\033[1;34m+\033[1;37m] FristName/Nickname : \033[1;34m")
                FName = input("\033[1;37m[\033[1;34m+\033[1;37m] Father name : \033[1;34m")
                GFName = input("\033[1;37m[\033[1;34m+\033[1;37m] GrandFather name : \033[1;34m")
                lastname = input("\033[1;37m[\033[1;34m+\033[1;37m] Last/Family/Tribe name : \033[1;34m")

                if fristname == "" or fristname == " ": self.fristname = False
                else: self.fristname = fristname

                if FName == "" or FName == " ": self.FName = False
                else: self.FName = FName

                if GFName == "" or GFName == " ": self.GFName = False
                else: self.GFName = GFName

                if lastname == "" or lastname == " ": self.lastname = False
                else: self.lastname = lastname

                if self.FName and self.fristname and self.GFName and self.lastname is None:
                    input("\033[1;31mPlease add at least fristname!\033[1;37m")
                    exit()

            def admin(self):
                self.set_info()
                print("\n\033[1;37m[ Searching in internet browsers... ]")
                space = " "

                if self.fristname:
                    sql = self.fristname + space
                    self.search_google(sql)
                    self.search_bing(sql)
                    self.search_brave(sql)

                if self.fristname and self.FName:
                    sql = self.fristname + space + self.FName
                    self.search_google(sql)
                    self.search_bing(sql)
                    self.search_brave(sql)

                if self.fristname and self.GFName:
                    sql = self.fristname + space + self.GFName
                    self.search_google(sql)
                    self.search_bing(sql)
                    self.search_brave(sql)

                if self.fristname and self.lastname:
                    sql = self.fristname + space + self.lastname
                    self.search_google(sql)
                    self.search_bing(sql)
                    self.search_brave(sql)
             
                if self.fristname and self.FName and self.lastname:
                    sql = self.fristname + space + self.FName + space + self.lastname
                    self.search_google(sql)
                    self.search_bing(sql)
                    self.search_brave(sql)

                if self.fristname and self.GFName and self.lastname:
                    sql = self.fristname + space + self.GFName + space + self.lastname
                    self.search_google(sql)
                    self.search_bing(sql)
                    self.search_brave(sql)                    

                if self.fristname and self.FName and self.GFName and self.lastname:
                    sql = self.fristname + space + self.FName + space + self.GFName + space + self.lastname
                    self.search_google(sql)
                    self.search_bing(sql)
                    self.search_brave(sql)

                self.save()

            def add_info(self, link, title, text, _from): self.output += f"""[-] Link : {link}
[-] Title : {title}
[-] Text : {text}
[-] From : {_from}\n\n"""

            def search_google(self, sql):
                engine = Google()
                results = engine.search(sql, pages=3)
                seen = set()
                for data in results.__dict__['_results']:
                    text = data['text']
                    if text not in seen:
                        link = data['link']
                        title = data['title']
                        self.add_info(link, title, text, "Google")
                        seen.add(text)
                print("[\033[1;32m✓\033[1;37m] Done Search in Google")

            def search_bing(self, sql):
                engine = Bing()
                results = engine.search(sql, pages=3)
                seen = set()
                for data in results.__dict__['_results']:
                    text = data['text']
                    if text not in seen:
                        link = data['link']
                        title = data['title']
                        self.add_info(link, title, text, "Google")
                        seen.add(text)
                print("[\033[1;32m✓\033[1;37m] Done Search in Bing")

            def search_brave(self, sql):
                engine = Brave()
                results = engine.search(sql, pages=3)
                seen = set()
                for data in results.__dict__['_results']:
                    text = data['text']
                    if text not in seen:
                        link = data['link']
                        title = data['title']
                        self.add_info(link, title, text, "Google")
                        seen.add(text)
                print("[\033[1;32m✓\033[1;37m] Done Search in Brave")

            def save(self):
                with open(f"Dorks results.txt", "wt", encoding="utf-8") as F: F.write(self.output)
                F.close()
                print(f"\n\033[1;37m[\033[1;32m✓\033[1;37m] The results has been saved in \033[1;34m{ os.getcwd()}\Dorks results.txt\033[1;37m")
        dorks()

        another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else: 
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()
    elif selection == "2" or selection == "02" or selection == "Search for Username" or selection == "search for username" or selection == "SEARCH FOR USERNAME":
        def search_social_media(username):
            websites = {
                "FaceBook": f"https://www.facebook.com/public/{username}/",
                "Instagram": f"https://instagram.com/{username}/",
                "YouTube": f"https://www.youtube.com/@{username}/",            
                "TikTok": f"https://www.tiktok.com/@{username}/",
                "Kwai": f"https://www.kwai.com/@{username}/",            
                "SnapChat": f"https://www.snapchat.com/add/{username}/",
                "Telegram": f"https://t.me/{username}/",
                "Spotify": f"https://open.spotify.com/user/{username}/",            
                "X": f"https://twitter.com/{username}/",
                "Pinterest": f"https://in.pinterest.com/{username}/",
                "Reddit": f"https://www.reddit.com/user/{username}/",
                "Tumblr": f"https://tumblr.com/{username}/",
                "Google+": f"https://plus.google.com/s/{username}/top/",
                "Weibo": f"https://weibo.com/u/{username}/",     
                "Badoo": f"https://www.badoo.com/en/{username}/",
                "Behance": f"https://www.behance.net/{username}/",
                "Dribbble": f"https://dribbble.com/{username}/",
                "Kuaishou": f"https://www.kuaishou.com/profile/{username}/",
                "YY": f"https://www.yy.com/u/{username}/",
                "Quora": f"https://www.quora.com/profile/{username}/",     
                "Tieba Baidu": f"https://tieba.baidu.com/f?kw={username}/", 
                "Imgur": f"https://imgur.com/user/{username}/",
                "PayPal": f"https://www.paypal.com/paypalme/{username}/",
                "Vimeo": f"https://vimeo.com/{username}/",      
                "Discord": f"https://discord.gg/{username}/",
                "Likee": f"https://l.likee.video/p/{username}/",
                "PicsArt": f"https://picsart.com/{username}/",
                "Twitch": f"https://www.twitch.tv/{username}/",
                "Linkedin": f"https://www.linkedin.com/in/{username}/",
                "Threads": f"https://www.threads.net/@{username}/",
                "Medium": f"https://medium.com/@{username}/",                    
                "Stack Exchange": f"https://academia.stackexchange.com/users/{username}/",
                "Wattpad": f"https://www.wattpad.com/user/{username}/",
                "SoundCloud": f"https://soundcloud.com/{username}/",
                "Deviantart": f"https://www.deviantart.com/{username}/",
                "YuboLive": f"https://www.deviantart.com/{username}/",
                "Tinder": f"https://tinder.com/app/profile/{username}/",
                "Wordpress": f"https://wordpress.com/{username}/",
                "NextDoor": f"https://nextdoor.com/profile/{username}/",
                "Triller": f"https://triller.co/@{username}/",
                "Flickr": f"https://www.flickr.com/people/{username}/",
                "Foursquare": f"https://foursquare.com/user/{username}/",          
                "Steam": f"https://steamcommunity.com/id/{username}/",
                "Roblox": f"https://www.roblox.com/user.aspx?username={username}/",
                "Fotolog": f"https://fotolog.com/{username}/",
                "Gaiaonline": f"https://www.gaiaonline.com/profiles/{username}/",       
                "Myspace": f"https://myspace.com/{username}/",
                "Replit": f"https://replit.com/@{username}/",
                "Tagged": f"https://www.tagged.com/{username}/",
                "Mixi": f"https://mixi.jp/view_community.pl?id= {username}/",
                "Crunchyroll": f"https://www.crunchyroll.com/{username}/",
                "Meetup": f"https://www.meetup.com/{username}/",
                "Tellonym": f"https://tellonym.me/{username}/",
                "Pastebin": f"https://pastebin.com/u/{username}/",
                "Github": f"https://github.com/{username}/",
                "Gitlab": f"https://gitlab.com/{username}/",
                "Wikipedia": f"https://www.wikipedia.org/wiki/User:{username}/",
                "Udemy": f"https://www.udemy.com/user/{username}/",
                "Canva": f"https://www.canva.com/{username}/",
                "Portswigger": f"https://portswigger.net/users//{username}",
                "DokanTip": f"https://tip.dokan.sa/{username}/",
                "Harmash": f"https://harmash.com/users/{username}/" }

            found_sites = []
            for site, url in websites.items():
                response = requests.get(url)
                if response.status_code == 200:
                    time.sleep(0.5)
                    print(f"\033[1;37m[\033[1;32m✔\033[1;37m] {site} : Found - \033[1;33m{url}")
                    found_sites.append(f"{site} : {url}")
                else: print(f"\033[1;37m[\033[1;31m✕\033[1;37m] {site} Not Found")

            print("\n\033[1;37m[\033[1;32m✓\033[1;37m] Done search in 61 social media!")

            return found_sites

        def save_results(results):
            with open(f"search_social_media_results.txt", "wt") as F:
                for i, result in enumerate(results, start=1): F.write(f"{i}- {result}\n")
            F.close()
            print(f"\033[1;37m[\033[1;32m✓\033[1;37m] The results has been saved in \033[1;34m{ os.getcwd()}\search social media results.txt\033[1;37m")

        username = input("\033[1;37m[\033[1;34m+\033[1;37m] Enter username/nickname target : \033[1;34m@")
        print(f"\033[1;37mSearch for \033[1;34m@{username}\033[1;37m in\n")
        time.sleep(3)

        results = search_social_media(username)

        save_to_file = input("\n\033[1;37mDo you want to save it to a file? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
        if save_to_file == "Y" or save_to_file == "y" or save_to_file == "Yes" or save_to_file == "yes" or save_to_file == "YES": save_results(results)
        elif save_to_file == "N" or save_to_file == "n" or save_to_file == "No" or save_to_file == "no" or save_to_file == "No": exit()
        else: print("\033[1;31mPlease choose a valid option!\033[1;37m")
        
        another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else: 
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()
    elif selection == "3" or selection == "03" or selection == "Usernames OSINT" or selection == "usernames OSINT" or selection == "USERNAMES OSINT" or selection == "usernames osint":
        submenu1()
        user_input = input("Choose : \033[1;34m")

        if user_input == "1" or user_input == "01" or user_input == "Instagram" or user_input == "instagram" or user_input == "INSTAGRAM" or user_input == "Insta" or user_input == "insta" or user_input == "INSTA":
            class Insta:
                def __init__(self, username):
                    self.username = username
                    
                    print("\033[1;37mGetting info...")
                    self.iguser()

                def iguser(self):
                    r = requests.get(f"https://api.givtt.com/api/ig/info_username/{self.username}", allow_redirects=False, timeout=50)

                    if "error" in r.text and r.json()["error"] is True:
                        if r.json()["message"] == "==": return self.run()
                        input(f"\033[1;31mError {r.json()['message']}\033[1;37m")
                        exit()
                    else: 
                        print(f"\033[1;37m[ Get info for \033[1;34m@{self.username} \033[1;37m]\n")

                        result = r.json()["result"]

                        table = Table(title="")
                        table.add_column("Info", no_wrap=True)
                        table.add_column("Acc")
                        table.add_row("ID", str(result["username_id"]))
                        table.add_row("Is business acc?", str("Yes" if result["business_account"] else "No"))
                        table.add_row("Is verified acc?", str("Yes" if result["verified_account"] else "No"))
                        table.add_row("Is private acc?", str("Yes" if result["private_account"] else "No"))
                        table.add_row("Is memorialized acc?", str("Yes" if result.get("is_memorialized")else "No"))
                        table.add_row("Is new acc?", str("Yes" if result["is_new_account"] is True else "No"))
                        table.add_row("User have another acc?", str("Yes" if result["user_have_another_account"] is True else "No"))
                        table.add_row("User have Threads acc?", str("Yes" if result["has_threads"] is True else "No"))
                        table.add_row("Username", str("@"+result["username"]))
                        table.add_row("Nickname", str(result["name"]))
                        table.add_row("Avater", str(result["profile_pic"]))
                        table.add_row("Location", str(result.get("account_region", "")))
                        table.add_row("Is in Canada?", str("Yes" if result.get("is_in_canada") else "No"))
                        table.add_row("Followers", str(result["followers"]))
                        table.add_row("Following", str(result["following"]))
                        table.add_row("Posts", str(result["media_count"]))
                        table.add_row("Has videos?", str("Yes" if result.get("has_videos", "None") else "No"))
                        table.add_row("IGTV videos", str(result["total_igtv_videos"]))
                        table.add_row("Bio", str(result["bio"]))
                        table.add_row("Bio link", str(result["external_url"]))
                        table.add_row("Public email", str(result.get("public_email", "None")))
                        table.add_row("Public phonenumber", str(result.get("public_phone_number", "None")))
                        table.add_row("Create", str(result.get("create_time", "")))
                        table.add_row("Lst change avatar", str(result["last_time_edit_avatar"]))
                        Console().print(table, justify="left")

            username = input("\033[1;37m[\033[1;34m+\033[1;37m] Enter username target : \033[1;34m@")
            Insta(username)

            another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else: 
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()
        elif user_input == "2" or user_input == "02" or user_input == "Telegram" or user_input == "telegram" or user_input == "TELEGRAM" or user_input == "Tele" or user_input == "TELE" or user_input == "tele":
            api_id = input("\033[1;37m[\033[1;34m+\033[1;37m] - Enter your API ID : \033[1;34m")
            api_hash = input("\033[1;37m[\033[1;34m+\033[1;37m] - Enter your API hash : \033[1;34m")

            client = TelegramClient('session_name', api_id, api_hash)

            async def main():
                await client.start()
                username = input("\033[1;37m[\033[1;34m+\033[1;37m] - Enter username/phonenumber target : \033[1;34m@")
                
                print("\033[1;37mGetting info...")
                time.sleep(3)
                print(f"\033[1;37m[ Get info for \033[1;34m@{username} \033[1;37m]\n")

                try:
                    username = await client.get_entity(username)

                    table = Table(title="")
                    table.add_column("Info", no_wrap=True)
                    table.add_column("Acc")
                    table.add_row("ID", str(username.id))
                    table.add_row("Username", str("@"+username.username))
                    table.add_row("Fristname", str(username.first_name))
                    table.add_row("Lastname", str(username.last_name))
                    table.add_row("Phonenumber", str(username.phone))
                    Console().print(table, justify="left")

                except Exception as e:
                    print(f"\033[1;31mErorr : {e}!\033[1;37m")

                await client.disconnect()

            if __name__ == '__main__':
                import asyncio
                asyncio.run(main())

            another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else: 
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()
        elif user_input == "3" or user_input == "03" or user_input == "TikTok" or user_input == "TIKTOK" or user_input == "tiktok" or user_input == "Tik" or user_input == "TIK" or user_input == "tik":
            class Tik:
                def __init__(self, username: str):
                    self.username = username
                    self.json_data = None

                    if "@" in self.username: self.username = self.username.replace("@", "")

                    self.admin()

                def admin(self):
                    self.send_request()
                    self.output()

                def send_request(self):
                    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0"}
                    r = requests.get(f"https://www.tiktok.com/@{self.username}", headers=headers)

                    try:
                        soup = BeautifulSoup(r.text, 'html.parser')
                        script_tag = soup.find('script', {'id': '__UNIVERSAL_DATA_FOR_REHYDRATION__'})
                        script_text = script_tag.text.strip()
                        self.json_data = json.loads(script_text)["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]
                    except:
                        print("\033[1;31mError : Username not found!\033[1;37m")

                def get_user_id(self):
                    try: return str(self.json_data["user"]["id"])
                    except IndexError: return "Unknown"

                def get_name(self):
                    try: return self.json_data["user"]["nickname"]
                    except IndexError: return "Unknown"

                def is_verified(self):
                    try:
                        check = self.json_data["user"]["verified"]
                        if check == "false" or check is False: return "No"
                        else: return "Yes"
                    except: return "Unknown"

                def secUid(self):
                    try: return self.json_data["user"]["secUid"]
                    except: return "Unknown"

                def is_private(self):
                    try:
                        check = self.json_data["user"]["privateAccount"]
                        if check == "true" or check is True: return "Yes"
                        else: return "No"
                    except: return "Unknown"

                def followers(self):
                    try: return self.json_data["stats"]["followerCount"]
                    except: return "Unknown"

                def following(self):
                    try: return self.json_data["stats"]["followingCount"]
                    except: return "Unknown"

                def user_create_time(self):
                    try:
                        url_id = int(self.get_user_id())
                        binary = "{0:b}".format(url_id)
                        i = 0
                        bits = ""
                        while i < 31:
                            bits += binary[i]
                            i += 1
                        timestamp = int(bits, 2)
                        dt_object = datetime.fromtimestamp(timestamp)
                        return dt_object
                    except: return "Unknown"

                def last_change_name(self):
                    try:
                        time = self.json_data["user"]["nickNameModifyTime"]
                        check = datetime.fromtimestamp(int(time))
                        return check
                    except: return "Unknown"

                def account_region(self):
                    try: return self.json_data["user"]["region"]
                    except: return "Unknown"

                def video_count(self):
                    try: return self.json_data["stats"]["videoCount"]
                    except: return "Unknown"

                def open_favorite(self):
                    try:
                        check = self.json_data["user"]["openFavorite"]
                        if check is False or check == "false": return "No"
                        return "Yes"
                    except: return "Unknown"

                def see_following(self):
                    try:
                        check = str(self.json_data["user"]["followingVisibility"])
                        if check == "1": return "Yes"
                        return "No"
                    except: return "Unknown"

                def language(self):
                    try: return str(self.json_data["user"]["language"])
                    except: return "Unknown"

                def heart_count(self):
                    try: return str(self.json_data["stats"]["heart"])
                    except: return "Unknown"

                def output(self):
                    print(f"\033[1;37m[ Get info for \033[1;34m@{self.username} \033[1;37m]\n")

                    table = Table(title="")
                    table.add_column("Info", no_wrap=True)
                    table.add_column("Acc")
                    table.add_row("ID", str(self.get_user_id()))
                    table.add_row("SecUid", str(self.secUid()))
                    table.add_row("is verified?", str(self.is_verified()))
                    table.add_row("is private?", str(self.is_private()))
                    table.add_row("Username", str("@"+self.username))
                    table.add_row("Nickname", str(self.get_name()))
                    table.add_row("Location", str(self.account_region()))
                    table.add_row("Followers", str(self.followers()))
                    table.add_row("Following", str(self.following()))
                    table.add_row("Can see following list?", str(self.see_following()))
                    table.add_row("Videos", str(self.video_count()))
                    table.add_row("Likes", str(self.heart_count()))
                    table.add_row("Open Fav?", str(self.open_favorite()))
                    table.add_row("Language", str(self.language()))
                    table.add_row("Create", str(self.user_create_time()))
                    table.add_row("Last change nickname", str(self.last_change_name()))
                    Console().print(table, justify="left")

            username = input("\033[1;37m[\033[1;34m+\033[1;37m] Enter username target : \033[1;34m@")
            
            print("\033[1;37mGetting info...")
            time.sleep(3)
            Tik(username)

            another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else: 
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()
        elif user_input == "4" or user_input == "04" or user_input == "GitHub" or user_input == "Github" or user_input == "github" or user_input == "GITHUB":
            class Github:
                def __init__(self):
                    self.Start()
                
                def Start(self):
                    self.username = input("\033[1;37m[\033[1;34m+\033[1;37m] Enter username target : \033[1;34m@")
                    
                    print("\033[1;37mGetting info...")
                    time.sleep(3)
                    print(f"\033[1;37m[ Get info for \033[1;34m@{self.username} \033[1;37m]\n")
                    
                    try:
                        self.Get = requests.get('https://api.github.com/users/%s'%(self.username))
                        self.Req = json.loads(self.Get.text)
                        table = Table(title="")
                        table.add_column("Info", no_wrap=True)
                        table.add_column("Acc")
                        table.add_row("ID", str(self.Req['node_id']))
                        table.add_row("Type", str(self.Req['type']))
                        table.add_row("Username", str("@"+self.Req['login']))
                        table.add_row("Acc link", str(self.Req['html_url']))
                        table.add_row("Nickname", str(self.Req['name']))
                        table.add_row("Company", str(self.Req['company']))
                        table.add_row("Bio", str(self.Req['bio']))
                        table.add_row("Public email", str(self.Req['email'] if self.Req['email'] else "No"))
                        table.add_row("Bio link", str(self.Req['blog']))
                        table.add_row("X link", str(self.Req['twitter_username'] if self.Req['twitter_username'] else "No"))
                        table.add_row("Avatar", str(self.Req['avatar_url']))
                        table.add_row("Location", str(self.Req['location']))
                        table.add_row("Followers", str(self.Req['followers']))
                        table.add_row("Following", str(self.Req['following']))
                        table.add_row("Public repos", str(self.Req['public_repos']))
                        table.add_row("Public gists", str(self.Req['public_gists']))
                        table.add_row("Create", str(self.Req['created_at']))
                        table.add_row("Hireable", str("Yes" if self.Req['hireable'] else "No"))
                        table.add_row("Last updated", str(self.Req['updated_at']))
                        Console().print(table, justify="left")
                    except (KeyboardInterrupt, EOFError): exit()
                    except Exception as F: print("\033[1;31mNo connection!\033[1;37m")

            if __name__=='__main__':
                try: Github()
                except (KeyboardInterrupt, EOFError): pass

            another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else: 
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()
        elif user_input == "5" or user_input == "05" or user_input == "Reddit" or user_input == "REDDIT" or user_input == "reddit":
            client_id = input("\033[1;37m[\033[1;34m+\033[1;37m] - Enter your client ID : \033[1;34m")
            client_secret = input("\033[1;37m[\033[1;34m+\033[1;37m] - Enter your client secert : \033[1;34m")
            user_agent = input("\033[1;37m[\033[1;34m+\033[1;37m] - Enter your useragent : \033[1;34m@")
            username = input("\033[1;37m[\033[1;34m+\033[1;37m] - Enter username target : \033[1;34m@")
            
            print("\033[1;37mGetting info...")
            time.sleep(3)
            print(f"\033[1;37m[ Get info for \033[1;34m@{username} \033[1;37m]\n")        

            reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

            try:
                username = reddit.redditor(username)

                table = Table(title="")
                table.add_column("Info", no_wrap=True)
                table.add_column("Acc")
                table.add_row("ID", str(username.id))
                table.add_row("Username", str("@"+username.name))
                table.add_row("Nickname", str(username.fullname))
                table.add_row("Avatar", str(username.icon_img))
                table.add_row("Bio", str(username.subreddit['description']))
                table.add_row("Bio link", str(username.subreddit['public_description']))
                table.add_row("Public email", str("Yes" if username.has_verified_email else "No"))
                table.add_row("Public phonenumber", str(username.comment_karma + username.link_karma))
                table.add_row("Create", str(username.created_utc))
                Console().print(table, justify="left")

            except Exception as e: print(f"\033[1;31mError : {e}!\033[1;37m")

            another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else: 
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()
        elif user_input == "6" or user_input == "06" or user_input == "Tellonym" or user_input == "tellonym" or user_input == "TELLONYM" or user_input == "Tell" or user_input == "TELL" or user_input == "tell":
            class Tell:
                def __init__(self, username):
                    self.username = username
                    self.driver = self.driver()
                    self.get_info()

                @staticmethod
                def driver():
                    chrome_options = Options()
                    chrome_options.add_argument('disable-infobars')
                    chrome_options.add_argument("--disable-logging")
                    chrome_options.add_argument('--log-level=3')
                    chrome_options.add_argument("--headless")
                    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
                    return webdriver.Chrome(options=chrome_options)

                def get_info(self):
                    try:
                        self.driver.get(f"https://api.tellonym.me/profiles/name/{self.username}?previousRouteName=ScreenProfileSharing&isClickedInSearch=true&sourceElement=Search%20Result&adExpId=91&limit=16")
                        self.driver.implicitly_wait(5)
                        response = self.driver.find_element(By.TAG_NAME, "pre")

                        if "The entry you were looking for could not be found." in response.text:
                            input("\033[1;31mUsername not found!\033[1;37m")
                            exit()
                        elif "This account is banned." in response.text:
                            input("\033[1;31macc is banned!\033[1;37m")
                            exit()
                        else:
                            json_data = json.loads(response.text)
                            id = json_data.get("id", "Unknown")
                            username = json_data.get("username", "Unknown")
                            name = json_data.get("displayName", "Unknown")
                            bio = json_data.get("aboutMe", "Unknown")
                            avatar = f"https://userimg.tellonym.me/lg-v2/{json_data['avatarFileName']}"
                            countryCode = json_data.get("countryCode", "Unknown")
                            followers = json_data.get("followerCount", "Unknown")
                            anonymousFollowerCount = json_data.get("anonymousFollowerCount", "Unknown")
                            RealFollowers = followers - anonymousFollowerCount or "0"
                            following = json_data.get("followingCount", "Unknown")
                            tell = json_data.get("tellCount", "Unknown")
                            answer = json_data.get("answerCount", "Unknown")
                            likes = json_data.get("likesCount", "Unknown")
                            is_Verified = json_data.get("isVerified", "Unknown")
                            is_Able_to_comment = json_data.get("isAbleToComment", "Unknown")
                            is_Active = json_data.get("isActive", "Unknown")
                            
                            table = Table(title="\n")
                            table.add_column("Info", no_wrap=True)
                            table.add_column("Acc")
                            table.add_row("ID", str(id))
                            table.add_row("Username", str("@"+username))
                            table.add_row("Name", str(name))
                            table.add_row("Bio", str(bio))
                            table.add_row("Avatar", str(avatar))
                            table.add_row("Country", str(countryCode))
                            table.add_row("Followers", str(followers))
                            table.add_row("Real Followers", str(RealFollowers))
                            table.add_row("Anonymous Followers", str(anonymousFollowerCount))
                            table.add_row("Following", str(following))
                            table.add_row("Tells", str(tell))
                            table.add_row("Answers", str(answer))
                            table.add_row("Likes", str(likes))
                            table.add_row("is Verified acc?", "Yes" if is_Verified else "No")
                            table.add_row("is Able to comment?", "Yes" if is_Able_to_comment else "No")
                            table.add_row("is Active now?", "Yes" if is_Active else "No")
                            Console().print(table, justify="left")
                    except Exception as e:
                        self.driver.quit()
                        input(f"\033[1;31mError : {str(e)}!\033[1;37m")
                        exit()

            username = input("\033[1;37m[\033[1;34m+\033[1;37m] - Enter username target : \033[1;34m@")
            print("\033[1;37mGetting info...")
            time.sleep(3)
            print(f"\033[1;37m[ Get info for \033[1;34m@{username} \033[1;37m]\n")

            Tell(username)

            another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else:
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()
        elif user_input == "99" or user_input == "BACK" or user_input == "Back": main_menu()
        else: 
            print("\033[1;31mPlease choose a valid option!")
            exit()
    elif selection == "4" or selection == "04" or selection == "Domains OSINT" or selection == "DOMAINS OSINT" or selection == "domains osint":
        domain = input("\033[1;37m[\033[1;34m+\033[1;37m] - Enter the domain or IP : \033[1;34m")
        
        print("\033[1;37mGetting info...")
        time.sleep(3)
        print(f"[ Get info for \033[1;34m{domain} \033[1;37m]\n") 

        def domain_info():
            url = f"https://demo.ip-api.com/json/{domain}?fields=66842623&lang=en"
            headers = { 'Accept': '*/*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Connection': 'keep-alive',
                        'Host': 'demo.ip-api.com',
                        'Origin': 'https://ip-api.com',
                        'Referer': 'https://ip-api.com/',
                        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': "Windows",
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-site',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36' }
            req1 = requests.post(url, headers=headers)
            req2 = requests.get(f'https://ipapi.co/{domain}/json/')

            table = Table(title="")
            table.add_column("Info", no_wrap=True)
            table.add_column("Domain")
            try: 
                response = requests.get(f"https://{domain}/")
                table.add_row("URL", str(response.url))
            except requests.exceptions.SSLError: table.add_row("URL", str(socket.gethostbyaddr(domain)))
            try:
                ip = socket.gethostbyname(domain)
                table.add_row("IP", str(ip))
                hexhost = socket.inet_aton(domain)
                table.add_row("Binary Host", str(hexhost))
                table.add_row("Hex Host", str(hexlify(hexhost)))
            except OSError: 
                hexhost = socket.inet_aton(ip)
                table.add_row("Binary Host", str(hexhost))
                table.add_row("Hex Host", str(hexlify(hexhost)))
            try: table.add_row("Version", str(req2.json()['version']))
            except KeyError: None
            table.add_row("ISP", str(req1.json()['isp']))
            table.add_row("FQDN", str(socket.getfqdn(domain)))
            try: table.add_row("Asn", str(req2.json()['asn']))
            except KeyError: None
            table.add_row("Status", str(req1.json()['status']))
            table.add_row("Continent", str(req1.json()['continent']))
            table.add_row("ContinentCode", str(req1.json()['continentCode']))
            table.add_row("Country", str(req1.json()['country']))
            table.add_row("CountryCode", str(req1.json()['countryCode']))
            table.add_row("Region", str(req1.json()['region']))
            table.add_row("RegionName", str(req1.json()['regionName']))
            table.add_row("City", str(req1.json()['city']))
            table.add_row("District", str(req1.json()['district']))
            table.add_row("Zip", str(req1.json()['zip']))
            table.add_row("TimeZone", str(req1.json()['timezone']))
            table.add_row("Currency", str(req1.json()['currency']))
            table.add_row("Lat", str(req1.json()['lat']))
            table.add_row("Lon", str(req1.json()['lon']))
            table.add_row("Offset", str(req1.json()['offset']))
            table.add_row("Mobile", str("Yes" if req1.json()['mobile'] is True else "No"))
            table.add_row("Status", str("Yes" if req1.json()['proxy'] is True else "No"))
            table.add_row("Hosting", str("Yes" if req1.json()['hosting'] is True else "No"))
            Console().print(table, justify="left")
        domain_info()

        another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else:
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()
    elif selection == "5" or selection == "05" or selection == "IP's OSINT" or selection == "IP'S OSINT" or selection == "ip's osint":
        ip_osint_selections = input("""\033[1;37m[\033[1;34m1\033[1;37m] - Target
[\033[1;34m2\033[1;37m] - Your device
Choose : \033[1;34m""")
        if ip_osint_selections == "1" or ip_osint_selections == "Target" or ip_osint_selections == "TARGET" or ip_osint_selections == "target":
            target_ip = input("\033[1;37m[\033[1;34m+\033[1;37m] - Enter Target IP : \033[1;34m")
            
            print("\033[1;37mGetting info...")
            time.sleep(3)
            print(f"[ Get info for \033[1;34m{target_ip} \033[1;37m]\n") 
            try:
                response = requests.get(url=f'http://ip-api.com/json/{target_ip}').json()

                table = Table(title="")
                table.add_column("Info", no_wrap=True)
                table.add_column("IP")
                table.add_row("IP", str(response.get(search)))
                ip_version = ipaddress.ip_address(target_ip)
                table.add_row("Version", str("IPV4" if ip_version.version == 4 else "IPV6"))
                hexhost = socket.inet_aton(target_ip)
                table.add_row("Binary Host", str(hexhost))
                table.add_row("Hex Host", str(hexlify(hexhost)))
                ip_hostname = socket.gethostname()
                table.add_row("ISP", str(response.get('isp')))
                table.add_row("Country", str(response.get('country')))
                table.add_row("RegionName", str(response.get('regionName')))
                table.add_row("City", str(response.get('city')))
                table.add_row("Zip", str(response.get('zip')))
                table.add_row("Lat", str(response.get('lat')))
                table.add_row("Lon", str(response.get('lon')))
                Console().print(table, justify="left")
            except requests.exceptions.ConnectionError: print('\033[1;31mPlease check your connection!')

            another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else:
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()
        elif ip_osint_selections == "2" or ip_osint_selections == "Your device" or ip_osint_selections == "YOUR DEVICE" or ip_osint_selections == "your device":
            device_host_name = socket.gethostname()
            device_ip = socket.gethostbyname(device_host_name)
            ip_version = ipaddress.ip_address(device_ip)

            table = Table(title="\033[1;37m")
            table.add_column("Info", no_wrap=True)
            table.add_column("Yor device")
            table.add_row("OS", str(platform.system()))
            table.add_row("OS release", str(platform.version()))
            table.add_row("Architecture", str(platform.architecture()))
            table.add_row("Processor", str(platform.processor()))
            table.add_row("Total, Physical cores", str(f"{psutil.cpu_count(logical=True)}, {psutil.cpu_count(logical=False)}"))            
            cpufreq = psutil.cpu_freq()
            table.add_row("Max, Min, Current frequency", str(f"{cpufreq.max:.2f} MHz, {cpufreq.min:.2f} MHz, {cpufreq.current:.2f} MHz"))
            for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)): table.add_row(f"Core {i}", str(f"{percentage}%"))
            table.add_row(f"Total CPU Usage", str(f"{psutil.cpu_percent()}%"))
            total, used, free = shutil.disk_usage("/")
            table.add_row("Total, Used, Free storage space", str(f"{total//(2**30)}GB, {used//(2**30)}GB, {free//(2**30)}GB"))
            table.add_row("Hostname", str(device_host_name))
            table.add_row("IP", str(device_ip))
            table.add_row("Version", str("IPV4" if ip_version.version == 4 else "IPV6"))
            hexhost = socket.inet_aton(device_ip)
            table.add_row("Binary Host", str(hexhost))
            table.add_row("Hex Host", str(hexlify(hexhost)))
            try: ipv6_addr = str(socket.getaddrinfo(device_host_name, None, socket.AF_INET6)[0][4][0])
            except socket.gaierror: ipv6_addr = "Unavailable"
            table.add_row("IPV6", ipv6_addr)

            Console().print(table, justify="left")

            another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else:
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()
    elif selection == "6" or selection == "06" or selection == "Networks OSINT" or selection == "NETWORKS OSINT" or selection == "networks osint":
        submenu3()
        user_input = input("Choose : \033[1;34m")

        if user_input == "1" or user_input == "01" or user_input == "Networks OSINT" or user_input == "NETWORKS OSINT" or user_input == "networks osint":
            print("\033[1;37mExtracting info...")
            time.sleep(3)
            print("\n[ Get info for networks ]")
            time.sleep(1)

            def check_os():
                os_name = platform.system()

                if os_name == "Windows":
                    print("\033[1;34m")
                    os.system("ipconfig")
                    print("\033[1;37m")
                elif os_name == "Linux":
                    def get_distro_name():
                        try:
                            output = subprocess.check_output("lsb_release -i", shell=True)
                            distro_name = output.decode().split(":")[1].strip().lower()
                        except Exception as e: distro_name = None
                        return distro_name

                    distro_name = get_distro_name()

                    if "kali" in distro_name or "Mac OS" in os.environ: 
                        print("\033[1;34m")
                        os.system("ifconfig")
                        print("\033[1;37m")
                    elif "parrot" in distro_name:
                        print("\033[1;34m")
                        os.system("ip address")
                        print("\033[1;37m")
                    elif "arch" in distro_name or "backbox" in distro_name:
                        print("\033[1;34m")
                        os.system("ip")
                        print("\033[1;37m")
                elif os_name == "Darwin": 
                    if "iSH" in os.environ or "termux" in os.environ:
                        print("\033[1;34m")
                        os.system("ip a")
                        print("\033[1;37m")
                    else: pass
                else: print("\033[1;31mOSINT cannot be done because your operating system is unknown!\033[1;37m")
            print(check_os())

            another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else:
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()
        elif user_input == "2" or user_input == "02" or user_input == "Show network operations" or user_input == "SHOW NETWORK OPERATIONS" or user_input == "show network operations":
            print("\033[1;37mExtracting network operations...")
            time.sleep(3)
            print("\n[ Get network operations ]")
            time.sleep(1)

            print("\033[1;34m")
            os.system("netstat")
            print("\033[1;37m")

            another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else:
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()
        elif user_input == "99" or user_input == "Back" or user_input == "BACK" or user_input == "back": main_menu()
        else: print("\033[1;31mPlease choose a valid option!")
    elif selection == "7" or selection == "07" or selection == "Images OSINT" or selection == "IMAGES OSINT" or selection == "images osint":
        class images:
            def __init__(self):
                try: 
                    self.img_name = str(input("\033[1;37m[\033[1;34m+\033[1;37m] Enter img name or path : \033[1;34m")).replace(" ","")
                    self.image = Image.open(self.img_name)
                    self.img_read = cv2.imread(self.img_name)
                except Exception as e:
                    print(f"\033[1;31m{e}!\033[1;37m")
                    exit()

            def handle_exif_data(self):
                exif_data = self.image._getexif()
                if exif_data is not None:
                    for tag, value in exif_data.items():
                        tag_name = TAGS.get(tag, tag)
                        if tag_name == "DateTimeOriginal":
                            return value
                return None

            def DeviceInfo(self):
                try:  exif = self.image._getexif()
                except: exit()
                if self.image._getexif() is None: exit()
                else:
                    for k, v in self.image._getexif().items():
                        decoded = TAGS.get(k, k)
                        if decoded == "MakerNote": pass
                        elif decoded == "GPSInfo": self.GPSInfo = v

            def GetGeoposition(self):
                self.DeviceInfo()
                gp = self.GPSInfo
                if self.GPSInfo is None:
                    return None, None

                gpsinfo = {}
                for k in gp.keys():
                    decoded = GPSTAGS.get(k, k)
                    gpsinfo[decoded] = gp[k]
                lat = None
                lon = None
                gps_latitude = gpsinfo.get("GPSLatitude")
                gps_latitude_ref = gpsinfo.get("GPSLatitudeRef")
                gps_longitude = gpsinfo.get("GPSLongitude")
                gps_longitude_ref = gpsinfo.get("GPSLongitudeRef")
                if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
                    lat = self._convert_to_degress(gps_latitude)
                    if gps_latitude_ref != 'N': lat = 0 - lat
                    lon = self._convert_to_degress(gps_longitude)
                    if gps_longitude_ref != 'E': lon = 0 - lon
                self.lat = lat
                self.lon = lon
                return True

            def LocationInfo(self):
                if not self.GetGeoposition(): pass
                else: 
                    headers = { 'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1' }
                    response = requests.get(f'https://api.opencagedata.com/geocode/v1/json?q={self.lat}+{self.lon}&key=03c48dae07364cabb7f121d8c1519492&no_annotations=1&language=en', headers=headers)
                    if 'country' not in response.text: pass
                    try:
                        console = Console()
                        table = Table(title="\033[1;37m")
                        table.add_column("Pic", no_wrap=True)
                        table.add_column("Info")

                        for info in response.json()['results']:
                            date_taken = self.handle_exif_data()
                            if date_taken is not None: table.add_row("Imagine time", date_taken)
                            pixels = self.img_read.size
                            dim = self.img_read.shape
                            table.add_row("Pixels", str(pixels))
                            table.add_row("Dimensions", str(dim))
                            components = info['components']
                            for key, value in components.items():
                                if key not in ['ISO_3166-1_alpha-2', 'ISO_3166-1_alpha-3', 'ISO_3166-2']:
                                    table.add_row(key, str(value))
                        table.add_row("GoogleMap link", f"http://www.google.com/maps/place/{self.lat},{self.lon}")
                        console.print(table)
                    except: pass
        img = images()
        img.LocationInfo()

        another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else:
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()
    elif selection == "8" or selection == "08" or selection == "PhoneNumbers OSINT" or selection == "PHONENUMBERS OSINT" or selection == "phonenumber osint":
        submenu2()
        user_input = input("Choose : \033[1;34m")

        if user_input == "1" or user_input == "01" or user_input == "PhoneNumber OSINT" or user_input == "PHONENUMBER OSINT" or user_input == "phonenumber osint":
            PhoneNumber = input("\033[1;37m[\033[1;34m+\033[1;37m] Enter phonenumber (ex: +966500000000) : \033[1;34m")
            
            print("\033[1;37mGetting info...")
            time.sleep(3)
            print(f"\033[1;37m[ Get info for \033[1;34m{PhoneNumber} \033[1;37m]\n") 

            try: parse = phonenumbers.parse(PhoneNumber)
            except: print("\033[1;31mPlease add countrycode!\033[1;37m")

            region = geocoder.description_for_number(parse, 'en')
            tiimezone = timezone.time_zones_for_number(parse)
            isp = carrier.name_for_number(parse, 'en')

            table = Table(title="")
            table.add_column("Info", no_wrap=True)
            table.add_column("PhoneNumber")
            table.add_row("Location", str(region))
            table.add_row("TimeZone", str(tiimezone))
            table.add_row("ISP", str(isp))
            Console().print(table, justify="left")

            another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else:
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()
        elif user_input == "2" or user_input == "02" or user_input == "Search for the owner of the number by name" or user_input == "SEARCH FOR THE OWNER OF THE NUM BY NAME" or user_input == "search for the owner of the num by name":
            print(f"""\033[1;37m[\033[1;34m1\033[1;37m] KSA [SA]
\033[1;37m[\033[1;34m2\033[1;37m] UAE [AE]
\033[1;37m[\033[1;34m4\033[1;37m] Kuwait [KW]
\033[1;37m[\033[1;34m3\033[1;37m] Qatar [QA]
\033[1;37m[\033[1;34m5\033[1;37m] Oman [OM]
\033[1;37m[\033[1;34m6\033[1;37m] Bahrain [BH]
\033[1;37m[\033[1;34m7\033[1;37m] Egypt [EG] 
\033[1;37m[\033[1;34m8\033[1;37m] Iraq [IQ]""")

            country = input("\033[1;37m[\033[1;34m+\033[1;37m] Enter the countrycode : \033[1;34m")
            country_list = ["SA", "AE", "KW", "QA", "OM", "BH", "EG", 'IQ']
            if country in country_list:
                name = input("\033[1;37m[\033[1;34m+\033[1;37m] Enter the target Name : \033[1;34m")

                print("\033[1;37mSearching...")
                time.sleep(3)
                print(f"\033[1;37m[ Search for \033[1;34m{name} \033[1;37m]\n") 

                url = f"https://caller-id.saedhamdan.com/index.php/UserManagement/search_number?country_code={country}&name={name}"
                r = requests.get(url, verify=False)
                data = r.json()

                if 'result' in r.text:
                    if len(data['result']) > 0:
                        print("-"*40)
                        for numbers in data['result']:
                            number = numbers['number']
                            name = numbers['name']
                            country_code = numbers['country_code']
                            address = numbers['address']
                            with open("SRFTOOTN.txt", "at", encoding="utf-8") as f: 
                                f.write(f"""[-] Name : {name}
[-] Number : {number}
[-] CountryCode : {country_code}
[-] Address : {address}\n\n""")

                        print(f"\033[1;37m[\033[1;32m✓\033[1;37m] The results has been saved in \033[1;34m{ os.getcwd()}\SRFTOOTN.txt\033[1;37m")
                elif 'No recourd found' in r.text: print("\033[1;31mnothing found for this name!")
            else: print("\033[1;31myour Country not in the list!")

            another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else:
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()
        elif user_input == "99" or user_input == "Back" or user_input == "BACK" or user_input == "back": main_menu()
        else: print("\033[1;31mPlease choose a valid option!")
    elif selection == "9" or selection == "09" or selection == "Search engine" or selection == "SEARCH ENGINE" or selection == "Search engine":
        searchh = input("\033[1;37m[\033[1;34m+\033[1;37m] Enter the thing to search for : \033[1;34m")
        result = input("\033[1;37m[\033[1;34m+\033[1;37m] Enter the num of results : \033[1;34m")

        print("\033[1;37mSearching...")
        time.sleep(3)
        print(f"\033[1;37m[ Search for \033[1;34m{searchh} \033[1;37m]\n") 

        with open("ESR.txt", "at", encoding="utf-8") as f:
            for url in search(searchh, tld="co.in", num=int(result), stop=int(result)):
                page = requests.get(url)
                soup = BeautifulSoup(page.content, 'html.parser')

                title = soup.title.string if soup.title else 'No title'
                text = ' '.join(p.get_text() for p in soup.find_all('p'))

                f.write(f"""[-] Title : {title}
[-] URL : {url}
[-] Text : {text}\n\n""")

        print(f"\033[1;37m[\033[1;32m✓\033[1;37m] The results has been saved in \033[1;34m{ os.getcwd()}\ESR.txt\033[1;37m")

        another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else:
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()
    elif selection == "10" or selection == "Ports scan" or selection == "PORTS SCAN" or selection == "ports scan":
        def check_port(ip_input, port):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                if s.connect_ex((ip_input, port)) == 0: return port

        def scan_ports(ip_input, num_ports):
            open_ports = []

            print("\033[1;37mScanning...")

            with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                future_to_port = {executor.submit(check_port, ip_input, port): port for port in range(1, num_ports+1)}
                for future in concurrent.futures.as_completed(future_to_port):
                    result = future.result()
                    if result is not None: open_ports.append(result)
            return sorted(open_ports)

        ip_input = input("\033[1;37m[\033[1;34m+\033[1;37m] Enter the target IP : \033[1;34m")
        num_ports = int(input("\033[1;37m[\033[1;34m+\033[1;37m] Entet the num of ports : \033[1;34m"))
        open_ports = scan_ports(ip_input, num_ports)

        if open_ports:
            print(f"\033[1;37m[ Scan for \033[1;34m{ip_input} \033[1;37mPorts ]\n")
            time.sleep(1)

            for port in open_ports:
                print(f"\033[1;37m[\033[1;32m✓\033[1;37m] Port \033[1;33m{port} \033[1;37mis open\n")
                time.sleep(1)
        else: print(f"\033[1;33mThere are no open ports!\033[1;37m")

        print(f"\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;33m{num_ports} \033[1;37mPorts were scanned")

        print(f"\033[1;37m[\033[1;32m✓\033[1;37m] Open ports : \033[1;33m{open_ports}\033[1;37m")

        another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else:
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()
    elif selection == "11" or selection == "Deep & Dark Web" or selection == "DEEP & DARK WEB" or selection == "deep & dark web":
        table = Table(title="\nThe most famous search engines in the \033[1;31mDeep & Dark Web\n\033[1;37m")
        table.add_column("General Info", no_wrap=True)
        table.add_column("Clients")
        table.add_column("Discovery")
        table.add_column("TOR Search")
        table.add_column("TOR Directories")
        table.add_row("Reddit Deep Web", "TOR Download", "OnionScan", "Onion Cab", "Hidden Wiki")
        table.add_row("Reddit Onions", "Freenet Project", "TorBot", "OnionLink", "Core.onion")
        table.add_row("Reddit Darknet", "I2P Anonymous Network", "Tor Scan", "Candle", "Tor2web")
        table.add_row("-", "-", "Onioff", "Not Evil", "Web O Proxy")
        table.add_row("-", "-", "Hunchly Hidden Services Report", "Tor66", "IACA Dark Web Investigation Support")
        table.add_row("-", "-", "docker-onion-nmap", "dark.fail", "-")
        table.add_row("-", "-", "Onion Investigator", "Ahmia", "-")
        Console().print(table, justify="left")

        another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else:
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()
    elif selection == "12" or selection == "Monitor cameras" or selection == "MONITPR CAMERAS" or selection == "monitor cameras":
        submenu4()

        user_input = input("Choose : \033[1;34m")

        if user_input == "1" or user_input == "Cameras around the world" or user_input == "CAMERAS AROUND THE WORLD" or user_input == "cameras around the world":
            def monitor_cameras_world():
                json = requests.get('http://www.insecam.org/en/jsoncountries/', headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
                    'Cache-Control': 'max-age=0',
                    'Connection': 'keep-alive',
                    'Cookie': '_ga=GA1.1.1125454972.1667225132; __gads=ID=d4a85cd85ce2f539-223503ca84d60066:T=1667225145:RT=1667225145:S=ALNI_MZ4MsyAr2w4HGK_wzfy90dxfdFtng; __gpi=UID=00000b196cc62113:T=1667225145:RT=1667225145:S=ALNI_MZx4MzjOSuSbqPbJFNskKGifhu5zw; _ga_F7ZM4QYVCB=GS1.1.1667225132.1.1.1667226059.0.0.0',
                    'Host': 'www.insecam.org',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36' }).json()['countries']

                value = []
                counter = 1
                for i in json:
                    print(f"\033[1;37m[\033[1;34m{counter}\033[1;37m] {json[i]['country']} [{i}] \033[1;33m{ {json[i]['count']} }\033[1;37m")
                    value.append(i)
                    counter += 1

                cc_choose = input(f"\033[1;37m[\033[1;34m+\033[1;37m] Choose the CountryCode : \033[1;34m")
                if cc_choose in value:
                    r = requests.get('http://www.insecam.org/en/bycountry/'+cc_choose+'/', headers={
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
                        'Cache-Control': 'max-age=0',
                        'Connection': 'keep-alive',
                        'Cookie': '_ga=GA1.1.1125454972.1667225132; __gads=ID=d4a85cd85ce2f539-223503ca84d60066:T=1667225145:RT=1667225145:S=ALNI_MZ4MsyAr2w4HGK_wzfy90dxfdFtng; __gpi=UID=00000b196cc62113:T=1667225145:RT=1667225145:S=ALNI_MZx4MzjOSuSbqPbJFNskKGifhu5zw; _ga_F7ZM4QYVCB=GS1.1.1667225132.1.1.1667226059.0.0.0',
                        'Host': 'www.insecam.org',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36' }).text
                    s = r.split('pagenavigator("?page=",')[1]
                    next = s.split(',')[0]
                    next = int(next)
                    
                    S = r.split('"thumbnail-item__wrap" href="')
                    counter = 1
                    for i in S:
                        Y = i.split('" ')[0]
                        if 'html' in Y:	pass
                        else:
                            url = f'http://www.insecam.org{Y}'
                            print(f"\033[1;37m[\033[1;34m{counter}\033[1;37m] \033[1;33m{url}")
                            counter += 1
                            
                    info = requests.get(url, headers={
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'Accept-Encoding': 'gzip, deflate',
                            'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
                            'Cache-Control': 'max-age=0',
                            'Connection': 'keep-alive',
                            'Cookie': '_ga=GA1.1.1125454972.1667225132; __gads=ID=d4a85cd85ce2f539-223503ca84d60066:T=1667225145:RT=1667225145:S=ALNI_MZ4MsyAr2w4HGK_wzfy90dxfdFtng; __gpi=UID=00000b196cc62113:T=1667225145:RT=1667225145:S=ALNI_MZx4MzjOSuSbqPbJFNskKGifhu5zw; _ga_F7ZM4QYVCB=GS1.1.1667225132.1.1.1667226059.0.0.0',
                            'Host': 'www.insecam.org',
                            'Upgrade-Insecure-Requests': '1',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36' }).text
                            
                    for i in range(2, next):
                        print(i)
                        url = 'http://www.insecam.org/en/bycountry/RS/?page='+str(i)
                        r = requests.get(url, headers={
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'Accept-Encoding': 'gzip, deflate',
                            'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
                            'Cache-Control': 'max-age=0',
                            'Connection': 'keep-alive',
                            'Cookie': '_ga=GA1.1.1125454972.1667225132; __gads=ID=d4a85cd85ce2f539-223503ca84d60066:T=1667225145:RT=1667225145:S=ALNI_MZ4MsyAr2w4HGK_wzfy90dxfdFtng; __gpi=UID=00000b196cc62113:T=1667225145:RT=1667225145:S=ALNI_MZx4MzjOSuSbqPbJFNskKGifhu5zw; _ga_F7ZM4QYVCB=GS1.1.1667225132.1.1.1667226059.0.0.0',
                            'Host': 'www.insecam.org',
                            'Upgrade-Insecure-Requests': '1',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36' }).text

                        S = r.split('"thumbnail-item__wrap" href="')
                        counter = 1
                        for i in S:
                            Y = i.split('" ')[0]
                            if 'html' in Y:	pass
                            else:
                                url = f'http://www.insecam.org{Y}'
                                print(f"\033[1;37m[\033[1;34m{counter}\033[1;37m] \033[1;33m{url}")
                                counter += 1
                else: 
                    print(f"\033[1;31mCountryCode not found!\033[1;37m")
                    print("\n")
                    time.sleep(3)
                    monitor_cameras_world()
            monitor_cameras_world()

            another_operation = input("\n\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else:
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()   
        elif user_input == "2" or user_input == "Cameras of places" or user_input == "CAMERAS OF PLACES" or user_input == "cameras of places":
            def monitor_cameras_places():
                json = requests.get('http://www.insecam.org/en/jsontags/', headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
                    'Cache-Control': 'max-age=0',
                    'Connection': 'keep-alive',
                    'Cookie': '_ga=GA1.1.1125454972.1667225132; __gads=ID=d4a85cd85ce2f539-223503ca84d60066:T=1667225145:RT=1667225145:S=ALNI_MZ4MsyAr2w4HGK_wzfy90dxfdFtng; __gpi=UID=00000b196cc62113:T=1667225145:RT=1667225145:S=ALNI_MZx4MzjOSuSbqPbJFNskKGifhu5zw; _ga_F7ZM4QYVCB=GS1.1.1667225132.1.1.1667226059.0.0.0',
                    'Host': 'www.insecam.org',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36' }).json()['tags']
                
                counter = 1
                jsontags = []
                for i in json:
                    jsontags.append(i)
                    print(f"\033[1;37m[\033[1;34m{str(counter)}\033[1;37m] {i}")
                    counter += 1
                place_choose = int(input((f"\033[1;37m[\033[1;34m+\033[1;37m] Choose the place : \033[1;34m")))
                
                try:
                    r = requests.get('http://www.insecam.org/en/bytag/'+jsontags[place_choose]+'/', headers={
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'Accept-Encoding': 'gzip, deflate',
                            'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
                            'Cache-Control': 'max-age=0',
                            'Connection': 'keep-alive',
                            'Cookie': '_ga=GA1.1.1125454972.1667225132; __gads=ID=d4a85cd85ce2f539-223503ca84d60066:T=1667225145:RT=1667225145:S=ALNI_MZ4MsyAr2w4HGK_wzfy90dxfdFtng; __gpi=UID=00000b196cc62113:T=1667225145:RT=1667225145:S=ALNI_MZx4MzjOSuSbqPbJFNskKGifhu5zw; _ga_F7ZM4QYVCB=GS1.1.1667225132.1.1.1667226059.0.0.0',
                            'Host': 'www.insecam.org',
                            'Upgrade-Insecure-Requests': '1',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}).text
                except IndexError:
                    print(f"\033[1;31mPlace not found!\033[1;37m")
                    print("\n")
                    time.sleep(3)
                    monitor_cameras_places()

                s = r.split('pagenavigator("?page=",')[1]
                next = s.split(',')[0]
                next = int(next)
                S = r.split('"thumbnail-item__wrap" href="')
                counter = 1
                for i in S:
                    Y = i.split('" ')[0]
                    if 'html' in Y: pass
                    else:
                        url = f'http://www.insecam.org{Y}'
                        print(f"\033[1;37m[\033[1;34m{counter}\033[1;37m] \033[1;33m{url}")
                        counter += 1
                        
                info = requests.get(url, headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
                    'Cache-Control': 'max-age=0',
                    'Connection': 'keep-alive',
                    'Cookie': '_ga=GA1.1.1125454972.1667225132; __gads=ID=d4a85cd85ce2f539-223503ca84d60066:T=1667225145:RT=1667225145:S=ALNI_MZ4MsyAr2w4HGK_wzfy90dxfdFtng; __gpi=UID=00000b196cc62113:T=1667225145:RT=1667225145:S=ALNI_MZx4MzjOSuSbqPbJFNskKGifhu5zw; _ga_F7ZM4QYVCB=GS1.1.1667225132.1.1.1667226059.0.0.0',
                    'Host': 'www.insecam.org',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36' }).text
                            
                for i in range(2, next):		
                    url = f'http://www.insecam.org/en/bycountry/RS/?page={str(i)}'
                    r = requests.get(url, headers={
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
                        'Cache-Control': 'max-age=0',
                        'Connection': 'keep-alive',
                        'Cookie': '_ga=GA1.1.1125454972.1667225132; __gads=ID=d4a85cd85ce2f539-223503ca84d60066:T=1667225145:RT=1667225145:S=ALNI_MZ4MsyAr2w4HGK_wzfy90dxfdFtng; __gpi=UID=00000b196cc62113:T=1667225145:RT=1667225145:S=ALNI_MZx4MzjOSuSbqPbJFNskKGifhu5zw; _ga_F7ZM4QYVCB=GS1.1.1667225132.1.1.1667226059.0.0.0',
                        'Host': 'www.insecam.org',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36' }).text

                    S = r.split('"thumbnail-item__wrap" href="')
                    counter = 1
                    for i in S:
                        Y = i.split('" ')[0]
                        if 'html' in Y: pass
                        else:
                            url = f'http://www.insecam.org{Y}'
                            print(f"\033[1;37m[\033[1;34m{counter}\033[1;37m] \033[1;33m{url}")
                            counter += 1
            monitor_cameras_places()
            
            another_operation = input("\n\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else:
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()
        elif user_input == "99" or user_input == "Back" or user_input == "BACK" or user_input == "back": main_menu()
        else: print("\033[1;31mPlease choose a valid option!")
    elif selection == "13" or selection == "WebScraping" or selection == "WEbSCRAPING" or selection == "webscraping":
        def extract_links_and_images(url):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            image_links = [img.get('src') for img in soup.find_all('img', src=True)]
            return links, image_links

        url = input("\033[1;37m[\033[1;34m+\033[1;37m] - Enter the target URL : \033[1;34m")

        print("\033[1;37mWebScraping...")
        time.sleep(3)
        print(f"\033[1;37m[ WebScraping for \033[1;34m{url} \033[1;37m]\n") 

        links, image_links = extract_links_and_images(url)

        print("\033[1;37mPaths & Links :")
        for link in links:
            print(f"    {link}")

        print("\n\033[1;37mImages :")
        for link in image_links:
            print(f"    {link}")

        def another_operation(): 
            ao = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if ao == "Y" or ao == "y" or ao == "Yes" or ao == "yes" or ao == "YES": main_menu()
            elif ao == "N" or ao == "n" or ao == "No" or ao == "no" or ao == "No": exit("\033[1;37m")
            else:
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                another_operation()

        def download_images(image_links, save_dir):
            save_images = input("\n\033[1;37mDo u want to save the images? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if save_images == "Y" or save_images == "y" or save_images == "Yes" or save_images == "yes" or save_images == "YES": 
                if not os.path.exists(save_dir): os.makedirs(save_dir)

                for i, link in enumerate(image_links):
                    if 'http' not in link:
                        link = url + link
                    response = requests.get(link)
                    with open(os.path.join(save_dir, f'img{i}.png'), 'wb') as f:
                        f.write(response.content)
                another_operation()
            elif save_images == "N" or save_images == "n" or save_images == "No" or save_images == "no" or save_images == "No": another_operation()
            else:
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                download_images(image_links, save_dir)
        download_images(image_links, "Downloaded images")

    elif selection == "14" or selection == "Israeli databases" or selection == "ISRAELI DATABASES" or selection == "israeli databases":
        table = Table(title="\n\033[1;37mLeaked Israeli db uploaded to the MediaFire platform.\n")
        table.add_column("Link")
        table.add_column("Description")
        table.add_column("Size")
        table.add_row("https://www.mediafire.com/file/l4o3yg0nehr0txv/1.csv/file", "Store room db containing 400K+ customers.", "86.6MB")
        table.add_row("https://www.mediafire.com/file/2is34z1ekkhj2su/2.csv/file", "A commercial db containing 200k+ customers.", "23.2MB")
        table.add_row("https://www.mediafire.com/file/63ib6s7o4rla335/3.csv/file", "A normal db contains 38K+ person.", "6.69MB")
        table.add_row("https://www.mediafire.com/file/0ruazdhfg3pib51/Leaks.json/file", "Json file containing info of 521 Israeli companies.", "689KB")
        Console().print(table, justify="left")
        
        another_operation = input("\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else:
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()  

    elif selection == "15" or selection == "Verify passwords leakage" or selection == "VERIFY PASSWORDS LEAKAGE" or selection == "verify passwords leakage":
        def check_password_leak(password):
            sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
            first5_char, tail = sha1password[:5], sha1password[5:]
            url = f'https://api.pwnedpasswords.com/range/{first5_char}'
            response = requests.get(url)
            hashes = (line.split(':') for line in response.text.splitlines())
            for h, count in hashes:
                if h == tail: return f"\033[1;31mThe passwas leaked {count} times!"
            return "\033[1;32mThe pass isn’t leaked."

        password = input("\033[1;37m[\033[1;34m+\033[1;37m] Enter the pass : \033[1;34m")
        print(check_password_leak(password))

    elif selection == "98" or selection == "Report bug" or selection == "REPORT BUG" or selection == "rebort bug":
        print("""\n\033[1;37mContact me through one of my acc
all my acc : \033[1;34mhttps://tlersa.github.io/tleralshahrani/Index.html#contact""")

        another_operation = input("\n\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else:
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()

    elif selection == "99" or selection == "Help" or selection == "HELP" or selection == "help":
        print("""\n\033[1;37mContact me through one of my acc
all my acc : \033[1;34mhttps://tlersa.github.io/tleralshahrani/Index.html#contact""")

        another_operation = input("\n\033[1;37mWould u like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else:
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()

def main():
    main_menu()

    while True:
        user_input = input("\033[1;37mChoose : \033[1;34m")
        handle_selection(user_input)

if __name__ == "__main__": main()
