import hashlib
import rsa
from user import *


def hash_func(str):
    return rsa.compute_hash(str.encode('utf-8'), 'SHA-512').hex()


if __name__ == '__main__':

    a = User("A")
    b = User("B")
    c = User("C")
    d = User("D")

    t1 = Transaction(a, b, 10)
    t2 = Transaction(a, c, 10)
    t3 = Transaction(b, d, 20)
    t4 = Transaction(a, b, 100)
    t5 = Transaction(b, a, 10)
    t6 = Transaction(c, d, 20)
    t7 = Transaction(c, a, 30)
    t8 = Transaction(d, b, 200)
    t9 = Transaction(b, c, 10)
    t10 = Transaction(a, d, 20)
    t11 = Transaction(d, a, 10)

    ledger = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11]

    bc = Blockchain()
    # bc.add_block(ledger, 4)
    bc.build(ledger, 4)
    print(a.get_balance())
    print(b.get_balance())

    ledger.append(Transaction(b, a, 20))
    ledger.append(Transaction(b, a, 20))
    ledger.append(Transaction(b, a, 20))
    bc.build(ledger, 4)

    bc.chain[1].print()
    bc.print()
