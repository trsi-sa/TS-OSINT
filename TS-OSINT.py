try:
    import os, requests, json, time, sys, praw, socket, PIL.Image, PIL.ExifTags
    import phonenumbers
    from search_engines import Google, Bing
    from bs4 import BeautifulSoup
    from datetime import datetime
    from telethon.sync import TelegramClient
    from phonenumbers import geocoder, carrier, timezone
    from googlesearch import search
except ModuleNotFoundError:
    os.system("pip install os requests json time sys bs4 datetime telethon.sync praw socket PIL.Image PIL.ExifTags phonenumbers googlesearch")
    
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
           
                        \033[1;37mv0.0.0
\nTHIS TOOL WAS PROGRAMMED BY TLER AL-SHAHRANI.\nPERSONAL WEBSITE : \033[1;34mhttps://tlersa.github.io/tleralshahrani/Index.html""")
print("\033[1;37m- "*35)

def main_menu():
    print("""\033[1;37m[\033[1;34m1\033[1;37m] - Dorks
[\033[1;34m2\033[1;37m] - Usernames OSINT
[\033[1;34m3\033[1;37m] - Domains OSINT
[\033[1;34m4\033[1;37m] - IP OSINT
[\033[1;34m5\033[1;37m] - Images OSINT
[\033[1;34m6\033[1;37m] - PhoneNumbers OSINT
[\033[1;34m7\033[1;37m] - Search engine
[\033[1;34m99\033[1;37m] - Exit""")

def submenu():
    print("""\033[1;37m[\033[1;34m1\033[1;37m] - Instagram
[\033[1;34m2\033[1;37m] - Telegram accs
[\033[1;34m3\033[1;37m] - TikTok
[\033[1;34m4\033[1;37m] - Github
[\033[1;34m5\033[1;37m] - Reddit
[\033[1;34m99\033[1;37m] - Back""")

def handle_selection(selection):
    if selection == "1" or selection == "Dorks" or selection == "dorks" or selection == "DORKS":
        class dorks():
            def __init__(self):
                self.frist_name = None
                self.FName = None
                self.GFName = None
                self.last_name = None
                self.output = ""
                self.admin()

            def set_info(self):
                frist_name = input("[\033[1;34m+\033[1;37m] Frist name : \033[1;34m")
                FName = input("\033[1;37m[\033[1;34m+\033[1;37m] Father name : \033[1;34m")
                GFName = input("\033[1;37m[\033[1;34m+\033[1;37m] GrandFather name : \033[1;34m")
                last_name = input("\033[1;37m[\033[1;34m+\033[1;37m] Last/Family/Tribe name : \033[1;34m")

                if frist_name == "" or frist_name == " ": self.frist_name = False
                else: self.frist_name = frist_name

                if FName == "" or FName == " ": self.FName = False
                else: self.FName = FName

                if GFName == "" or GFName == " ": self.GFName = False
                else: self.GFName = GFName

                if last_name == "" or last_name == " ": self.last_name = False
                else: self.last_name = last_name

                if self.FName and self.frist_name and self.GFName and self.last_name is None:
                    input("\033[1;31mPlease add at least fristname!")
                    exit()

            def admin(self):
                self.set_info()
                print("\033[1;37m[ Searching in Google and Bing... ]")
                space = " "

                if self.frist_name and self.FName:
                    sql = self.frist_name + space + self.FName
                    self.search_google(sql)
                    self.search_bing(sql)

                if self.frist_name and self.last_name:
                    sql = self.frist_name + space + self.last_name
                    self.search_google(sql)
                    self.search_bing(sql)

                if self.frist_name and self.GFName and self.last_name:
                    sql = self.frist_name + space + self.GFName + space + self.last_name
                    self.search_google(sql)
                    self.search_bing(sql)

                if self.frist_name and self.last_name:
                    sql = self.frist_name + space + self.last_name
                    self.search_google(sql)
                        
                if self.frist_name and self.FName and self.last_name:
                    sql = self.frist_name + space + self.FName + space + self.last_name
                    self.search_google(sql)
                    self.search_bing(sql)

                if self.frist_name and self.FName and self.GFName and self.last_name:
                    sql = self.frist_name + space + self.FName + space + self.GFName + space + self.last_name
                    self.search_google(sql)
                    self.search_bing(sql)

                print("[ Searching in social media ]")
                self.output += "[ Searching in social media ]\n"

                self.search_in_social_media(self.frist_name)
                self.save()

            def add_info(self, link, title, text, _from): self.output += f"[-] Link : {link}\n[-] Title : {title}\n[-] Text : {text}\n[-] From : {_from}\n\n"

            def search_google(self, sql):
                try:
                    engine = Google()
                    results = engine.search(sql, pages=2)
                    for data in results.__dict__['_results']:
                        link = data['link']
                        title = data['title']
                        text = data['text']
                        self.add_info(link, title, text, "Google")
                    print("    [\033[1;32m✓\033[1;37m] Done Search in Google")
                except: pass

            def search_bing(self, sql):
                try:
                    engine = Bing()
                    results = engine.search(sql, pages=2)
                    for data in results.__dict__['_results']:
                        link = data['link']
                        title = data['title']
                        text = data['text']
                        self.add_info(link, title, text, "Bing")
                    print("    [\033[1;32m✓\033[1;37m] Done Search in Bing")
                except: pass

            def search_in_social_media(self, sql):
                websites = ['https://www.google.com/', 'https://www.bing.com/', 'https://www.youtube.com/', 'https://www.facebook.com/',
                            'https://www.messenger.com/', 'https://instagram.com', 'https://www.wechat.com/', 'https://www.tiktok.com/',
                            'https://open.spotify.com/', 'https://www.tumblr.com/', 'https://weibo.com/', 'https://t.me/',
                            'https://www.kuaishou.com/', 'https://accounts.snapchat.com/', 'https://www.pinterest.com/',
                            'https://www.reddit.com/', 'https://x.com', 'https://ar.quora.com/', 'https://badoo.com/',
                            'https://www.skype.com/', 'https://www.viber.com/', 'https://www.linkedin.com/', 'https://discord.com/',
                            'https://vimeo.com/', 'https://www.paypal.com/', 'https://www.twitch.tv/', 'https://www.epicgames.com/',
                            'https://imgur.com/', 'https://www.yy.com/', 'https://www.wattpad.com/', 'https://line.me/',
                            'https://soundcloud.com/', 'https://www.taringa.net/', 'https://medium.com/', 'https://foursquare.com/',
                            'https://triller.co/', 'https://www.deviantart.com/', 'https://www.yubo.live/', 'https://rumble.com/',
                            'https://renren.com/', 'https://nextdoor.com/', 'https://www.gaiaonline.com/', 'https://onlyfans.com/',
                            'https://weheartit.com/', 'https://myspace.com/', 'https://mixi.jp/', 'https://www.crunchyroll.com/',
                            'https://www.meetup.com/', 'https://tellonym.me/', 'https://pastebin.com/', 'https://www.flickr.com/',
                            'https://picsart.com/', 'https://mega.nz/','https://www.adobe.com/', 'https://github.com/',
                            'https://www.canva.com/', 'https://kick.com/', 'https://tip.dokan.sa/']
                for x in websites:
                    try:
                        engine = Google()
                        results = engine.search(sql + f"  {x}", pages=2)
                        for data in results.__dict__['_results']:
                            link = data['link']
                            title = data['title']
                            text = data['text']
                            self.add_info(link, title, text, "Google")
                        print(f"    [\033[1;32m✓\033[1;37m] Done Search in \033[1;34m{x}\033[1;37m")
                    except: pass
                print("[\033[1;32m✓\033[1;37m] Done search in social media")

            def save(self):
                with open(f"{self.frist_name}.txt", "a", encoding="utf-8") as F: F.write(self.output)
                F.close()
                print(f"\033[1;37m[\033[1;32m✓\033[1;37m] The info has been saved in \033[1;34m{ os.getcwd()}/{self.frist_name}.txt\033[1;37m")
        dorks()
        another_operation = input("Would you like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else:
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()        
    elif selection == "2" or selection == "Usernames OSINT" or selection == "usernames OSINT" or selection == "USERNAMES OSINT" or selection == "usernames osint":
        submenu()
        user_input = input("Choose : \033[1;34m")

        if user_input == "1" or user_input == "Instagram" or user_input == "instagram" or user_input == "INSTAGRAM" or user_input == "Insta" or user_input == "insta" or user_input == "INSTA":
            class insta:
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
                        print("[\033[1;32m-\033[1;37m] Username :\033[1;34m", result["username"])
                        print("\033[1;37m[\033[1;32m-\033[1;37m] User ID :\033[1;34m", result["username_id"])
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Nickame :\033[1;34m", result["name"])
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Bio :\033[1;34m", result["bio"])
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Bio URL :\033[1;34m", result["external_url"])
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Is Business acc :\033[1;34m", "Yes" if result["business_account"] else "No")
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Is Verified acc :\033[1;34m", "Yes" if result["verified_account"] else "No")
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Is Private acc :\033[1;34m", "Yes" if result["private_account"] else "No")
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Followers :\033[1;34m", result["followers"])
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Following :\033[1;34m", result["following"])
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Acc created before 30 days? :\033[1;34m", "Yes" if result['account_created_before_30d'] else "No")
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Has threads :\033[1;34m", "Yes" if result["has_threads"] is True else "No")
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Has videos :\033[1;34m", result.get("has_videos", "None"))
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Media count :\033[1;34m", result["media_count"])
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Total IGTV videos :\033[1;34m", result["total_igtv_videos"])
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Is in Canada :\033[1;34m", result.get("is_in_canada", False))
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Is memorialized acc :\033[1;34m", result.get("is_memorialized", False))
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Is new acc :\033[1;34m", "Yes" if result["is_new_account"] is True else "No")
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Public email :\033[1;34m", result.get("public_email", "None"))
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Public phonenumber :\033[1;34m", result.get("public_phone_number", "None"))
                        print("\033[1;37m[\033[1;32m-\033[1;37m] User have another acc :\033[1;34m", "Yes" if result["user_have_another_account"] is True else "No")
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Location :\033[1;34m", result.get("account_region", ""))
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Create :\033[1;34m", result.get("create_time", ""))
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Avatar :\033[1;34m", result["profile_pic"])
                        print("\033[1;37m[\033[1;32m-\033[1;37m] Last change avater :\033[1;34m", result["last_time_edit_avatar"])

            username = input("\033[1;37m[\033[1;34m+\033[1;37m] Enter username target : \033[1;34m")
            insta(username)
            
            another_operation = input("Would you like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else:
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()
        elif user_input == "2" or user_input == "Telegram" or user_input == "telegram" or user_input == "TELEGRAM":
            api_id = input("\033[1;37m[\033[1;34m+\033[1;37m] - Enter your API ID : \033[1;34m")
            api_hash = input("\033[1;37m[\033[1;34m+\033[1;37m] - Enter your API hash : \033[1;34m")

            client = TelegramClient('session_name', api_id, api_hash)

            async def main():
                await client.start()
                username = input("\033[1;37m[\033[1;34m+\033[1;37m] - Enter username/phonenumber target : \033[1;34m")
                
                print("\033[1;37mGetting info...")
                time.sleep(3)
                print(f"\033[1;37m[ Get info for \033[1;34m@{username} \033[1;37m]\n")

                try:
                    username = await client.get_entity(username)
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] Username : \033[1;34m@{username.username}")
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] User ID : \033[1;34m{username.id}")
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] Fristname : \033[1;34m{username.first_name}")
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] Lastname : \033[1;34m{username.last_name}")
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] Phonenumber : \033[1;34m{username.phone}")

                except Exception as e:
                    print(f"\033[1;31mErorr : {e}!\033[1;37m")

                await client.disconnect()

            if __name__ == '__main__':
                import asyncio
                asyncio.run(main())

            another_operation = input("\033[1;37mWould you like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else:
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()
        elif user_input == "3" or user_input == "TikTok" or user_input == "TIKTOK" or user_input == "tiktok" or user_input == "Tik" or user_input == "TIK" or user_input == "tik":
            class tik:
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
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] UserID : \033[1;34m{self.get_user_id()}")
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] Nickname : \033[1;34m{self.get_name()}")
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] is verified : \033[1;34m{self.is_verified()}")
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] is private : \033[1;34m{self.is_private()}")
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] secUid : \033[1;34m{self.secUid()}")
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] Followers : \033[1;34m{self.followers()}")
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] Following : \033[1;34m{self.following()}")
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] Likes : \033[1;34m{self.heart_count()}")
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] Video count : \033[1;34m{self.video_count()}")
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] Open favorite : \033[1;34m{self.open_favorite()}")
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] Can see following list : \033[1;34m{self.see_following()}")
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] Language : \033[1;34m{self.language()}")
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] Create : \033[1;34m{self.user_create_time()}")
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] Last change nickname : \033[1;34m{self.last_change_name()}")
                    print(f"\033[1;37m[\033[1;32m-\033[1;37m] Location : \033[1;34m{self.account_region()}\033[1;37m")

            username = input("\033[1;37m[\033[1;34m+\033[1;37m] Enter username target : \033[1;34m")
            
            print("\033[1;37mGetting info...")
            time.sleep(3)
            tik(username)

            another_operation = input("\033[1;37mWould you like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else:
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()
        elif user_input == "4" or user_input == "GitHub" or user_input == "Github" or user_input == "github" or user_input == "GITHUB":
            class github:
                def __init__(self):
                    self.Start()
                
                def Start(self):
                    self.username = input("\033[1;37m[\033[1;34m+\033[1;37m] Enter username target : \033[1;34m")
                    
                    print("\033[1;37mGetting info...")
                    time.sleep(3)
                    print(f"\033[1;37m[ Get info for \033[1;34m@{self.username} \033[1;37m]\n")
                    
                    try:
                        self.Get = requests.get('https://api.github.com/users/%s'%(self.username))
                        self.Req = json.loads(self.Get.text)
                        print(f"\033[1;37m[\033[1;32m-\033[1;37m] Username : \033[1;34m@{self.Req['login']}")
                        print(f"\033[1;37m[\033[1;32m-\033[1;37m] UserID : \033[1;34m{self.Req['node_id']}")
                        print(f"\033[1;37m[\033[1;32m-\033[1;37m] Avater : \033[1;34m{self.Req['avatar_url']}")
                        print(f"\033[1;37m[\033[1;32m-\033[1;37m] HTML URL : \033[1;34m{self.Req['html_url']}")
                        print(f"\033[1;37m[\033[1;32m-\033[1;37m] Type : \033[1;34m{self.Req['type']}")
                        print(f"\033[1;37m[\033[1;32m-\033[1;37m] Nickname : \033[1;34m{self.Req['name']}")
                        print(f"\033[1;37m[\033[1;32m-\033[1;37m] Company : \033[1;34m{self.Req['company']}")
                        print(f"\033[1;37m[\033[1;32m-\033[1;37m] Blog : \033[1;34m{self.Req['blog'], }")
                        print(f"\033[1;37m[\033[1;32m-\033[1;37m] Location : \033[1;34m{self.Req['location']}")
                        print(f"\033[1;37m[\033[1;32m-\033[1;37m] Public email : \033[1;34m{self.Req['email']}")
                        print(f"\033[1;37m[\033[1;32m-\033[1;37m] Hireable : \033[1;34m{self.Req['hireable']}")
                        print(f"\033[1;37m[\033[1;32m-\033[1;37m] Bio : \033[1;34m{self.Req['bio']}")
                        print(f"\033[1;37m[\033[1;32m-\033[1;37m] X username : \033[1;34m{self.Req['twitter_username']}")
                        print(f"\033[1;37m[\033[1;32m-\033[1;37m] Public repos : \033[1;34m{self.Req['public_repos']}")
                        print(f"\033[1;37m[\033[1;32m-\033[1;37m] Public gists : \033[1;34m{self.Req['public_gists']}")
                        print(f"\033[1;37m[\033[1;32m-\033[1;37m] followers : \033[1;34m{self.Req['followers']}")
                        print(f"\033[1;37m[\033[1;32m-\033[1;37m] following : \033[1;34m{self.Req['following']}")
                        print(f"\033[1;37m[\033[1;32m-\033[1;37m] Create : \033[1;34m{self.Req['created_at']}")
                        print(f"\033[1;37m[\033[1;32m-\033[1;37m] Last updated : \033[1;34m{self.Req['updated_at']}")
                    except (KeyboardInterrupt, EOFError): exit()
                    except Exception as F: print("\033[1;31mNo connection!\033[1;37m")

            if __name__=='__main__':
                try: github()
                except (KeyboardInterrupt, EOFError): pass
            
                another_operation = input("\033[1;37mWould you like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
                if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
                elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
                else:
                    print("\033[1;31mPlease choose a valid option!\033[1;37m")
                    exit()
        elif user_input == "5" or user_input == "Reddit" or user_input == "REDDIT" or user_input == "reddit":
            client_id = input("\033[1;37m[\033[1;34m+\033[1;37m] - Enter your client ID : \033[1;34m")
            client_secret = input("\033[1;37m[\033[1;34m+\033[1;37m] - Enter your client secert : \033[1;34m")
            user_agent = input("\033[1;37m[\033[1;34m+\033[1;37m] - Enter your user agent : \033[1;34m")
            username = input("\033[1;37m[\033[1;34m+\033[1;37m] - Enter username target : \033[1;34m")
            
            print("\033[1;37mGetting info...")
            time.sleep(3)
            print(f"\033[1;37m[ Get info for \033[1;34m@{username} \033[1;37m]\n")        

            reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

            try:
                username = reddit.redditor(username)

                print(f"\033[1;37m[\033[1;32m-\033[1;37m] Username : \033[1;34m@{username.name}")
                print(f"\033[1;37m[\033[1;32m-\033[1;37m] User ID : \033[1;34m{username.id}")
                print(f"\033[1;37m[\033[1;32m-\033[1;37m] Nickname : \033[1;34m{username.fullname}")
                print(f"\033[1;37m[\033[1;32m-\033[1;37m] Create : \033[1;34m{username.created_utc}")
                print(f"\033[1;37m[\033[1;32m-\033[1;37m] Avatar : \033[1;34m{username.icon_img}")
                print(f"\033[1;37m[\033[1;32m-\033[1;37m] Public phonenumber : \033[1;34m{username.comment_karma + username.link_karma}")
                print(f"\033[1;37m[\033[1;32m-\033[1;37m] Public email : \033[1;34m{username.has_verified_email}")
                print(f"\033[1;37m[\033[1;32m-\033[1;37m] Bio : \033[1;34m{username.subreddit['description']}")
                print(f"\033[1;37m[\033[1;32m-\033[1;37m] Bio URL : \033[1;34m{username.subreddit['public_description']}")

            except Exception as e: print(f"\033[1;31mError : {e}!\033[1;37m")   
            another_operation = input("\033[1;37mWould you like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else:
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()
        elif user_input == "99" or user_input == "Exit" or user_input == "EXIT" or user_input == "exit": main_menu()
        else: print("\033[1;31mPlease choose a valid option!")
    elif selection == "3" or selection == "Domains OSINT" or selection == "domains OSINT" or selection == "DOMAINS OSINT" or selection == "domains osint":
        domain = input("[\033[1;34m+\033[1;37m] - Enter the domain or IP : \033[1;34m")
        
        print("\033[1;37mGetting info...")
        time.sleep(3)
        print(f"[ Get info for \033[1;34m{domain} \033[1;37m]\n") 

        def domain_info():
            url = f'https://demo.ip-api.com/json/{domain}?fields=66842623&lang=en'
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
            print(f"\033[1;37m[\033[1;32m-\033[1;37m] Domain : \033[1;34m{socket.gethostbyaddr(domain)}")
            print(f"\033[1;37m[\033[1;32m-\033[1;37m] IP : \033[1;34m{socket.gethostbyname(domain)}")
            print(f"\033[1;37m[\033[1;32m-\033[1;37m] Host info : \033[1;34m{socket.gethostbyname_ex(domain)}")
            print(f"\033[1;37m[\033[1;32m-\033[1;37m] Status : \033[1;34m{req1.json()['status']}")
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] Continent : \033[1;34m'+req1.json()['continent'])
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] ContinentCode : \033[1;34m'+req1.json()['continentCode'])
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] Country : \033[1;34m'+req1.json()['country'])
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] CountryCode : \033[1;34m'+req1.json()['countryCode'])
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] Region : \033[1;34m'+req1.json()['region'])
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] RegionName : \033[1;34m'+req1.json()['regionName'])
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] City : \033[1;34m'+req1.json()['city'])
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] District : \033[1;34m'+req1.json()['district'])
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] Zip : \033[1;34m'+req1.json()['zip'])
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] TimeZone : \033[1;34m'+req1.json()['timezone'])
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] Currency : \033[1;34m'+req1.json()['currency'])
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] Isp : \033[1;34m'+req1.json()['isp'])
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] As : \033[1;34m'+req1.json()['as'])
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] Asname : \033[1;34m'+req1.json()['asname'])
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] Query : \033[1;34m'+req1.json()['query'])
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] Lat : \033[1;34m'+str(req1.json()['lat']))
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] Lon : \033[1;34m'+str(req1.json()['lon']))
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] Offset : \033[1;34m'+str(req1.json()['offset']))
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] Mobile : \033[1;34m'+str(req1.json()['mobile']))
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] Proxy : \033[1;34m'+str(req1.json()['proxy']))
            print(f'\033[1;37m[\033[1;32m-\033[1;37m] Hosting : \033[1;34m'+str(req1.json()['hosting']))

            req2 = requests.get(f'https://ipapi.co/{domain}/json/')
            try:
                print(f'\033[1;37m[\033[1;32m-\033[1;37m] Version : \033[1;34m'+str(req2.json()['version']))
                print(f'\033[1;37m[\033[1;32m-\033[1;37m] Asn : \033[1;34m'+str(req2.json()['asn']))
            except KeyError: None
        domain_info()

        another_operation = input("\033[1;37mWould you like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else:
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()
    elif selection == "4" or selection == "IP OSINT" or selection == "ip OSINT" or selection == "ip osint":
        ip_osint_selections = input("""[\033[1;34m1\033[1;37m] - Target
[\033[1;34m2\033[1;37m] - Your device
Choose : \033[1;34m""")
        if ip_osint_selections == "1" or ip_osint_selections == "Target" or ip_osint_selections == "target" or ip_osint_selections == "TARGET":
            target_ip = input("\033[1;37m[\033[1;34m+\033[1;37m] - Enter Target IP : \033[1;34m")
            
            print("\033[1;37mGetting info...")
            time.sleep(3)
            print(f"[ Get info for \033[1;34m{target_ip} \033[1;37m]\n") 
            try:
                response = requests.get(url=f'http://ip-api.com/json/{target_ip}').json()                    
                print(f"\033[1;37m[\033[1;32m-\033[1;37m] IP : \033[1;34m{response.get('query')}")
                print(f"\033[1;37m[\033[1;32m-\033[1;37m] ISP : \033[1;34m{response.get('isp')}")
                print(f"\033[1;37m[\033[1;32m-\033[1;37m] ORG : \033[1;34m{response.get('org')}")
                print(f"\033[1;37m[\033[1;32m-\033[1;37m] Country : \033[1;34m{response.get('country')}")
                print(f"\033[1;37m[\033[1;32m-\033[1;37m] Region name : \033[1;34m{response.get('regionName')}")
                print(f"\033[1;37m[\033[1;32m-\033[1;37m] City : \033[1;34m{response.get('city')}")
                print(f"\033[1;37m[\033[1;32m-\033[1;37m] ZIP : \033[1;34m{response.get('zip')}")
                print(f"\033[1;37m[\033[1;32m-\033[1;37m] LAT : \033[1;34m{response.get('lat')}")
                print(f"\033[1;37m[\033[1;32m-\033[1;37m] LON : \033[1;34m{response.get('lon')}")
                    
            except requests.exceptions.ConnectionError: print('\033[1;31mPlease check your connection!')

            another_operation = input("\033[1;37mWould you like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else:
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()
        elif ip_osint_selections == "2" or ip_osint_selections == "Your device" or ip_osint_selections == "your device" or ip_osint_selections == "YOUR DEVICE":
            device_hostname = socket.gethostname()
            device_ip = socket.gethostbyname(device_hostname)
            print(f"""\033[1;37m[\033[1;32m-\033[1;37m] Device hostname : \033[1;34m{device_hostname}
\033[1;37m[\033[1;32m-\033[1;37m] Device IP : \033[1;34m{device_ip}
\033[1;37m[\033[1;32m-\033[1;37m] Host info : \033[1;34m{socket.gethostbyaddr(device_hostname)}""")

            another_operation = input("\033[1;37mWould you like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else:
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()
    elif selection == "5" or selection == "Images OSINT" or selection == "images OSINT" or selection == "images osint" or selection == "IMAGES OSINT":
        class images:
            def __init__(self):
                try: self.image = PIL.Image.open(str(input("\033[1;37m[\033[1;34m+\033[1;37m] Enter img name or path : \033[1;34m")).replace(" ",""))
                except Exception as e:
                    print(f"\033[1;31m{e}!\033[1;37m")
                    exit()
            def DeviceInfo(self):
                try: exif = self.image._getexif()
                except:
                    print("\033[1;31mNo GPS/Location data exists!\033[1;37m")
                    exit()
                if self.image._getexif() is None:
                    print("\033[1;31mNo GPS/Location data exists!\033[1;37m")
                    exit()
                else:
                    for k, v in self.image._getexif().items():
                        decoded = PIL.ExifTags.TAGS.get(k, k)
                        if decoded == "MakerNote": pass
                        elif decoded == "GPSInfo": self.GPSInfo = v
                        else: print(f"\033[1;37m[\033[1;32m-\033[1;37m] {decoded} : \033[1;34m{v}\033[1;37m")
            def _convert_to_degress(self,value):
                try:
                    d = float(value[0][0])/float(value[0][1])
                    m = float(value[1][0])/float(value[1][1])
                    s = float(value[2][0])/float(value[2][1])
                    return d + (m / 60.0) + (s / 3600.0)
                except: return None

            def GetGeoposition(self):
                images.DeviceInfo()
                gp = self.GPSInfo
                if self.GPSInfo is None:
                    print("\033[1;31mNo GPs Info Found!\033[1;37m")
                    return None, None

                gpsinfo = {}
                for k in gp.keys():
                    decoded = PIL.ExifTags.GPSTAGS.get(k, k)
                    gpsinfo[decoded] = gp[k]
                lat = None
                lon = None
                gps_latitude = gpsinfo.get("GPSLatitude")
                gps_latitude_ref = gpsinfo.get("GPSLatitudeRef")
                gps_longitude = gpsinfo.get("GPSLongitude")
                gps_longitude_ref = gpsinfo.get("GPSLongitudeRef")
                if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
                    lat = images._convert_to_degress(gps_latitude)
                    if gps_latitude_ref != 'N': lat = 0 - lat
                    lon = images._convert_to_degress(gps_longitude)
                    if gps_longitude_ref != 'E': lon = 0 - lon
                self.lat = lat
                self.lon = lon
                return True

            def LocationInfo(self):
                if not images.GetGeoposition(): pass
                else: 
                    headers = { 'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1' }
                    response = requests.get(f'https://api.opencagedata.com/geocode/v1/json?q={self.lat}+{self.lon}&key=03c48dae07364cabb7f121d8c1519492&no_annotations=1&language=en', headers=headers)
                    if 'country' not in response.text: pass
                    try:
                        for info in response.json()['results']:
                            omponents = info['components']
                            for key, value in omponents.items():
                                if key == 'ISO_3166-1_alpha-2': pass
                                elif key == 'ISO_3166-1_alpha-3': pass
                                elif key == 'ISO_3166-2': pass
                                else: print(f"\033[1;37m[\033[1;32m-\033[1;37m] {key} : \033[1;34m{value}\033[1;37m")
                            print(f"\033[1;37m[\033[1;32m-\033[1;37m] GoogleMap link : \033[1;34mhttp://www.google.com/maps/place/{self.lat},{self.lon}\033[1;37m")
                    except: pass
        images = images()
        images.LocationInfo()

        another_operation = input("\033[1;37mWould you like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else:
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()
    elif selection == "6" or selection == "Phonenumbers OSINT" or selection == "phonenumbers OSINT" or selection == "PHONENUMBERS OSINT" or selection == "phonenumber osint":
        PhoneNumber = input("\033[1;37m[\033[1;34m+\033[1;37m] Enter phonenumber (ex: +966500000000) : \033[1;34m")
        
        print("\033[1;37mGetting info...")
        time.sleep(3)
        print(f"\033[1;37m[ Get info for \033[1;34m{PhoneNumber} \033[1;37m]\n") 

        try: parse = phonenumbers.parse(PhoneNumber)
        except: print("\033[1;31mPlease add countrycode!\033[1;37m")

        region = geocoder.description_for_number(parse, 'en')
        tiimezone = timezone.time_zones_for_number(parse)
        varrier = carrier.name_for_number(parse, 'en')

        print(f"\033[1;37m[\033[1;32m-\033[1;37m] Location : \033[1;34m{region}")
        print(f"\033[1;37m[\033[1;32m-\033[1;37m] TimeZone : \033[1;34m{tiimezone}")
        print(f"\033[1;37m[\033[1;32m-\033[1;37m] ISP : \033[1;34m{varrier}")

        another_operation = input("\033[1;37mWould you like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else:
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()
    elif selection == "7" or selection == "Search engine" or selection == "SEARCH ENGINE" or selection == "Search engine":
        searchh = input("\033[1;37m[\033[1;34m+\033[1;37m] Enter the thing you want to search for : \033[1;34m")
        result = input("\033[1;37m[\033[1;34m+\033[1;37m] Enter the number of results you want : \033[1;34m")

        print("\033[1;37mSearching...")
        time.sleep(3)
        print(f"\033[1;37m[ Search for \033[1;34m{searchh} \033[1;37m]\n") 

        with open(searchh+".txt", "at", encoding="utf-8") as f:
            for url in search(searchh, tld="co.in", num=int(result), stop=int(result)):
                page = requests.get(url)
                soup = BeautifulSoup(page.content, 'html.parser')

                title = soup.title.string if soup.title else 'No title'
                text = ' '.join(p.get_text() for p in soup.find_all('p'))

                f.write(f"""[-] Title : {title}
[-] URL : {url}\n
[-] Text : {text}\n\n""")

        print(f"\033[1;37m[\033[1;32m✓\033[1;37m] The results has been saved in \033[1;34m{ os.getcwd()}/{query}.txt\033[1;37m")

        another_operation = input("\033[1;37mWould you like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else:
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()
    elif selection == "99": exit()
    else: print("\033[1;31mPlease choose a valid option!")

def main():
    main_menu()

    while True:
        user_input = input("\033[1;37mChoose : ")
        handle_selection(user_input)

if __name__ == "__main__": main()