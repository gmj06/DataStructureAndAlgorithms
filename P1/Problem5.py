import hashlib, datetime

class Block:

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.data)

    def calc_hash(self, data):
        """ Calculating SHA 256 encoding for the given data """
        sha = hashlib.sha256()
        hash_str = str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:
    def __init__(self, genesis_data):
        self.chain = []
        self.create_genesis_block(genesis_data)


    def create_genesis_block(self, data):
        """ Create first block of the chain """
        self.create_block(data, 0)

    def get_UTC_time(self):
        """ Get the current UTC time """
        return datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M %m/%d/%Y")

    def create_block(self, block_data, prev_hash):
        """ Add a block to the end of the chain """
        new_block = Block(
            index = len(self.chain),
            timestamp = self.get_UTC_time(),
            data = block_data,
            previous_hash = prev_hash
        )
        
        self.chain.append(new_block)
        return new_block

    def get_last_block(self):
        """ Get the last block in the chain """
        return self.chain[-1]

    def add_block(self, block):
        """ Add the given block to the Blockchain """
        previous_hash = self.get_last_block().hash

        if previous_hash != block.previous_hash:
            return

        self.chain.append(block)

    def size(self):
        """ Size of the Blockchain """
        return len(self.chain)

    def print_blockchain(self):
        """ Printing the Blockchain """
        for block in self.chain:
            print_string = f"index: {block.index} \n Timestamp: {block.timestamp} \n Data: {block.data} \n SHA256 Hash: {block.hash} \n Prev_Hash: {block.previous_hash}"
            print(print_string)
            print("<<<====") if block.index != self.size() - 1 else print("")
                            

blockchain = Blockchain("Genesis Block")
block1 = blockchain.create_block("Block #1", blockchain.get_last_block().hash)
blockchain.print_blockchain()

# As SHA 256 encoding is calculated based on all the properties of the Block, even if data is empty, it will not throw an error
blockchain1 = Blockchain("")
block11 = blockchain1.create_block("", blockchain1.get_last_block().hash)
blockchain1.print_blockchain()
    

    
        


