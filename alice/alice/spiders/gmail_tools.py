# #https://www.youtube.com/watch?v=e-OZeAHFpkw

# import imaplib, email, os

# user = 'infiniteandredoumad@gmail.com'
# password = 'abcdef1124'
# imap_url = 'imap.gmail.com'
# #Where you want your attachments to be saved (ensure this directory exists) 
# attachment_dir = '/home/gordon/p3env/alice/alice/spiders/gmail_attachments'
# # sets up the auth
# def auth(user,password,imap_url):
#     con = imaplib.IMAP4_SSL(imap_url)
#     con.login(user,password)
#     return con
# # extracts the body from the email
# def get_body(msg):
#     if msg.is_multipart():
#         return get_body(msg.get_payload(0))
#     else:
#         return msg.get_payload(None,True)
# # allows you to download attachments
# def get_attachments(msg):
#     for part in msg.walk():
#         if part.get_content_maintype()=='multipart':
#             continue
#         if part.get('Content-Disposition') is None:
#             continue
#         fileName = part.get_filename()

#         if bool(fileName):
#             filePath = os.path.join(attachment_dir, fileName)
#             with open(filePath,'wb') as f:
#                 f.write(part.get_payload(decode=True))
# #search for a particular email
# def search(key,value,con):
#     result, data  = con.search(None,key,'"{}"'.format(value))
#     return data
# #extracts emails from byte array
# def get_emails(result_bytes):
#     msgs = []
#     count = 0
#     for num in result_bytes[0].split():
#         typ, data = con.fetch(num, '(RFC822)')
#         msgs.append(data)
#         count += 1
#         if count > 3:
#             break
#     return msgs

# con = auth(user,password,imap_url)
# con.select('INBOX')

# result, data = con.fetch(b'10','(RFC822)')
# raw = email.message_from_bytes(data[0][1])
# get_attachments(raw)


# msgs = get_emails(search('FROM', 'connect',con))

# for msg in msgs:
#     print(get_body(email.message_from_bytes(msg[0][1])))



#================================================================================



#https://www.youtube.com/watch?v=e-OZeAHFpkw

import imaplib, email, os
from time import sleep

import base64
class gmail_tools:

    def __init__(self, user, password, imap_url, attachment_dir):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.user = user
        self.password = password
        self.imap_url = imap_url
        #Where you want your attachments to be saved (ensure this directory exists) 
        self.attachment_dir = str(self.dir_path + '/gmail_attachments')


    # sets up the auth
    def auth(self, user, password, imap_url):
        con = imaplib.IMAP4_SSL(imap_url)
        con.login(user, password)
        return con

    # extracts the body from the email
    def get_body(self, msg):
        if msg.is_multipart():
            return self.get_body(msg.get_payload(0))
        else:
            return msg.get_payload(None,True)

    # allows you to download attachments
    def get_attachments(self, msg):
        for part in msg.walk():
            if part.get_content_maintype()=='multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            fileName = part.get_filename()

            if bool(fileName):
                filePath = os.path.join(self.attachment_dir, fileName)
                with open(filePath,'wb') as f:
                    f.write(part.get_payload(decode=True))

    #search for a particular email
    def search(self, key, value, con):
        result, data  = con.search(None,key,'"{}"'.format(value))
        return data

    #extracts emails from byte array
    def get_emails(self, result_bytes):
        msgs = []
        count = 0
        for num in result_bytes[0].split():
            typ, data = con.fetch(num, '(RFC822)')
            msgs.append(data)
            count += 1
            if count > 3:
                break
        return msgs

    def find_between(self, s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            print('find_between: ' + str(s[start:end]))
            return s[start:end]
        except ValueError:
            return ''



    



    # def remove_bounced_emails(self):
    #     con = mail.auth(self.user, self.password, self.imap_url)
    #     mailbox_categories = []
    #     mailbox_categories = con.list()
    #     item_index = 0
    #     mailbox_titles = []
    #     for mailbox in mailbox_categories:
    #         print('-------------------')
    #         print(str(item_index))
    #         items = str(mailbox).split(',')
    #         for item in items:
    #             print(str(item))
    #             find_between_first = str('" "')
    #             find_between_last = str(str('"') + str("'"))
    #             mailbox_title = str(mail.find_between(str(item), find_between_first, find_between_last))
    #             print('mailbox_title: ' + mailbox_title)
    #             mailbox_titles.append(mailbox_title)

    #         print('\n')
    #         item_index += 1
    #     #exit()
        
    #     for mailbox_title in mailbox_titles:

    #         #con.select('INBOX')
            
    #         reading_mail = True
    #         if len(mailbox_title) < 5:
    #             reading_mail = False
    #         elif mailbox_title == '[Gmail]/Sent Mail':
    #             reading_mail = False
    #         elif mailbox_title == '[Gmail]':
    #             reading_mail = False
    #         elif mailbox_title == '[Gmail]/Drafts':
    #             reading_mail = False
    #         elif mailbox_title == '[Gmail]/All Mail':
    #             reading_mail = False
    #         elif mailbox_title == '[Gmail]/Trash':
    #             reading_mail = False
    #         while reading_mail == True:
    #             try:
    #                 print('\n')
    #                 print('-------------')

    #                 con.select(mailbox_title)

    #                 print('\n')
    #                 print('=====================')    

    #                 result, data = con.uid('search', None, "ALL")
    #                 i = len(data[0].split()) # data[0] is a space separate string
    #                 print('number of emails: ' + str(i))
    #                 if i == 0:
    #                     reading_mail = False



    #                 for x in range(i):
    #                     print('||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    #                     self.email_to = ''
    #                     self.email_from = ''
    #                     self.email_subject = ''
    #                     self.found_bounced_email = False

    #                     latest_email_uid = data[0].split()[x] # unique ids wrt label selected
    #                     print('reading from ' + mailbox_title)
    #                     print('latest_email_uid: ' + str(latest_email_uid))
    #                     result, email_data = con.uid('fetch', latest_email_uid, '(RFC822)')
    #                     raw_email_data = str(email_data[0][1])
    #                     raw_email = raw_email_data.decode('utf-8')

    #                     print(str(raw_email))
    #                     print('EXITING NOW')
    #                     sleep(3)
    #                     exit()
    #                     if self.found_bounced_email == False:
    #                         #common amazon bounce return subject
    #                         if str(raw_email).find('Delivery Status Notification (Failure)') != -1:
    #                             print('detected bounced email')
    #                             print('Reason: ' + str('Delivery Status Notification (Failure)'))
    #                             print('mail id', latest_email_uid)
    #                             print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    #                             print(str(raw_email))
    #                             print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    #                             if str(raw_email).find(r'The following message to <') != -1:
    #                                 print('+++++++--------------+++++++--------------')
    #                                 print('detected bounced email')
    #                                 print('Reason: ' + str(r'The following message to <'))
    #                                 print('mail id', latest_email_uid)
    #                                 print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    #                                 print(str(raw_email))
    #                                 print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    #                                 self.email_to = str(self.find_between(str(raw_email), r'The following message to <', r'>'))
    #                                 print('+++++++--------------+++++++--------------')
    #                                 print('BOUNCED EMAIL: ' + self.email_to)
    #                                 if len(self.email_to) > 5:
    #                                     with open(self.dir_path + '/bounced_emails.csv', 'a+') as f:
    #                                         f.write(str(self.email_to))
    #                                         f.write('\n')
    #                                         f.close()
    #                                         con.uid('STORE', latest_email_uid, '+X-GM-LABELS', '\\Trash')
    #                                         self.found_bounced_email = True
    #                                 else:
    #                                     print('BOUNCED EMAIL IS EMPTY')
    #                                     exit()
                            
    #                     if self.found_bounced_email == False:
    #                         #common amazon bounce return subject
    #                         if str(raw_email).find(r'\r\nYour message to ') != -1:
    #                             print('+++++++--------------+++++++--------------')
    #                             print('detected bounced email')
    #                             print('Reason: ' + str(r'\r\nYour message to '))
    #                             print('mail id', latest_email_uid)
    #                             print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    #                             print(str(raw_email))
    #                             print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    #                             self.email_to = str(self.find_between(str(raw_email), r'\r\nYour message to ', ' couldn'))
    #                             print('+++++++--------------+++++++--------------')
    #                             print('BOUNCED EMAIL: ' + self.email_to)
    #                             if len(self.email_to) > 5:
    #                                 with open(self.dir_path + '/bounced_emails.csv', 'a+') as f:
    #                                     f.write(str(self.email_to))
    #                                     f.write('\n')
    #                                     f.close()
    #                                     con.uid('STORE', latest_email_uid, '+X-GM-LABELS', '\\Trash')
    #                                 self.found_bounced_email = True
    #                             else:
    #                                 print('BOUNCED EMAIL IS EMPTY')
    #                                 exit()

    #                     if self.found_bounced_email == False:
    #                         #common amazon bounce return subject
    #                         if str(raw_email).find(r'Delivery has failed to these recipients or groups:') != -1:
    #                             print('+++++++--------------+++++++--------------')
    #                             print('detected bounced email')
    #                             print('Reason: ' + str(r'Delivery has failed to these recipients or groups:'))
    #                             print('mail id', latest_email_uid)
    #                             print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    #                             print(str(raw_email))
    #                             print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    #                             self.email_to = str(self.find_between(str(raw_email), str(str(self.user) +  r'>\r\nTo: <'), r'>'))
    #                             print('+++++++--------------+++++++--------------')
    #                             print("find between: " + str("self.email_to = str(self.find_between(str(raw_email), str(str(self.user) +  r'>\r\nTo: <'), r'>'))"))
    #                             print('BOUNCED EMAIL: ' + self.email_to)
    #                             if len(self.email_to) > 5:
    #                                 with open(self.dir_path + '/bounced_emails.csv', 'a+') as f:
    #                                     f.write(str(self.email_to))
    #                                     f.write('\n')
    #                                     f.close()
    #                                     con.uid('STORE', latest_email_uid, '+X-GM-LABELS', '\\Trash')
    #                                     self.found_bounced_email = True
    #                             else:
    #                                 print('BOUNCED EMAIL IS EMPTY')
    #                                 self.email_to = str(self.find_between(str(raw_email), r'Original-Recipient: rfc822;', '\\'))
    #                                 print('+++++++--------------+++++++--------------')
    #                                 print("find between: " + str("self.email_to = str(self.find_between(str(raw_email), r'Original-Recipient: rfc822;', '\\'))"))
    #                                 print('BOUNCED EMAIL: ' + self.email_to)
    #                                 if len(self.email_to) > 5:
    #                                     with open(self.dir_path + '/bounced_emails.csv', 'a+') as f:
    #                                         f.write(str(self.email_to))
    #                                         f.write('\n')
    #                                         f.close()
    #                                         con.uid('STORE', latest_email_uid, '+X-GM-LABELS', '\\Trash')
    #                                         self.found_bounced_email = True
    #                                 else:
    #                                     print('BOUNCED EMAIL IS EMPTY')
    #                                     self.email_to = str(self.find_between(str(raw_email), str(r'From: ' + str(self.user) + r'\r\nTo: '), '\\'))
    #                                     print('+++++++--------------+++++++--------------')
    #                                     print("find between: " + str(r'From: ' + str(self.user) + r'\r\nTo: '), '\\')
    #                                     print('BOUNCED EMAIL: ' + self.email_to)
    #                                     if len(self.email_to) > 5:
    #                                         with open(self.dir_path + '/bounced_emails.csv', 'a+') as f:
    #                                             f.write(str(self.email_to))
    #                                             f.write('\n')
    #                                             f.close()
    #                                             con.uid('STORE', latest_email_uid, '+X-GM-LABELS', '\\Trash')
    #                                             self.found_bounced_email = True
    #                                     else:
    #                                         print('BOUNCED EMAIL IS EMPTY')
    #                                         self.email_to = str(self.find_between(str(raw_email), r'nTo: <', '>'))
    #                                         print('+++++++--------------+++++++--------------')
    #                                         print("find between: " + str("nTo: <', '>'))"))
    #                                         print('BOUNCED EMAIL: ' + self.email_to)
    #                                         if len(self.email_to) > 5:
    #                                             with open(self.dir_path + '/bounced_emails.csv', 'a+') as f:
    #                                                 f.write(str(self.email_to))
    #                                                 f.write('\n')
    #                                                 f.close()
    #                                                 con.uid('STORE', latest_email_uid, '+X-GM-LABELS', '\\Trash')
    #                                                 self.found_bounced_email = True
    #                                         else:
    #                                             print('BOUNCED EMAIL IS EMPTY')
    #                                             exit()

    #                     if self.found_bounced_email == False:
    #                         #common amazon bounce return subject
    #                         if str(raw_email).find(r'r\nX-Failed-Recipients: ') != -1:
    #                             print('+++++++--------------+++++++--------------')
    #                             print('detected bounced email')
    #                             print('Reason: ' + str(r'r\nX-Failed-Recipients: '))
    #                             print('mail id', latest_email_uid)
    #                             print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    #                             print(str(raw_email))
    #                             print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    #                             self.email_to = str(self.find_between(str(raw_email), r'r\nX-Failed-Recipients: ', '\\'))
    #                             print('+++++++--------------+++++++--------------')
    #                             print('BOUNCED EMAIL: ' + self.email_to)
    #                             if len(self.email_to) > 5:
    #                                 with open(self.dir_path + '/bounced_emails.csv', 'a+') as f:
    #                                     f.write(str(self.email_to))
    #                                     f.write('\n')
    #                                     f.close()
    #                                     con.uid('STORE', latest_email_uid, '+X-GM-LABELS', '\\Trash')
    #                                     self.found_bounced_email = True
    #                             else:
    #                                 print('BOUNCED EMAIL IS EMPTY')
    #                                 exit()

    #                     if self.found_bounced_email == False:
    #                         #common amazon bounce return subject
    #                         if str(raw_email).find(r'\n\r\n   ----- The following addresses had permanent fatal errors -----\r\n<') != -1:
    #                             print('+++++++--------------+++++++--------------')
    #                             print('detected bounced email')
    #                             print('Reason: ' + str(r'\n\r\n   ----- The following addresses had permanent fatal errors -----\r\n<'))
    #                             print('mail id', latest_email_uid)
    #                             print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    #                             print(str(raw_email))
    #                             print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    #                             self.email_to = str(self.find_between(str(raw_email), r'\n\r\n   ----- The following addresses had permanent fatal errors -----\r\n<', r'>'))
    #                             print('+++++++--------------+++++++--------------')
    #                             print('BOUNCED EMAIL: ' + self.email_to)
    #                             if len(self.email_to) > 5:
    #                                 with open(self.dir_path + '/bounced_emails.csv', 'a+') as f:
    #                                     f.write(str(self.email_to))
    #                                     f.write('\n')
    #                                     f.close()
    #                                     con.uid('STORE', latest_email_uid, '+X-GM-LABELS', '\\Trash')
    #                                     self.found_bounced_email = True
    #                             else:
    #                                 print('BOUNCED EMAIL IS EMPTY')
    #                                 exit()

    #                 reading_mail = False
    #             except Exception as e: 
    #                 print('EXCEPTION: ')
    #                 print(e)
    #                 reading_mail = False
    #             print('||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    #             #sleep(0.3)
    #             #con.expunge()

    def send_email_to_trash(self, con, content, latest_email_uid, email_to):
        print('SENDING' + str(email_to) +  ' TO TRASH ')
        print('SENDING' + str(email_to) +  ' TO TRASH ')
        print('SENDING' + str(email_to) +  ' TO TRASH ')
        email_to = email_to.replace(' ', '')

        if len(email_to) > 5 and email_to.find('@') != -1:
            if email_to.find('>') != -1 and email_to.find('<') != -1:
                email_to = self.find_between(email_to, '<', '>')

            with open(self.dir_path + '/unsubscribed_emails.csv', 'a+') as f:
                f.write(str(email_to).rstrip())
                f.write('\n')
                f.close()
                con.uid('STORE', latest_email_uid, '+X-GM-LABELS', '\\Trash')
                print('+++++++--------------+++++++--------------')
                print('Unsubscribed EMAIL: ' + email_to)
                print('TRASHED' + str(email_to) )
                print('TRASHED' + str(email_to) )
                print('TRASHED' + str(email_to) )
                print('+++++++--------------+++++++--------------')
                return True
        else:
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print('FAILED' + str(email_to))
            print('FAILED' + str(email_to))
            print('FAILED' + str(email_to))
            print('content: ' + content)
            print('email_to: ' + email_to)
            print('I found a problem with the email')
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            #exit()
            return False

        if len(email_to) > 70:
            print('the length is far too long for an email exiting now!')
            print('debug this')
            exit()
        
        #print('removed one email and exited')
        #exit()


    def remove_unsubscribed_emails(self):
        con = mail.auth(self.user, self.password, self.imap_url)
        mailbox_categories = []
        mailbox_categories = con.list()
        item_index = 0
        mailbox_titles = []
        for mailbox in mailbox_categories:
            print('-------------------')
            print(str(item_index))
            items = str(mailbox).split(',')
            for item in items:
                print(str(item))
                find_between_first = str('" "')
                find_between_last = str(str('"') + str("'"))
                mailbox_title = str(mail.find_between(str(item), find_between_first, find_between_last))
                print('mailbox_title: ' + mailbox_title)
                mailbox_titles.append(mailbox_title)

            print('\n')
            item_index += 1
        #exit()
        
        for mailbox_title in mailbox_titles:

            #con.select('INBOX')
            
            reading_mail = True
            if len(mailbox_title) < 5:
                reading_mail = False
            elif mailbox_title == '\\Trash':
                reading_mail = False
            elif mailbox_title == 'Non-Daemon':
                reading_mail = False
            elif mailbox_title == 'Daemon':
                reading_mail = False
            elif mailbox_title == '[Gmail]/Sent Mail':
                reading_mail = False
            elif mailbox_title == '[Gmail]':
                reading_mail = False
            elif mailbox_title == '[Gmail]/Drafts':
                reading_mail = False
            elif mailbox_title == '[Gmail]/All Mail':
                reading_mail = False
            elif mailbox_title == '[Gmail]/Trash':
                reading_mail = False
            elif mailbox_title == '[Gmail]/Important':
                reading_mail = False

            reading_mail = False

            # if mailbox_title == 'remove-request':
            #     reading_mail = True
            # elif mailbox_title == 'Daemon':
            #     reading_mail = True


            if mailbox_title == 'INBOX':
                reading_mail = True

            while reading_mail == True:
                try:
                    print('\n')
                    print('-------------')

                    con.select(mailbox_title)

                    print('\n')
                    print('=====================')    

                    result, data = con.uid('search', None, "ALL")
                    i = len(data[0].split()) # data[0] is a space separate string
                    print('number of emails: ' + str(i))
                    if i == 0:
                        reading_mail = False

                    for x in range(i):
                        print('||||||||||||||||||||||||||||||||||||||||||||||||||||||')
                        self.email_to = ''
                        self.email_from = ''
                        self.email_subject = ''
                        self.unsubscribed_email = False

                        latest_email_uid = data[0].split()[x] # unique ids wrt label selected
                        print('reading from ' + mailbox_title)
                        print('latest_email_uid: ' + str(latest_email_uid))
                        result, email_data = con.uid('fetch', latest_email_uid, '(RFC822)')
                        raw_email_data = email_data[0][1]

                        raw_email = raw_email_data.decode('utf-8')

                        raw_email = raw_email.lower()
                        body = ''
                        mailbox_trigger = ''
                        mailbox_trigger_string_list = [
                            "b'unsubscribe",
                            'Please opt me out',
                            'remove me',
                            'remove us',
                            '\nunsubscribe',
                            'Subject: Unsubscribe',
                            'unsubscribe me',
                            'Please unsubscribe',
                            'complaints@',
                            'Pls Unsubscribe',
                            'Please delete us',
                            'Take me off of your marketing',
                            'Please STOP',
                            'has been received and is being reviewed by our support staff',
                            'PLEASE REMOVE',
                            'delete me',
                            'Valued Customer',
                            'our support team',
                            'Please immediately stop',
                            'harass',
                            'We do not need medical auditing services',
                            'abuse report',
                            'THIS IS A CHURCH',
                            'Thank you for contacting the Concerns Team',
                            'received your support request',
                            'no longer maintained',
                            'wrong department',
                            'nsubject: stop',
                            'nsubject: unsubscribe',
                            'nsubject: delete',
                            'Please opt out',
                            'Stop emailing me',
                            'remove my',
                            'being reviewed by our support staff',
                            'Support Team will contact you',
                            'immediately stop',
                            'wrong department',
                            'Unsubscribe me',
                            'received and is being reviewed',
                            'Dear Customer',
                            'the Clerk',
                            'sheriff',
                            'Laba diena',
                            'Your inquiry',
                            'obituary',
                            'Customer Service',
                            'por favor',
                            'We have received your case',
                            'Your case has been submitted',
                            'ticket has been created',
                            'error occurred while trying to deliver',
                            'the following message to <',
                            'recipient address rejected:',
                            'subject: delivery failure (',
                            "couldn't be delivered."
                            

                        ]
                        mailbox_triggered = False
                        is_base64 = False
                        print('--------SCANNING------')
                        print('--------FOR TRIGGERS------')
                        print('--------SCANNING------')
                        print('--------FOR TRIGGERS------')
                        print('--------SCANNING------')
                        print('--------FOR TRIGGERS------')
                        print(raw_email)
                        mailbox_trigger = ''
                        for trigger in mailbox_trigger_string_list:
                            mailbox_trigger = str(trigger.lower())
                            #print('searching for: ' + mailbox_trigger)
                            # print(body)
                            
                            lines = raw_email.split(r'\r')
                            #exit()
                            i = 0
                            for line in lines:
                                # print(str(i) + ' | raw  | ' + str(line))
                                # print(str(i) + ' |mail| ' + str(mailbox_trigger))
                                # print(str(i) + ' |scan|' + str(mailbox_title) + ' ' +  str(latest_email_uid) + ' |')

                                if line.find(mailbox_trigger) != -1:
                                    mailbox_triggered = True
                                    is_base64 = False
                                    print('MAILBOX TRIGGERED')
                                    print('REASON: ')
                                    print(mailbox_trigger)
                                    # exit()
                                    break
                                i += 1
                                # sleep(0.05)
                            #exit()


                        if mailbox_triggered == False:
                            
                            try:
                                msg = email.message_from_string(raw_email)
                                for part in msg.walk():
                                    # each part is a either non-multipart, or another multipart message
                                    # that contains further parts... Message is organized like a tree
                                    if part.get_content_type() == 'text/plain':
                                        body = str(base64.b64decode(part.get_payload())).lower()
                                        # print(body) # prints the raw text
                                        is_base64 = True
                            except Exception as e:
                                print(str(e))
                                #exit()

                            if is_base64:
                                mailbox_trigger = ''
                                for trigger in mailbox_trigger_string_list:
                                    mailbox_trigger = str(trigger.lower())
                                    #print('searching for: ' + mailbox_trigger)
                                    # print(body)
                                    
                                    lines = body.split(r'\r')
                                    #exit()
                                    i = 0
                                    for line in lines:
                                        # print(str(i) + ' |base64| ' + str(line))
                                        # print(str(i) + ' | 64 | ' + str(mailbox_trigger))
                                        # print(str(i) + ' |scan| ' + str(mailbox_title) + ' ' +  str(latest_email_uid) + ' |')

                                        if line.find(mailbox_trigger) != -1:
                                            mailbox_triggered = True
                                            print('MAILBOX TRIGGERED')
                                            print('REASON: ')
                                            print(mailbox_trigger)
                                            # exit()
                                            break
                                        i += 1
                                        #sleep(0.2)
                                #exit()

                        print('----------------------')                        
                        if mailbox_triggered == True: 
                        
                            print('detected unsubscribe email')
                            print('Reason: ' + mailbox_trigger)
                            print('mail id', latest_email_uid)
                            print('+++++++++++++++++ RAW HTML RAW HTML +++++++++++++++++++++++++')
                            print('+++++++++++++++++ RAW HTML RAW HTML +++++++++++++++++++++++++')
                            print('+++++++++++++++++ RAW HTML RAW HTML +++++++++++++++++++++++++')
                            print(raw_email)
                            print('+++++++++++++++++ BODY BODY BODY +++++++++++++++++++++++++')
                            print('+++++++++++++++++ BODY BODY BODY +++++++++++++++++++++++++')
                            print('+++++++++++++++++ BODY BODY BODY +++++++++++++++++++++++++')
                            print(body)
                            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

                            if self.unsubscribed_email == False and is_base64 == True:
                                email_to_start = str('to:' + str(self.find_between(body, 'to:', '<')) + '<')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = '>'
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(body, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, body, latest_email_uid, self.email_to)


                            if self.unsubscribed_email == False and is_base64 == True:
                                email_to_start = str('to: ')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = '\\'
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(body, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, body, latest_email_uid, self.email_to)



                            if self.unsubscribed_email == False and is_base64 == False:
                                email_to_start = str('reply-to: ')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = 'to:'
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(body, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, body, latest_email_uid, self.email_to)



                            if self.unsubscribed_email == False and is_base64 == False:
                                email_to_start = str('from: ' + str(self.find_between(body, 'from: ', '<')) + '<')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = '>'
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(body, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, body, latest_email_uid, self.email_to)


                            if self.unsubscribed_email == False and is_base64 == False:
                                email_to_start = str('550 5.4.1 [')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = ']'
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(raw_email, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, raw_email, latest_email_uid, self.email_to)


                            if self.unsubscribed_email == False and is_base64 == False:
                                email_to_start = str('return-path: <')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = '>'
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(raw_email, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, raw_email, latest_email_uid, self.email_to)


                            if self.unsubscribed_email == False and is_base64 == True:
                                email_to_start = str('from: ' + str(self.find_between(raw_email, 'from: ', '<')) + '<')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = '>'
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(raw_email, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, raw_email, latest_email_uid, self.email_to)
                                #exit()


                            if self.unsubscribed_email == False and is_base64 == False:
                                email_to_start = str('the following message to <')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = '> was undeliverable'
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(raw_email, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, raw_email, latest_email_uid, self.email_to)
                                #exit()


                            if self.unsubscribed_email == False and is_base64 == False:
                                email_to_start = str("failed to deliver to '")
                                print('email_to_start: ' + email_to_start)
                                email_to_end = "'"
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(raw_email, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, raw_email, latest_email_uid, self.email_to)
                                #exit()

                            if self.unsubscribed_email == False and is_base64 == False:
                                email_to_start = str('	for <')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = '>'
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(raw_email, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, raw_email, latest_email_uid, self.email_to)
                                #exit()

                            #- 5.1.1 <
                            #>

                            if self.unsubscribed_email == False and is_base64 == False:
                                email_to_start = str('- 5.1.1 <')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = '>'
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(raw_email, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, raw_email, latest_email_uid, self.email_to)
                                #exit()

                            if self.unsubscribed_email == False and is_base64 == False:
                                email_to_start = str('original-recipient: <')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = '>'
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(raw_email, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, raw_email, latest_email_uid, self.email_to)
                                #exit()

                            if self.unsubscribed_email == False and is_base64 == False:
                                email_to_start = str('subject: delivery failure (')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = ')'
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(raw_email, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, raw_email, latest_email_uid, self.email_to)
                                #exit()


                            if self.unsubscribed_email == False and is_base64 == False:
                                email_to_start = str('diagnostic-code: smtp; 550 5.1.1 <')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = '>'
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(raw_email, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, raw_email, latest_email_uid, self.email_to)
                                #exit()


                            if self.unsubscribed_email == False and is_base64 == False:
                                email_to_start = str('following message to <')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = '> was unde'
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(raw_email, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, raw_email, latest_email_uid, self.email_to)
                                #exit()

                            if self.unsubscribed_email == False and is_base64 == False:
                                email_to_start = str('ssage you sent to ')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = ' couldn'
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(raw_email, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, raw_email, latest_email_uid, self.email_to)
                                #exit()

                            if self.unsubscribed_email == False and is_base64 == False:
                                email_to_start = str('5.7.1 <')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = '>'
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(raw_email, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, raw_email, latest_email_uid, self.email_to)
                                #exit()

                            if self.unsubscribed_email == False and is_base64 == False:
                                email_to_start = str('5.4.1 [')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = ']'
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(raw_email, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, raw_email, latest_email_uid, self.email_to)
                                #exit()

                            if self.unsubscribed_email == False and is_base64 == False:
                                email_to_start = str('final-recipient: rfc822; ')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = '\n'
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(raw_email, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, raw_email, latest_email_uid, self.email_to)
                                #exit()

                            if self.unsubscribed_email == False and is_base64 == False:
                                email_to_start = str('final-recipient: rfc822;')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = '\n'
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(raw_email, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, raw_email, latest_email_uid, self.email_to)
                                #exit()


                            if self.unsubscribed_email == False and is_base64 == False:
                                email_to_start = str('your message to ')
                                print('email_to_start: ' + email_to_start)
                                email_to_end = " couldn't be delivered."
                                print('email_to_end: ' + str(email_to_end))
                                self.email_to = str(self.find_between(raw_email, str(email_to_start), str(email_to_end)))
                                print('self.email_to: ' + self.email_to)
                                self.unsubscribed_email = self.send_email_to_trash(con, raw_email, latest_email_uid, self.email_to)
                                #exit()

                            if self.unsubscribed_email == False:
                                print(' +++++++++++++++++')
                                print('I was unable to find that email')
                                print(' +++++++++++++++++')
                                print(' +++++++++++++++++ RAW +++++++++++++++++++ ')
                                print(' +++++++++++++++++')
                                print(raw_email)
                                print(' +++++++++++++++++')
                                print(' ++++++++++++++++ BODY ++++++++++++++++++  ')
                                print(' +++++++++++++++++')
                                print(body)
                                print(' +++++++++++++++++')
                                print(' +++++++++++++++++')
                                print('+++++++--------------+++++++--------------')
                                print('BASE64 = ' + str(is_base64))
                                print('Examining: raw_email')
                                print('detected unsubscribe email')
                                print('Reason: ' + mailbox_trigger)
                                print('mail id', latest_email_uid)
                                print('I was unable to find that email')
                                exit()
                            else:
                                print('+++++++--------------+++++++--------------')
                                print('BASE64 = ' + str(is_base64))
                                print('Examining: raw_email')
                                print('detected unsubscribe email')
                                print('Reason: ' + mailbox_trigger)
                                print('mail id', latest_email_uid)

                    reading_mail = False
                except Exception as e: 
                    print('EXCEPTION: ')
                    print(e)
                    reading_mail = False
                print('||||||||||||||||||||||||||||||||||||||||||||||||||||||')
                #sleep(0.3)
                #con.expunge()



if __name__ == '__main__':

    # user = 'infiniteandredoumad@gmail.com'
    # password = 'abcdef1124'
    # imap_url = 'imap.gmail.com'

    user = 'connect@ahaplink.com'
    password = '!Tufankji1124'
    imap_url = 'imap.gmail.com'

    #Where you want your attachments to be saved (ensure this directory exists) 
    attachment_dir = '/home/gordon/p3env/alice/alice/spiders/gmail_attachments'

    mail = gmail_tools(user, password, imap_url, attachment_dir)
    #mail.remove_bounced_emails()
    mail.remove_unsubscribed_emails()

