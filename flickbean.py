import requests

class OrderDB(object):

	def __init__(self):
		'''Starts the Flick Bean database in memory.'''
		self.db_path = '/home/apolysec/flickbean-db/orders.bean'
		with open(self.db_path, 'r') as f:
			self.database = f.read().splitlines()
		self.total = len(self.database)

	def getOrder(index):
		return self.database[index]

	def add(order):
		self.database.append(order)
		with open(self.db_path, 'a') as f:
			f.write(order + '\n')
		return

	def _rewrite_db():
		with open(self.db_path, 'w') as f:
			f.write(self.database)
		return

	def delete(order):
		for item in self.database:
			if order in item:
				self.database.remove(item)
		_rewrite_db()
		return

	def get_last_order():
		return self.database[-2]

	def searchID(ID):
		for item in self.database:
			if item.split('|')[0] == ID:
				return item

	def edit(ID, order):
		for item in self.database:
			if item.split('|')[0] == ID:
				if item != order:
					item = order
					_rewrite_db()
				return
		return False

	def search(keyword):
		results = []
		for item in self.database:
			if keyword in item:
				results.append((self.database.index(item), item))
		return results


def alertTheGuys(msg):
    requests.post(
    "https://api.mailgun.net/v3/mg.apolyse.com/messages",
    auth=("api", "key-188fe0bda2f15695e08ea26a8c164e96"),
    data={"from": "notifier@flickbeanalerts.com",
          "to": '4087064249@vtext.com, 4083910180@vtext.com, 4087060872@vtext.com',
          "text": msg})

def parseOrder(order):
	text = ''
	order_starts = order[8::6]
	for o_index in order_starts:
		o = order[o_index:][:6]
		order_labels = ['Bean: ', + 'Roast Type: ', + 'Amount: ', + 'Grinded: ', + 'Packaging: ', + 'Additional Instructions: ']
		i = 0
		for line in o:
			text += text + order_labels[i] + line + '\n'
			i += 1
		text += text + '\n------------------------------\n\n'
	text += 'Total Price: ' + order[8]
	return text

def sendConfirmationEmail(recipient, order):
	requests.post(
    "https://api.mailgun.net/v3/mg.apolyse.com/messages",
    auth=("api", "key-188fe0bda2f15695e08ea26a8c164e96"),
    data={"from": "receipts@flickbeancoffee.com",
          "to": recipient,
          "subject": 'Your Order Receipt.'
          "text": '''Order ID: ''' + order[0] + '''

          Thank you for shopping at Flick Bean! Your custom roast will be underway soon. Here are the details of your order:

          ''' + parseOrder(order) + '''
          To modify your order, send a message to us at http://apolyse.com/contact.flick and include your order ID in the subject field.'''})