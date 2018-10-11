import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("lekhana016@gmail.com","password")
msg="Hello!"
server.sendmail("lekhana016@gmail.com","poojitha202@gmail.com",msg)
print('msg sent')
server.quit()