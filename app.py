import os                # This is used for system function
import math          # The math library
import random     # For random numbers
import smtplib      # For email functions

num = "0123456789"
val = ""
for i in range(0,6):
    val =val + num[math.floor(random.random()*10)]
OTP = val + " is your One-Time-Password for verification"
message = OTP



email = smtplib.SMTP('smtp.gmail.com', 587)  # To call the gmail account client
email.starttls()
email.login("deepakkamboj4672@gmail.com", "pngaykjrwzoeupqx")
 # Sending the OTP email
def send(id):
    email.sendmail('&&&&&&&&&&&', id, message) 

def verify_otp(otp):
    if otp == val :
        return 1
    else:
        return 0

