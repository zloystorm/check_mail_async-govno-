import imap_tools.errors
from imap_tools import MailBox
from concurrent.futures import ThreadPoolExecutor

providers = {
    "imap.rambler.ru": [
        'rambler.ru',
        'lenta.ru',
        'autorambler.ru',
        'myrambler.ru',
        'ro.ru',
        'rambler.ua'],
    "imap.mail.ru": ['mail.ru', 'internet.ru', 'bk.ru', 'inbox.ru', 'list.ru'],
    "imap.gmail.com": 'gmail.com',
    "imap.yandex.ru": 'yandex.ru'
}
f = open('rez.txt', 'w')

def get_provider(mails: str):
    pr = mails.split("@")[-1]
    for key, value in providers.items():
        if pr in value:
            return key
    return f"imap.{pr}"

def check_mail(mail, psw):
            print(mail)
            print(psw)
            provider = get_provider(mail)
            try:
                with MailBox(provider).login(mail, psw) as mailbox:
                    for msg in mailbox.fetch():
                        msg_from.append(msg.from_)
            except:
                print('Скорее всего какие то пипы не включены\n')
                return 0

            with MailBox(provider).login(mail, psw, 'Spam') as mailboxs:
                for msgs in mailboxs.fetch():
                    msg_from.append(msgs.from_)

            f.write('==='+mail+'===' + '\n' + str(msg_from) + '\n')
            msg_from.clear()

threads = int(input('Threads: '))

if __name__ == '__main__':
    msg_from = []
    with open('emails.txt', encoding = 'utf-8') as file:
       emails = [row.strip().split(':') for row in file]
for i in emails:
    check_mail(i[0], i[1])

def huita():
    try:
        if __name__ == "__main__":
            while True:
                with ThreadPoolExecutor(max_workers=threads) as executor:
                    executor.map(check_mail())
    except:
        print("erorr")
        huita()


huita()
