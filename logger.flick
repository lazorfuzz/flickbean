#!/home/apolysec/dev/Python-2.7.8/python
import cgi, cgitb

print "Content-type:text/html\r\n\r\n"
form = cgi.FieldStorage()
username = form.getvalue('Username')
password = form.getvalue('Password')
updats = form.getvalue('email')
formtype = form.getvalue('type')

def register():
    f = open('database.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    for user in data:
        name = user.split('|')[0]
        if name == username:
            f = open('registration.html', 'r').read()
            f = f.replace('<!-- SHOWRESULT -->', '<p>You are already registered</p><br>')
            print f
            break
        else:
            f = open('database.txt', 'a')
            f.write(username + '|' + password + '\n')
            print f
            break
            
def login():
    f = open('database.txt', 'r')
    data = f.read()
    f.close()
    for user in data.split('\n'):
        name = user.split('|')[0]
        passw = user.split('|')[1]
        if name == username and passw == password:
            print '''<html><h2>You are in buddy!!!!!</h2><a href='apolyse.com/Leonflix.zip'>Get Leonflix</a></html>'''
            break

def updates():
    with open('updates.txt', 'a') as f:
        f.write(updats + '\n')
        

if formtype == 'login':
    login()
if formtype == 'updates':
    updates()
elif formtype == 'register':
    register()
    
        
    

