import smtplib, ssl


smtp_server = "box2527.bluehost.com"
port = 465

sender = "me@bathazarepaige.com"
password = input("Enter your password here : ")

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    print("It worked 🎉")
    
