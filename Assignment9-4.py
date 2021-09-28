# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
email_address = dict()

for emails in handle:
    if not emails.startswith('From '):
        continue
    emails = emails.split()
    emails_values = emails[1]
    email_address[emails_values] = email_address.get(emails_values, 0) + 1

sender = None
times = None

for k, v in email_address.items():
    if times is None or v > times:
        sender = k
        times = v

print(sender, times)
