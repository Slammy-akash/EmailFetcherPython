import imaplib
import email


# Connect to imap server

username = 'example@outlook.com'
password = 'yourPassword'
mail = imaplib.IMAP4_SSL('outlook.office365.com')
mail.login(username, password)

# retrieve a list of the mailboxes and select one
result, mailboxes = mail.list()
mail.select("inbox")

# retrieve a list of the UIDs for all of the messages in the select mailbox
result, numbers = mail.uid('search', None, 'ALL')
uids = numbers[0].decode().split()


# retrieve the headers (without setting the 'seen' flag) of the last 10 messages
# in the list of UIDs
result, messages = mail.uid('fetch', ','.join(uids[-10:]), '(BODY.PEEK[HEADER])')

# Convert the messages into email message object and print out the sender and
# the subject.
for _, message in messages[::2]:
    msg = email.message_from_bytes(message)
    print('{}: {}'.format(msg.get('from'), msg.get('subject')))
# At the end you will get from and subject on console
