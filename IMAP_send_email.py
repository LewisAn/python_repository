from imaplib import IMAP4_SSL as issl
import email
from email.header import decode_header

client = issl("imap.qq.com")
client.login(user='913248383@qq.com', password='oqmeyrjjrwzsbcec')

# test = client.list()
# for i in test[1]:
#     print("----------", i)
client.select()

resp, data = client.search(None, "UNSEEN")

def parse_msg(msg):
    subject_info = msg.get("Subject")
    subject = decode_header(subject_info)[0][0]
    print("Subject:",subject)

    from_info = email.utils.parseaddr(msg.get("From"))
    if len(from_info) == 2:
        user = email.header.decode_header(from_info[0])[0][0]
        from_addr = user + "<" + from_info[1] + ">"
    else:
        from_addr = from_info

    print("From:", from_addr)

    date = msg.get("Date")
    print("Date:", date)

    for i in msg.walk():
        content_type = i.get_connect_type()

        if not i.is_multipart():
            if content_type == 'text/plain':
                content = i.get_payload(decode=True)
                print("\r\n", "content:", content)

for num in data[0].split():
    typ, data = client.fetch(int(num), "(RFC822)")
    msg = data[0][1]
    msg = email.message_from_string(msg)
    print("*" * 30, "\r\n")
    parse_msg(msg)

