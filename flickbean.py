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

	def _rewrite_db():
		with open(self.db_path, 'w') as f:
			f.write(self.database)

	def delete(order):
		for item in self.database:
			if order in item:
				self.database.remove(item)
		_rewrite_db()

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