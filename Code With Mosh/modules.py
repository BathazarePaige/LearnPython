#from datetime  import datetime, timedelta

"""
dt = datetime(2023, 2, 23)
dt = datetime.now()
dt = datetime.strptime("2023/2/23", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())


print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))"""



"""dt1 = datetime(2023, 1, 1)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)"""

"""import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1,2,3,4]))
print(random.choices([1,2,3,4], k=2))
print(",".join(random.choices("abcdefghi", k=4)))

print(string.digits)
"""
"""import webbrowser

print("Deployment completed 🚀")

webbrowser.open("https://www.udemy.com/courses/search/?src=ukw&q=Python+Algorithmes")"""

"""from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl

message = MIMEMultipart()
message["from"] = "me@bathazarepaige.com"
message["to"] = "bathazarepaige@gmail.com"
message["subject"] = "This is my 1st email test in python"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host="smtp.gmail.com ", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls
    smtp.login("me@bathazarepaige.com", "Y@ounde-2023")
    smtp.send_message(message)
    print("sent...")"""

"""import os 
from email.message import EmailMessage
import ssl
import smtplib

email_sender = "me@bathazarepaige.com"
email_password = "Y@ounde-2023"
email_receiver = "bathazarepaige@gmail.com"

subject = "Check my 3rd test email📨"

#body = """ #Hello Paige \n
#Here is my 3rd python test email.
#Regards

"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("box2527.bluehost.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    print("Sent...🚀")"""

"""import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login("bathazarepaige@gmail.com", "qnqfthdwqkcdgumv")
subject = "Test mail from python"
server.sendmail("bathazarepaige@gmail.com","saturainvincent@gmail.com", "Test mail from python")
print("Sent...🎉🚀")"""
"""
import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login("bathazarepaige@gmail.com", "qnqfthdwqkcdgumv")

from_addr = "bathazarepaige@gmail.com"
to_addr = "saturainvincent@gmail.com"
subject = "Test mail from python"
body = "Hello Vincent, \n This is a test email from Python"

message = f"Subject:{subject}\n\n{body}"

server.sendmail(from_addr, to_addr, message)

server.quit()
print("Sent...🎉🚀")"""

#import os 
#from email.message import EmailMessage
#import ssl
#import smtplib
"""
email_sender = "me@bathazarepaige.com"
email_password = "Y@ounde-2023"
email_receiver = "saturainvincent@gmail.com"

subject = "Check my 3rd test email📨"

#body = """ #Hello Paige \n
#Here is my 3rd python test email.
#Regards

"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("box2527.bluehost.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    print("Sent...🚀")"""

"""
import smtplib, ssl


smtp_server = "smtp.gmail.com"
port = 587

sender = "bathazarepaige@gmail.com"
password = input("Enter your password : ")


context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    server.starttls(context=context)
    server.login(sender, password)
    #send mail
    print("It worked 🎉")
except Exception as e:
    print(e)
finally:
    server.quit()"""


"""import smtplib, ssl


smtp_server = "smtp.gmail.com"
port = 465

sender = "bathazarepaige@gmail.com"
password = input("Enter your password : ")

receiver = "me@bathazarepaige.com"
#message = """\
#From : {}
#To : {}
#Subject : Hi there!
#This message was sent from python

""".format(sender,receiver)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
    server.login(sender, password)
    #send email  
    server.sendmail(sender, receiver, message)
print("Email was sent 🚀")"""

"""import smtplib

gmail_user = "bathazarepaige@gmail.com"
gmail_password = "qnqfthdwqkcdgumv"

sent_from = gmail_user
to = ["me@bathazarepaige.com", "saturainvincent@gmail.com"]
subject = "Lorem ipsum dolor sit amet"
body = "consecteur adipiscing elit"


email_text = """
#From: %s
#To: %s
#Subject: %s


#%s
"""%(sent_from,", ".join(to),subject, body)

try:
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp_server.ehlo()
    smtp_server.login(sent_from, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print("Email sent successfully 🎉🚀")
except Exception as ex:
    print("Something went wrong...", ex)"""




from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from re import template
import smtplib, ssl
from string import Template 
from datetime import datetime
import time

template = Template(Path("template.html").read_text())

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
