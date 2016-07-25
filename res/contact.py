import cgi, cgitb

form=cgi.FieldStorage()
email=form.getvalue('email')
subject=form.getvalue('subject')
message=form.getvalue('message')

print 'Content-type: text/html\r\n'

try:
	line=email+'|'+subject+'|'+message+'\n'
	with open('contacts.txt','a') as f:
	    f.write(line)
	print 'Your information has been submitted. <a href="../coffee.html">Click here</a> to return.'
except:
	print '<script>window.location = "../contact.html";'
