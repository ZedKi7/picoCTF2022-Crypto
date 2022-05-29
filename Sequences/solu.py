import hashlib
from operator import xor
import sys

# Solved by Sage

ITERS = int(2e7)
VERIF_KEY = "96cc5f3b460732b442814fd33cf8537c"
ENCRYPTED_FLAG = bytes.fromhex("42cbbce1487b443de1acf4834baed794f4bbd0dfb5885e6c7ed9a3c62b")
 
def solu(n):
    a = 1419330 * 4913 * (17 ** (n-3))
    b = (-10828290) * 2197 * (13 ** (n-3))
    c = 9819200 * 1728 * (12 ** (n-3))
    d = 16120 * (-9261) * ((-21) ** (n-3))
    return (a + b + c + d) // 426360

def decrypt_flag(sol):
    sol = sol % (10**10000)
    sol = str(sol)
    sol_md5 = hashlib.md5(sol.encode()).hexdigest()
    print(sol_md5)

    if sol_md5 != VERIF_KEY:
        print("Incorrect solution")
        sys.exit(1)

    key = hashlib.sha256(sol.encode()).digest()
    flag = bytearray([xor(char,key[i]) for i, char in enumerate(ENCRYPTED_FLAG)]).decode()

    print(flag)


flagg = solu(ITERS)
decrypt_flag(flagg)