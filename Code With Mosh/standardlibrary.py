# Workinfg with Path 
# sourcery skip: identity-comprehension
"""from datetime import datetime
import time"""

"""path = Path("C:\\LearnPython")

paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)"""

# Working with files

"""dt = datetime(2023, 1, 1)
dt = datetime.now()
dt = datetime.strptime("2018/01/01","%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
print(dt)
"""

"""from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from re import template
import smtplib, ssl
from string import Template 
from datetime import datetime
import time


Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "Bathazare Paige"
message["to"] = "me@bathazarepaige.com"
message["subject"] = "Welcome to Python 🐍"
body = template.substitute(name= "Bathazare") 
message.attach(MIMEText(body,"html"))
message.attach(MIMEImage(Path("profil.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("bathazarepaige@gmail.com", "qnqfthdwqkcdgumv")
    smtp.send_message(message)
    start = time.time()
    start = datetime.fromtimestamp(time.time())
    print(f"Start sending : {start}")
    print("Email sent successfully...🎉🚀")
    end = time.time()
    end = datetime.fromtimestamp(time.time())
    print(f"Ending sending : {end}")
    smtp.quit() 
"""
"""import requests

response = requests.get("https://vip-call-center.com")
print(response)"""

