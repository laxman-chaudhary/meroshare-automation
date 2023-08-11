import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
from datetime import datetime
import json

#send_email("compan","type","to-be-sent@gmail.com","date")
def send_email(company,type,email,date):


    login = "email-id" # paste your login 

    sender_email = login 
    receiver_email = email
    message = MIMEMultipart("alternative") 
    message["Subject"] = f"Share Applied | {company} - {type} on {date}" 
    message["From"] = login 
    message["To"] = receiver_email
    message["cc"] = receiver_email


    html =f"""\
    <html>
    <body>
            <p>User: <b> Alex <b></p>
            <p>Share Type: <b>{type}</b></p>
            <p>Applied Date and Time: <b>{date}</b></p>
            <p>Company Name:<b> {company}</p>

            Thanks,<br>
            Powered by Alex
        </body>
    </html>
            """
    part2 = MIMEText(html, "html") 
    message.attach(part2)

    server=smtplib.SMTP_SSL('smtp-address-or-endpoint',465)
    server.login('smtp-email',"smtp-password")
    server.send_message(message)
    server.quit()
    print('Sent')
    return
