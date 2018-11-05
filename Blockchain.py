from Block import block

class blockchain:
	def __init__(self):
		self.chain = []
		self.transactions = []
		self.generate_block()

	def generate_block(self):
		transactions=[]
		previous_hash = 0
		block(transactions,previous_hash)
		self.chain.append(block)

		return self.chain

	def add_block(self,transactions):
		previous_block_hash = self.chain[len(self.chain)-1].hash
		new_block = block(transactions,previous_block_hash)
		new_block.generate_hash()
		proof = proof_of_work(new_block)
		self.chain.append(new_block)

		return new_block,self.chain

	def print_blocks(self):
		for i in range(len(self.chain)):
			current_block = self.chain[i]
			print('Block {} {}'.format(i, current_block))
			current_block.print_content()	

	def validate_block():
		for i in range(len(self.chain)):
			current_block = self.chain[i]
			previous_block = self.chain[i-1]

			if current_block.hash != current_block.generate_block():
				print("The current hash of the block does not equal the generated hash of the block.")
				return False

			if previous_block.hash != previous_block.generate_block():
				print("The previous block's hash does not equal the previous hash value stored in the current block.")
				return False

		return True

	def proof_of_work(self,block,difficulty=2):
		proof = block.generate_hash()

		while proof[:difficulty] != '0'*difficulty:
			block.nonce += 1
			proof = block.generate_hash() 
			
		block.nonce = 0
		return proof	

