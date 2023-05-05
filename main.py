import time

from RegDaoMaker import RegDaoMaker
from mailutil.ImapMail import ImapMail

def run(mail, pwd, regpwd):
    testRegDaoMaker = RegDaoMaker()
    testRegDaoMaker.reg(mail, regpwd)

    myMail = ImapMail(mail, pwd)
    msg = myMail.searchSubject("Confirm your account")
    verify_url = myMail.parseRegMail(msg)
    testRegDaoMaker.verify(verify_url)



if __name__ == '__main__':
    run()