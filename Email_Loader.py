import poplib
import email
import smtplib
import imaplib
import os
short_m = 'Are you logging into Steam'
user = 'f.depaz@hotmail.com'
password = 'Yoshi123'

def parser():
    text = open('email.txt')
    message = []
    for lines in text:
        lines = lines.strip()
        if lines != '':
            message.append(lines)
    count = 1
    for line in message:
        if short_m in line:
            code = message[count+1]
            return code
        count+=1

    


def Connection():

##    try:
##        m = poplib.POP3_SSL('pop3.live.com',995)
##        m.user(user)
##        m.pass_(password)
##    except:
##        print('no')
##    else:
##        print('yes')
##
##
##    messageCount = len(m.list()[1])
##
##    for j in m.retr(messageCount)[1]:
##        
##        msg = email.message_from_string(j)
##        
##        p = msg.get_payload()
##
##        print(p)
##        print('\n'*10)
##        print(str(p))
    mail = imaplib.IMAP4_SSL('imap-mail.outlook.com')
    mail.login(user,password)
    mail.list()
    mail.select('inbox')

    result,data = mail.search(None,"ALL")

    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[-1]

    result,data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]

    mail.store(latest_email_id,"+FLAGS",'(\\Deleted)')
    mail.expunge()
    f = open('email.txt','w')
    f.write(raw_email)
    f.close()

    code = parser()

    return code

            

