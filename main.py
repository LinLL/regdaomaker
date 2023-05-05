import time

from RegDaoMaker import RegDaoMaker
from mailutil.ImapMail import ImapMail

def run():
    testRegDaoMaker = RegDaoMaker()
    testRegDaoMaker.reg("jeeanmoodiex@hotmail.com","q1w2e3R$")

    myMail = ImapMail("jeeanmoodiex@hotmail.com","AHFAGA32")
    msg = myMail.searchSender("daomaker")
    verify_url = myMail.parseRegMail(msg)
    testRegDaoMaker.driver.get(verify_url)


if __name__ == '__main__':
    run()