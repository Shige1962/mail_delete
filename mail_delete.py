import imapclient, ssl, sys, pprint, imaplib

imaplib._MAXLINE = 10000000 

try:
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

    if mode == 1:
        print("Gmail is chosen") 
        imap_obj = imapclient.IMAPClient("imap.gmail.com", ssl=True, ssl_context=context)
        print('Please type your email of Google account that ends with "@gmail.com"')
        mail_ad = input("email:")
        print('Please type your App password for gmail')
        mail_pass = input("App password:")
        try: 
            imap_obj.login(mail_ad, mail_pass)
        except Exception as e:
            print("Error message: " + e)
            print("If you haven't created App password on your account yet,")
            print("please refer to https://support.google.com/accounts/answer/185833?hl=en and set App password before you run this programme")
            exit()
        print("Logged in successfully")
        # pprint.pprint(imap_obj.list_folders()) # To return folders of mail in list 
        imap_obj.select_folder("Inbox", readonly=False)
        enterd = True

        print("Please type an email address that you want to delete from your inbox")
        delete_ad = input("email:")
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
                imap_obj.logout()
                print("Logging out from the mail server")
                exit()
            imap_obj.expunge()
            print("Mails delted successfully")
            print("Would you like to delete other mails?")
            answer = input("y/n?:")
            if answer.lower() == "y":
                print("Please type an email address that you want to delete from your inbox")
                delete_ad = input("email:")
            else:
                imap_obj.logout()
                print("Logging out from the mail server")
                exit()
        imap_obj.logout()

    elif mode == 2:
        print("Yahoo Japan Mail is chosen")
        imap_obj = imapclient.IMAPClient("imap.mail.yahoo.co.jp", ssl=True, ssl_context=context)
        print('Please type your email of Yahoo account that ends with "@yahoo.co.jp"')
        mail_ad = input("email:")
        print('Please type your password for Yahoo Japan Mail')
        # print("If you haven't created App password on your account yet,")
        # print("please refer to https://support.google.com/accounts/answer/185833?hl=en and set App password before you run this programme")
        mail_pass = input("Password:")
        # Insert Exception later 
        imap_obj.login(mail_ad, mail_pass)
        print("Logged in successfully")
        imap_obj.select_folder("Inbox", readonly=False)

        enterd = True
        print("Please type an email address that you want to delete from your inbox")
        delete_ad = input("email:")
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
        print("Logging out from the mail server")
        imap_obj.logout()
        exit()
    elif mode == 3:
        print("Exit")

except Exception as e:
    print("An unknown exception error has occurred.Ending programme...")
    print(e)
    exit()



