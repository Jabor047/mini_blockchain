from datetime import datetime
from hashlib import sha256

class block:

	def __init__(self,transactions,previous_hash,nonce=0):
		self.transactions = transactions
		self.previous_hash = previous_hash
		self.nonce = nonce
		self.datetime = datetime.now()
		self.hash = self.generate_hash()

	def generate_hash(self):
		block_contents = str(transactions)+str(previous_hash)+str(nonce)+str(datetime)
		block_hash = sha256(block_contents.encode())

		return block_hash.hexidigest()

	def print_content(self):
		print('timestamp:', self.timestamp)
		print('transactions:', self.transactions)
		print('current hash:' self.generate_hash())	


