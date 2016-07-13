import subprocess
import datetime

output = subprocess.check_output(['bash','-c', 'tail /home/apolysec/access-logs/apolyse.com'])
data = output.splitlines()
newdata = []
last = lastAccess()
if data[-1] == last: raise SystemExit()
writeLastAccess(data[-1])
new = False
for item in data:
    if new == True:
        newdata.append(item)
    if item == last:
        new = True

users = []
for item in newdata:
    if 'coffee.html' in item:
        users.append(item.split('-')[0][:-1])
with open('/home/apolysec/flickbean-logs/total-' + str(datetime.date.today()) + '.txt', 'a') as f:
    for item in users:
        f.write(item + '\n')
users = list(set(users))
with open('/home/apolysec/flickbean-logs/unique-' + str(datetime.date.today()) + '.txt', 'a') as f:
    for item in users:
        f.write(item + '\n')

def writeLastAccess(entry):
    with open('/home/apolysec/flickbean-logs/lastaccess.txt', 'w') as f:
        f.write(entry)

def lastAccess():
    with open('/home/apolysec/flickbean-logs/lastaccess.txt', 'r') as f:
        lastaccess = f.read()
    return lastlaccess
