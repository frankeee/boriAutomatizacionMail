# -*- coding: utf-8 -*-
import os
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#import ezgmail
class mailardo:
    def mandaMail(self,filename,recibidor):

        #os.chdir(os.path.join('C:','\\Users','Franco','Documents','archivosproductores',carpeta))
        #ezgmail.send('francocolombini2013@gmail.com', 'charless', 'Body of the email',['2019-10-22_14_2882891_00000_36932_00354_00003036306_A.pdf'])
        
        subject = "Envio Polizas Emitidas CHUBB"
        body = "Estimado,adjunto polizas emitidas."
        sender_email = "francocolombini2013@gmail.com"
        receiver_email = recibidor
        password = "piruji98"
        #fBorisonik@gmail.com
        #ggraieb@gmail.com
        #Davis234
        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email  # Recommended for mass emails
        
        # Add body to email
        message.attach(MIMEText(body, "plain"))
        
        #filename = file   In same directory as script
        
        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        
        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)
        
        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        
        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()
        
        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
            
            server.quit()