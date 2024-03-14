# ?#    # ckxx xldu jcgf ugol 
# import smtplib, ssl
# from email.message import EmailMessage
# smtp_server="smtp.gmail.com"
# port=587 #For starttls
# sender_email="atimur.basirov@gmail.com"
# # to_email="atimur.basirov@gmail.com"
# password=input("Type your password and press enter: ")
# #Create a secure SSL context
# context=ssl.create_default_context()
# msg= EmailMessage("")
# msg.set_content("Password Recovery")
# msg['Subject']="Password Recovery"
# msg['From']="atimur.basirov@gmail.com"#Try to log in to server and send email
# msg['To']="marina.oleinik@tthk.ee"
# try:
#     server=smtplib.SMTP(smtp_server,port)
#     server.ehlo() #Can be omitted
#     server.starttls(context=context) #Secure the connection
#     server.ehlo() #Can be omitted
#     server.login(sender_email, password)
#     # server.sendmail(sender_email,to_email,msg)
#     server.send_message(msg)
# except Exception as e:
#     #Print any error mesages to stdout
#     print(e)
# finally:
#     server.quit

# from os import *
# from gtts import *
# def loe_failist(fail:str)->list:
#     """Loeme failist read ja salvestame järjendisse. Funktsioon tagastab järjend
#     :param str fail:
#     :rtype: list
#     """
#     f=open(fail,'r',encoding="utf-8") #try
#     järjend=[]
#     for rida in f:
#         järjend.append(rida.strip())
#     f.close()
#     return järjend
# def kirjuta_failisse(fail:str,jarjend=[]):
#     """Funktsion ümber kirjutab andmefailisse
#     """
#     n=int(input("Sisesta mitu elemendi: "))
#     for i in range(n):
#         jarjend.append(input(f"{i+1}. element: "))
#     f=open(fail,'w',encoding="utf-8")
#     for el in jarjend:
#         f.write(el+"\n")
#     f.close()

# def heli(tekst:str,keel:str):
#     obj=gTTS(text=tekst,lang=keel,slow=False).save("heli.mp3")
#     system("heli.mp3")

# tekst=input("Sisesta tekst: ")
# heli(tekst,'et')

# kirjuta_failisse("Text.txt")

# paevad=loe_failist("Paevad.txt")
# print(paevad) 