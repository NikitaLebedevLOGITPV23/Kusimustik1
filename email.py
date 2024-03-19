#zmje xmra itxt kkdn
import smtplib, ssl
from email.message import EmailMessage
import imghdr
smtp_server = "smtp.gmail.com"
port = 587 #For starttls
sender_email = "nikitalebedev2006molnija@gmail.com"
password = input("Kirjuta oma salasõna ja vajuta enter: ")
context = ssl.create_default_context()
#msg="Tere tulemast!"
msg = EmailMessage()
msg.set_content("Tere tulemast! Olen kirja teha!")
msg["Subject"]="Kirja teema"
msg["From"]="Nikita Lebedev"
msg["To"]="nikitalebedev2006molnija@gmail.com"
with open("images.jpg","rb") as fplit:
    pilt=fplit.read()
msg.add_attachment(pilt,maintype="image",subtype=imghdr.what(None, pilt))
try:
    server = smtplib.SMTP(smtp_server,port)
    server.starttls(context=context) #Secure the connextion
    server.login(sender_email,password)
    server.send_message(msg) #server.sendmail(sender_email,to_email,msg)
    print("Krija on saatnud")
except Exception as e:
     print(e)
finally:
    server.quit()