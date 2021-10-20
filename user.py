import datetime
import random
import rsa


def hash_func(str):
    return rsa.compute_hash(str, 'SHA-512')


class User:

    def __init__(self, name, balance=100):
        self.name = name
        self.balance = balance
        self.publicKey, self.privateKey = rsa.newkeys(2048)
        print("User %s created" % name)

    def sign_transaction(self, transaction):
        return rsa.sign(transaction.tr_hash, self.privateKey, 'SHA-512')

    def receive(self, amount):
        self.balance += amount

    def spend(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance


class Transaction(object):

    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timeStamp = datetime.datetime.now()
        self.receiver_key = receiver.publicKey
        self.tr_hash = hash_func((sender.name + receiver.name + str(amount) + str(self.timeStamp)).encode())
        self.signature = sender.sign_transaction(self)
        print("transaction: %s -> %s %d %s" %(self.sender.name, self.receiver.name, self.amount, self.tr_hash.hex()))

    def verify(self):
        if rsa.verify(self.tr_hash, self.signature, self.sender.publicKey) == "SHA-512":
            if self.sender.balance >= self.amount:
                self.sender.spend(self.amount)
                self.receiver.receive(self.amount)
                return "Transaction verified"
            else:
                return "Transaction failed: not enough coins"
        else:
            return "Transaction failed: signature not valid"


class Block(object):

    def __init__(self, blockID, topHash, lastBlock):
        self.blockID = blockID
        self.topHash = topHash
        self.lastBlock = lastBlock
        self.timeStamp = datetime.datetime.now()
        self.nonce = 3

    def print(self):
        print("\n********************************")
        print("blockID: " + self.blockID)
        print("topHash: " + self.topHash)
        print("lastBlock: " + self.lastBlock)
        print("timeStamp: " + str(self.timeStamp))
        print("nonce: " + str(self.nonce))
        print("********************************\n")


class Blockchain:

    chain = [Block("init_block", "34545653", "4564345")]

    def add_block(self, transactions, n):
        block = Block("124564563", "34545653", "4564345")
        block.topHash = build_merkle_tree(transactions, n)
        block.lastBlock = self.chain[-1].blockID
        block.timeStamp = datetime.datetime.now()
        block.blockID, block.nonce = mine_block(block)
        self.chain.append(block)
        print(" Block <%s> added to blockchain" % block.blockID)
        print(" nonce: " + str(block.nonce))

    def print(self):
        print("\nThe blockchain:")
        for i in range(len(self.chain)):
            print(" "*i + " -> " + self.chain[i].blockID)
        print()

    def build(self, ledger, n):
        while len(ledger) >= n:
            self.add_block(ledger, n)


def collect_transactions(transactions, n):
    valid = []
    print("\nCollecting transactions:")
    while len(valid) < n:
        if len(transactions) == 0:
            return valid
        msg = transactions[0].verify()
        if msg == "Transaction verified":
            valid.append(transactions[0])
        print("  " + msg)
        transactions.pop(0)
    return valid


def mine_block(block):

    print("Mining block")
    nonce = random.random()
    while not hash_func((block.topHash + block.lastBlock + str(block.timeStamp) + str(nonce)).encode()).hex().startswith("0000"):
        nonce = random.random()

    return hash_func((block.topHash + block.lastBlock + str(block.timeStamp) + str(nonce)).encode()).hex(), nonce


def build_merkle_tree(transactions_in, n):

    transactions = collect_transactions(transactions_in, n)

    for i in range(len(transactions)):
        transactions[i] = transactions[i].tr_hash.hex()

    print("Building Merkle tree")

    while len(transactions) > 1:
        i = 0
        while i < len(transactions)-1:
            transactions[i] = hash_func((transactions[i] + transactions[i+1]).encode()).hex()
            transactions.pop(i+1)
            i += 1

    print(" Top hash: " + transactions[0])
    return transactions[0]
