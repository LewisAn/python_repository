from poplib import POP3_SSL as pssl

client = pssl("pop.qq.com")
client.user("913248383@qq.com")
client.pass_("gcimhvyjknaxbccg")

all_num, all_sz = client.stat() # message count, mailbox size

print("There are {} messages in total".format(all_num))
print("There are {} bytes in total".format(all_sz))

print("Client list", client.list())

msg_2 = client.retr(2)

print("This is an email:")
for i in msg_2[1]:
    print("_______{}".format(i))

print("\r\n", client.quit())