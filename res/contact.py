import cgi

form=cgi.FieldStorage()
email=form.getvalue('email')
subject=form.getvalue('subject')
message=form.getvalue('message')

line=email+'|'+subject+'|'+message
with open('res/contacts.txt','a') as f:
    f.write(line)
