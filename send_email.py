from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Modify these to change sender and receivers
SENDER = "uqzian.wang@qq.com"
RECEIVERS = ["wza913248383@gmail.com"]

client = SMTP_SSL("smtp.qq.com")

client.login(user='uqzian.wang@qq.com', password='oqmeyrjjrwzsbcec')

msg = MIMEMultipart()

msg['From'] = "Lewis Alex"
msg['To'] = RECEIVERS[0]


def send_image(name, text_string):
    with open(name, "rb") as f:
        img = MIMEImage(f.read(), name=name)
        msg.attach(img)
        
    text = MIMEText(text_string)
    msg.attach(text)
def send_email(text, subject):
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    try:
        # send_image('WechatIMG103.jpeg', "testing string")
        client.sendmail(from_addr=SENDER, to_addrs=RECEIVERS, msg=msg.as_string())
        print("Successfully sent email")
    except:
        print("Fail due to exception raised")

send_email("This is an email sent from python script", "Testing email")
client.quit()

