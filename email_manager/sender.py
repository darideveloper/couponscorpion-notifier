import os
import sys
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from .servers_ports import servers_ports_dic

class Email_manager (): 
    """Manage emails: connect and send mails
    """
    
    def __init__(self, email, password): 
        """Constrcutor of class
        """
        
        # Credentials
        self.email = email
        self.password = password
        
        # Get correct server and port
        email_domain = self.email[self.email.find("@")+1:]
        self.smtp_server = servers_ports_dic[email_domain]["smtp_server"]
        self.smtp_port = servers_ports_dic[email_domain]["smtp_port"]
        
        
    def __connect_smtp (self): 
        """Connect to smtp server for the email
        """
        
        message = "Connecting to smtp..."
        
        # Connect to server and port
        self.smtpObj = smtplib.SMTP (self.smtp_server, self.smtp_port)

        # Send hello to smtp
        self.smtpObj.ehlo()

        # Active encriptation
        self.smtpObj.starttls()

        # login
        self.smtpObj.login (self.email, self.password)
        
        message = "Connected to smtp"
    
    def send_email (
            self, receivers=[], subject="", body="", 
            files=[], html_path=""): 
        """Send email to specific receivers
        """
        
        
        self.__connect_smtp()
        
        # Create text menssage
        menssage = f"Subject: {subject}\n\n{body}"
        
        # Send emails
        for receiver in receivers: 
            
            with_subject = subject != ""
            with_body = body != ""
            with_files = files != []
            with_html_path = html_path != ""
            
            logtext = f"Sending email to: {receiver}. Subject: {with_subject},"
            logtext += f" Body: {with_body}, files: {with_files}, html: {with_html_path}"
                        
            # Make an instance of mime multipart to create the message
            message = MIMEMultipart()

            # Add main part to the email
            message['From'] = self.email
            message["To"] = receiver
            message["Date"] = formatdate(localtime=True)
            message["Subject"] = subject

            # Add text to the email
            if body:
                message.attach (MIMEText(body, "plain"))

            # Loop for files in list
            for file in files:

                # Read file and create email part 
                file_binary = open(file, "rb")
                part = MIMEApplication(file_binary.read(), name=os.path.basename(file))
                file_binary.close()

                # Add file to the message
                part['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(file))
                message.attach(part)

            # Add html from file
            if html_path: 
                template_file = open(html_path, "r")
                html_part = template_file.read()
                message.attach (MIMEText(html_part, "html"))            

            # Send email
            self.smtpObj.sendmail(self.email, 
                            receiver, 
                            message.as_string())

        # Close connection
        self.smtpObj.quit()
