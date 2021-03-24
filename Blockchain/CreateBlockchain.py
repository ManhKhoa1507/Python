import hashlib
import json
import time

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        
        """
            Set the index, transactions, timestamp
            index: Block ID
            transactions: List of transactions (in BlockChain the data is transactions)
            time: time that create the block 
            previous_hash: include the previous hash block 
        """
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash

    def compute_hash(self):
        
        """
            Convert to json then hash the string
            return the hash string 
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        """
            Constructor of Block class
        """
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
            Create the first block and add to the blockchain
            This block have the ID = 0, previous_hash = 0
        """
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()

        #   Add the block to the blockchain 
        self.chain.append(genesis_block)

    @property
    
    def last_block(self):
        """
            Get the last block in the chain 
        """
        return self.chain[-1]
