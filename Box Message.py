import requests, json, time, random, base64, os
#+------------------------------------------------------+
#| Author : L7N                                       |
#| Telegram : t.me/PyL7N                     |
#| Github : https://github.com/is-L7N  |
#+------------------------------------------------------+

class Instagram:
    def __init__(self, Bearer: str, id, token):
        self.Bearer = Bearer
        self.id = id
        self.Token = token
        self.time = int(time.time() * 1_000_000)
        self.url = "https://i.instagram.com/api/v1/direct_v2/inbox/"
        self.params = {
            'thread_message_limit': "10",
            'persistentBadging': "true",
            'limit': "20",
            'is_prefetching': "false",
            'fetch_reason': "manual_refresh"
        }
        self.headers = {
            'User-Agent': self.user_agent(),
            'Authorization': self.Bearer,
        }
        try:
            with open("messages.json", "r") as f:
                self.messages = json.load(f)
        except Exception:
            self.messages = {}
    
    def run(self):
        print("Wait for message...\n")
        while True:
            try:
                response = requests.get(self.url, params=self.params, headers=self.headers).json()
                for thread in response.get("inbox", {}).get("threads", []):
                    for user in thread.get("users", []):
                        username = user.get("username", "")  
                        name = user.get("full_name", "")
                        photo = user.get("profile_pic_url", "") 
                    for item in thread.get("items", []):
                        msgid = item.get("item_id")
                        message = item.get("text")
                        timestamp = item.get("timestamp")
                        iD = item.get("user_id")
                        
                        if msgid and message and msgid not in self.messages and int(timestamp) > self.time:
                            print(f"""
New Message in Your Instagram Box
Name : {name}  
Username : @{username}  
Message : {message}
""")
                            msg = (f"""
> New Message in Your Instagram Box
**Name :** {name}  
**Username :** @{username}  
**Message :** {message}

""")
                            try:
                                ass = requests.get(photo).content
                                response = requests.post(f"https://api.telegram.org/bot{self.Token}/sendDocument", 
                                 files={'document': ('L7N.jpg', ass, 'image/jpeg')},
                                 data={'chat_id': self.id, 'caption': msg, 'parse_mode' :'MarkdownV2'})
                            except Exception:
                                pass
                            
                            self.messages[msgid] = {
                                "iD": iD,
                                "username": username,
                                "name": name,
                                "message": message
                            }
                with open("messages.json", "w") as f:
                    json.dump(self.messages, f, ensure_ascii=False, indent=4)
                    
            except Exception:
                print("Err")

            time.sleep(random.randint(4, 6))
    
    def user_agent(self) -> str:
        rnd = str(random.randint(150, 999))
        agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986" + str(random.randint(111, 999)) + ")"
        return agent
        
class Fun:
    @staticmethod
    def trans_sessionid(ses):
        try:
            inp = ses.strip()
            if inp.startswith("Bearer IGT:2:"):
                b64 = inp.split("Bearer IGT:2:")[1]
                data = json.loads(base64.b64decode(b64).decode())
                return "[+] SessionID:\n" + data["sessionid"]
            else:
                uid = inp.split(":")[0]
                payload = json.dumps({"ds_user_id": uid, "sessionid": inp})
                token = base64.b64encode(payload.encode()).decode()
                return "[+] Bearer Token:\nBearer IGT:2:" + token
        except Exception:
            return {"status": False, "message": "Fuck!"}
            
if __name__ == "__main__":
    info = [
    "Author : L7N 🇮🇶",
    "Telegram : t.me/PyL7N",
    "Github : https://github.com/is-L7N"
]

    width = max(len(line) for line in info) + 4
    border = "+" + "-" * (width - 2) + "+"
    
    print(border)
    for line in info:
        print("| " + line.ljust(width - 3) + " |") 
    print(border)
    print("\n[1] Trans Sessionid To Token (Bearer) or opposite !\n[2] Run Tool !\n")
    cho = input("[*] Choose : ")
    if cho == 1 or cho == "1":
        inp = input("[×] Your Sessiond or Token : ")
        print(Fun.trans_sessionid(inp))   
    else:
        print("\n[※] Do you want to add send to Telegram ? (yes , no)\n")
        cho = input("[*] Choose : ").lower()
        if cho == "yes":
            token = input("\nYour Token Telegram : ")
            id = input("\nYour id Telegram : ")
            Bearer = input("\nYour Token Instagram Bearer (IGT) : ")
            os.system('clear')
            bot = Instagram(Bearer=Bearer,token=token,id=id)
            bot.run()

        elif cho == "no":
            token, id = None,None
            Bearer = input("\nYour Token Instagram Bearer (IGT) : ")
            os.system('clear')
            bot = Instagram(Bearer=Bearer,token=token,id=id)
            bot.run()
        else:
            print("Put Yes or No !!!")