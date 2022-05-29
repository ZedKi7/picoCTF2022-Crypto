# diffie-hellman

## What is Diffie-Hellman Key Exchange? (Definition)
The Diffie-Hellman key exchange is a mathematical protocol allowing 2 people (who may have never met) to agree on a secret number, without disclosing it during their exchanges (i.e. say that a person who could monitor the exchanges could not deduce the secret number).

## How does Diffie-Hellman Key Exchange work?
Two people Alice and Bob come into contact and choose 2 numbers, a prime number **P** and a number **G** (with P>G). This choice can be communicated in plain text and made public.

Alice chooses a number **a** at random, called the private key (kept secret), and performs the calculation **A = G^a mod P** whose value A is called Alice's public key, qu he sends to Bob publicly.

Similarly, Bob chooses a random number **b**, called the private key (alse kept secret), and performs the calculation **B = G^b mod P** whose value B is called the public key from Bob, which he sends to Alice publicly.

Alice received the value B and can then calculate the value **S = B^a mod P**
Similarly, Bob who received the value A can calculate the value **S = A^b mod P**

Thanks to math (and modular arithmetic), the **S** value is the same for Alice and Bob, it's their shared secret key. They can then communicate by encrypting their messages with this key.

The publicly exchanged values **(P, G, A and B)** do not allow to calculate **S** as long as the 2 private keys **a** and **b** remain hidden by their owner.

P = 13, G = 5, a = 7, b = 3
A = G^a mod P = 8
B = G^b mod P = 8
S = B^a mod P = S = A^b mod P = **5**

## Write-up

```python
import string

enc = 'H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_D9FF6IFD'
flag = ''
stringList = string.ascii_uppercase + string.digits

for i in enc:
    if i.isnumeric():
        flag += str((int(i)-5))
    elif i.isalpha():
        flag += stringList[(ord(i)-65-5) % 36]
    elif i == '_':
        flag += '_'

print(flag) # C4354R_C1PH3R_15_4_817_0U7D473D_84AA1DA8
```

## Flag

`picoCTF{C4354R_C1PH3R_15_4_817_0U7D473D_84AA1DA8}`
