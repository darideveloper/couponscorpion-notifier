import os
import sys
import imaplib
import pyzmail
import imapclient
from .servers_ports import servers_ports_dic

current_dir = os.path.dirname(__file__)
current_file = os.path.basename(__file__)

class Email_manager (): 
    """Manage emails: connect and send mails
    """
    
    def __init__(self, email, password, server=None, port=None): 
        """Constrcutor of class
        """
        
        # Credentials
        self.email = email
        self.password = password
        
        # Get correct server and port
        email_domain = self.email[self.email.find("@")+1:]
        if server:
            self.imap_server = server
        else:
            self.imap_server = servers_ports_dic[email_domain]["imap_server"]

        if port:
            self.imap_port = port
        else:
            self.imap_port = servers_ports_dic[email_domain]["imap_port"]
        
        # Update the number of bytes to use in the program
        imaplib._MAXLINE = 10000000
        
        # Login
        self.__connect_imap()
        
    def __connect_imap (self): 
        """Connect to imap server for the email
        """
        
        # Contect to imap server 
        self.imapObj = imapclient.IMAPClient (self.imap_server, ssl=True)

        # Login to email account
        self.imapObj.login (self.email, self.password)
        
    def get_folders (self): 
        """return a list of folders in email service

        Returns:
            list: folders in email services
        """
        
        return self.imapObj.list_folders()        
    
    def set_folder (self, folder): 
        """Set emails folder for reader class

        Args:
            folder (str): folder name, like "Inbox"
        """
    
        # Use specific folder
        self.imapObj.select_folder (folder, readonly=False)
    
    def get_uids (self, search_query=None, last_emails_num=0):

         # Seach emails (get uid: unique identifiers)
        if search_query:
            email_uids = self.imapObj.search (search_query)
        else: 
            email_uids = self.imapObj.search ('ALL')
            
        
        # Get the specific number of last emails
        if last_emails_num:
            uids = email_uids[-last_emails_num:]
        else: 
            uids = email_uids
        
        return uids

    def get_emals (self, uids): 
                
        # Loop for each uid
        emails = []
        for uid in uids:

            # Get the raw content of the last email
            rawMessages = self.imapObj.fetch([uid], ['BODY[]', 'FLAGS'])

            # Process email as pzmail object
            message = pyzmail.PyzMessage.factory(rawMessages[uid][b'BODY[]'])

            # Get email subject
            subject = str(message.get_subject()).replace("\r", "").replace("\n", "")
            
            # Get from email
            from_email = message.get_addresses('from')[0]
            
            # Get to email
            try:
                to_email = message.get_addresses('to')[0]
            except: 
                to_email = "Mail without to email"
            
            # Get body
            try:
                body = message.text_part.get_payload().decode(message.text_part.charset)   
            except:                 
                body = "Mail without a body text part"

            try:
                html = message.html_part.get_payload().decode(message.html_part.charset)
            except:
                html = "Mail without a html part"


            emails.append({
                "uid": uid,
                "subject": subject,
                "from_email":from_email, 
                "to_email":to_email,
                "body":body, 
                "html": html         
            })
        
        return emails
    
    def move_emails (self, uids=[], to_fodler=""):
        
        self.imapObj.move (uids, to_fodler)
    
    def get_files (self, uids=[], download_path="", extenion=".pdf"):

        for uid in uids:
    
            # Get the raw content of the last email
            rawMessages = self.imapObj.fetch([uid], ['BODY[]', 'FLAGS'])

            # Process email as pzmail object
            message = pyzmail.PyzMessage.factory(rawMessages[uid][b'BODY[]'])

            # Loop for each part in the email
            for index_part in range (1, len(message.get_payload())): 
                
                # Read each file in the current part
                for part in message.get_payload(index_part).walk():

                    file_name = part.get_filename()

                    # Verify the name of the file
                    if str(file_name).lower().strip().endswith(extenion): 
                        print (f"Downloading file: {file_name}...")

                        # Create path of file
                        file_path = os.path.join (download_path, file_name)
                        
                        # Save file
                        file_obj = open (file_path, "wb")
                        file_obj.write (part.get_payload(decode=True))
                        file_obj.close()

