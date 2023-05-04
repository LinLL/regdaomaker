from imap_tools import MailBox, A, BaseMailBox

class ImapMail(object):
    def __int__(self, mailserver="pop-mail.outlook.com"):
        self.mailserver = mailserver

    def checkStatus(self, mail, pwd):
        try:
            with MailBox(self.mailserver).login(mail, pwd) as mailbox:
                print(mailbox.login_result)
                return True
        except:
            return False


if __name__ == '__main__':
    pass