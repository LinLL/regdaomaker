from imap_tools import MailBox, A, BaseMailBox
import re

class ImapMail(object):
    def __init__(self, mail, passwd, mailserver="pop-mail.outlook.com"):
        self.mailserver = mailserver
        self.mail = mail
        self.passwd = passwd


    def checkStatus(self):
        try:
            with MailBox(self.mailserver).login(self.mail, self.passwd) as mailbox:
                print(mailbox.login_result)
                return True
        except Exception as e:
            print(e)
            return False

    def checkAllStatus(self, mail_list: list):
        success = []
        failed = []

        for mail in mail_list:
            if self.checkStatus(mail['addr'], mail['pwd']):
                success.append(mail)
            else:
                failed.append(mail)
        print(success)
        print(failed)
        return success, failed

    def searchSubject(self, subject):
        with MailBox(self.mailserver).login(self.mail, self.passwd) as mailbox:
            for msg in mailbox.fetch(A(subject=subject)):
                return msg

    def searchSender(self, sender):
        with MailBox(self.mailserver).login(self.mail, self.passwd) as mailbox:
            for msg in mailbox.fetch(A(from_=sender)):
                return msg

    def getAllMailSubject(self):
        subjects = []
        with MailBox(self.mailserver).login(self.mail, self.passwd) as mailbox:
            for msg in mailbox.fetch():
                subjects.append(msg.subject)

        return subjects

    def parseRegMail(self, msg):
        api_pattern = re.compile(r'https?://api\.\S+')
        first_api = api_pattern.search(msg.text).group()
        return first_api

def getAllMailList(path="../data/mailspwd"):
    mail_list = []
    with open(path, 'r') as fr:
        for line in fr.readlines():
            mail, pwd = line.split("|")
            pwd = pwd.strip()
            mail_list.append({"addr": mail, "pwd": pwd})
    return mail_list

def checkAllStatus(path="../data/mailspwd"):
    mail_list = getAllMailList(path)
    for mail, pwd in mail_list:
        myImap = ImapMail(mail, pwd)
        print(mail, myImap.checkStatus())



if __name__ == '__main__':
    # mail_list = []
    # with open("../data/mailspwd", 'r') as fr:
    #     for line in fr.readlines():
    #         mail, pwd = line.split("|")
    #         pwd = pwd.strip()
    #         mail_list.append({"addr": mail, "pwd": pwd})
    #         break

    #checkAllStatus()

    testImapMail = ImapMail("abkalodessaw@hotmail.com","72plzQ38")
    msg = testImapMail.searchSubject("Confirm your account")
    result = testImapMail.parseRegMail(msg)
    print(result)
    # subs = testImapMail.getAllMailSubject()
    # print(subs)


