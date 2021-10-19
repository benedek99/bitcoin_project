import hashlib
import rsa
from user import *


def hash_func(str):
    return rsa.compute_hash(str.encode('utf-8'), 'SHA-512').hex()


if __name__ == '__main__':
    """
    string="pythonpool.com"
    encoded=string.encode()
    result = hashlib.sha512(encoded)
    print("String : ", end ="")
    print(string)
    print("Hash Value : ", end ="")
    print(result)
    print("Hexadecimal equivalent: ",result.hexdigest())
    print("Digest Size : ", end ="")
    print(result.digest_size)
    print("Block Size : ", end ="")
    print(result.block_size)

    pubkey, privkey = rsa.newkeys(1024)
    message = "xyz".encode('utf-8')

    hash = rsa.compute_hash(encoded, 'SHA-512')
    print(hash)
    print(hash_func(string))

    signature = rsa.sign(message, privkey, 'SHA-512')
    print(signature)
    signature = rsa.sign_hash(hash, privkey, 'SHA-512')
    print(signature)

    #b1 = Block()

    #print(mine_block(b1))

    a = User("A")
    b = User("B")

    t1 = Transaction(a, b, 10)

   # print(verify_transaction(t1,t1.sender))

    blockchain = [Block(0, 0, 0)]

    for i in range(0):
        print(mine_block(blockchain[i]))
 

    a = User("A")
    b = User("B")
    #c = User("C")
    #d = User("D")

    t1 = Transaction(a,b,10)
    print(t1.verify())

    t2 = Transaction(a,b,100)
    print(t1.verify())


    (pubkey, privkey) = rsa.newkeys(1024)
    message = 'Go left at the blue tree'.encode()
    hash = rsa.compute_hash(message, 'SHA-512')
    print(hash)
    signature = rsa.sign_hash(hash, privkey, 'SHA-512')
    print(signature)
    signature = rsa.sign(message, privkey, 'SHA-512')
    print(signature)

    message2 = 'Go left at the blue tree'.encode()
    print(rsa.verify(message2, signature, pubkey) == 'SHA-512')

    a = User("A")
    b = User("B")
    #c = User("C")
    #d = User("D")

    t1 = Transaction(a, b, 10)
    t2 = Transaction(a, b, 10)
    t3 = Transaction(a, b, 10)
    t4 = Transaction(a, b, 10)

    transactions = [t1,t2,t3,t4]
    print(transactions)
    print(build_merkle_tree(transactions, 4))
    print(transactions)
"""

    a = User("A")
    b = User("B")

    t1 = Transaction(a, b, 10)
    t2 = Transaction(a, b, 10)
    t3 = Transaction(a, b, 10)
    t4 = Transaction(a, b, 100)
    t5 = Transaction(a, b, 10)

    ledger = [t1, t2, t3, t4, t5, t1, t2, t3, t4, t5, t5, t5]

    bc = Blockchain()
    #bc.add_block(ledger, 4)
    bc.build(ledger, 4)
    print(a.get_balance())
    print(b.get_balance())

    ledger.append(t5)
    ledger.append(t5)
    bc.build(ledger, 4)
    bc.print()
    bc.chain[1].print()



