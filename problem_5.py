import hashlib
from time import gmtime, strftime


class Block:

	def __init__(self, index, data, previous_hash):
		self.index = index

		self.timestamp = gmtime()
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.calc_hash()
		
		self.next_block = None

	def calc_hash(self):
		sha = hashlib.sha256()
		block = str(self.timestamp) + str(self.data) + str(self.previous_hash)
		hash_str = block.encode('utf-8')
		sha.update(hash_str)
		return sha.hexdigest()

	def get_block_index(self):
		return self.index

	def get_timestamp(self):
		return strftime("%H:%M %d/%m/%Y", self.timestamp)

	def get_block_data(self):
		return self.data
 	
	def get_previous_hash(self):
		return self.previous_hash

	def get_block_hash(self):
		return self.hash

	def __repr__(self):
		idx = self.get_block_index()
		timestamp = self.get_timestamp()
		data = self.get_block_data()
		prev_hash = self.get_previous_hash()
		sha256_hash = self.get_block_hash()

		return "Block #{}:\nTimestamp: {}\nData: {}\nSHA256 Hash: {}\nPrev_Hash: {}\n".format(idx, timestamp, data, sha256_hash, prev_hash)

class Blockchain:

	def __init__(self):
		self.genesis_block = None
		self.last_block = None

	def add_block(self, data):
		if self.genesis_block is None:
			self.genesis_block = Block(index = 0, data = data, previous_hash = 0)
			self.last_block = self.genesis_block
		else:
			idx = self.last_block.get_block_index() + 1
			prev_hash = self.last_block.get_block_hash()
			new_block = Block(idx, data, prev_hash)

			self.last_block.next_block = new_block
			self.last_block = new_block

	def get_genesis_block(self):
		return self.genesis_block

	def get_block_contents(self, idx):
		block = self.get_genesis_block()

		while block and block.get_block_index() != idx:
			block = block.next_block
		
		return block

	def __repr__(self):
		output = ''
		block = self.genesis_block

		separator = ((("	" * 5) + "|" + "\n") * 3) + ((("	" * 5) + "v" + "\n"))
		while block != self.last_block:
			output += str(block) + separator
			block = block.next_block
		output += str(block)

		return output


b = Blockchain()
b.add_block('First')
b.add_block('Second')
b.add_block('Third')

print(b)

# Output:

# Block #0:
# Timestamp: 12:43 24/06/2020
# Data: First
# SHA256 Hash: e3c20f78684203a0164ed660053003fda1d666af83d0b8419326c9d6b2894779
# Prev_Hash: 0
#                                         |
#                                         |
#                                         |
#                                         v
# Block #1:
# Timestamp: 12:43 24/06/2020
# Data: Second
# SHA256 Hash: 753fb9fc424a12f80dd78d930b369bea901599e73fee5d5e2e9b234efce56ca3
# Prev_Hash: e3c20f78684203a0164ed660053003fda1d666af83d0b8419326c9d6b2894779
#                                         |
#                                         |
#                                         |
#                                         v
# Block #2:
# Timestamp: 12:43 24/06/2020
# Data: Third
# SHA256 Hash: fe13bf342e5a460d64322ca6132b2791e6d64775657dff12da45973be2caf928
# Prev_Hash: 753fb9fc424a12f80dd78d930b369bea901599e73fee5d5e2e9b234efce56ca3

''' Test Case 1: Block not present '''
print('Test 1:\n{}\n'.format(b.get_block_contents(4)))

# Expected Output: None

''' Test Case 2: Random block '''
print('Test 2:\n{}\n'.format(b.get_block_contents(2)))

# Expected Output: 
# Block #2:
# Timestamp: 13:29 24/06/2020
# Data: Third
# SHA256 Hash: c7f8f32d38d11a5e4a9e1225905415cfad36684aec8f899e0ba5c4f2abc2c506
# Prev_Hash: c084bfe223e5746216863b9dc7eb064544082b70907d189f380d4bd3f2e96d0a


''' Test Case 3: Genesis block '''
print('Test 3:\n{}\n'.format(b.get_block_contents(0)))

# Expected Output: 
# Block #0:
# Timestamp: 13:30 24/06/2020
# Data: First
# SHA256 Hash: ad1d5ab704935ef997c73566bad48e650cf31c96f48e69f868145e257f1bdee2
# Prev_Hash: 0