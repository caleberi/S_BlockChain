from time import strftime,gmtime
from json import dumps
from hashlib import sha256
from transactions import Transactions
from chain import Chain


class BlockChain(object):
    def __init__(self):
        super().__init__()
        self.chain = Chain()
        self.transactions = Transactions()
        self.create_new_block(previous_hash=1,proof=100)

    def create_new_block(self,proof=0,previous_hash=0):
        """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        block_info = {
            "index":self.chain.length+1,
            "timestamp":strftime("%d-%m-%Y %H:%M:%S +0000", gmtime()),
            "transaction":self.transactions.transactions,
            "proof":proof,
            "previous_hash": previous_hash or self.hash(self.chain.tail)
        }

        self.transactions.reset()

        self.chain.append(block_info)

        return block_info

    def create_new_transaction(self,sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        self.transactions.append({
            "sender":sender,
            "recipient":recipient,
            "amount":amount
        })
        return self.chain.tail.data["index"]+1

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """
        print(block.data)
        block_string = dumps(block.data, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain.tail

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes,
           where p is the previous p'
         - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    
    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"



