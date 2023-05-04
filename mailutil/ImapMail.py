from imap_tools import MailBox, A, BaseMailBox

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



if __name__ == '__main__':
    mail_list = []
    with open("../data/mailspwd", 'r') as fr:
        for line in fr.readlines():
            mail, pwd = line.split("|")
            pwd = pwd.strip()
            mail_list.append({"addr": mail, "pwd": pwd})
            break

    testImapMail = ImapMail(mail, pwd)
    # msg = testImapMail.searchSender("daomaker")
    # print(msg.subject)
    subs = testImapMail.getAllMailSubject()
    print(subs)


