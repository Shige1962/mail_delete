import imapclient, ssl, sys, pprint, imaplib, getpass

imaplib._MAXLINE = 10000000 

print("Please choose a number below to conitue")
print("1. Gmail")
print("2.Yahoo Japan Mail")
print('3. For exit')

while_enterd = True

while while_enterd:
    try:
        mode = int(input("Number: "))
        if mode > 0 and mode < 4:
            while_enterd = False   
    except Exception as e:
        print("Please enter valid number")
    print("Value must be a number between 1 and 3")        
        
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

def mail_delete(mail_server):
    print( mail_server + " is chosen") 
    imap_obj = imapclient.IMAPClient("imap.gmail.com", ssl=True, ssl_context=context)
    print('Please type your email of ' + mail_server + ' account that ends with ' +domain)
    mail_ad = input("email:")
    print('Please type your password for ' + mail_server)
    mail_pass = getpass.getpass("Password:")
    try: 
        imap_obj.login(mail_ad, mail_pass)
    except Exception as e:
        # print("Error message: " + e)
        print(exception_message)
        exit()
    print("Logged in successfully")
    # pprint.pprint(imap_obj.list_folders()) # To return folders of mail in list 
    imap_obj.select_folder("Inbox", readonly=False)
    print("Please type an email address that you want to delete from your inbox")
    delete_ad = input("email:")
    enterd = True
    while enterd: 
        UIDs = imap_obj.search(["FROM", delete_ad])
        number_of_mail = len(UIDs)
        print("There are " + str(number_of_mail) + " mails. Would you like to delte them all?")
        answer = input("y/n?:")
        if answer.lower() == "y":
            print("Deleting all the mails. This may take for a while...")
            for delete_id in UIDs:
                imap_obj.delete_messages(delete_id)
        else: 
            enterd = False
        imap_obj.expunge()
        print("Mails delted successfully")
        print("Would you like to delete other mails?")
        answer = input("y/n?:")
        if answer.lower() == "y":
            print("Please type an email address that you want to delete from your inbox")
            delete_ad = input("email:")
        else:
            enterd = False
    imap_obj.logout()
    print("Logging out from the mail server")
    exit()

if mode == 1:
    domain = '"@gmail.com"'
    exception_message = ("If you haven't created App password on your account yet, \n please refer to https://support.google.com/accounts/answer/185833?hl=en and set App password before you run this programme")
    mail_delete("Gmail")

elif mode == 2:
    domain = '"@gmail.com"'
    exception_message = ("Email or passowrod is not correct. Please try again")
    mail_delete("Yahoo Japan Mail")
    
elif mode == 3:
    print("Exit")




