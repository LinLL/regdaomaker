from mailutil.ImapMail import ImapMail
def getOneTestMailPwd():
    with open("data/mailspwd", 'r') as fr:
        for l in fr.readlines():
            mail, pwd = l.split("|")
            pwd = pwd.strip()
            mail = mail.strip()
            return mail, pwd
def test_checkStatus():
    mail, pwd = getOneTestMailPwd()
    testImapMail = ImapMail(mail, pwd)
    result = testImapMail.checkStatus()
    assert result == True