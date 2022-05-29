# diffie-hellman

**`Author:`** [Will Hong]
**`Points:`** [200]

## Description

> Alice and Bob wanted to exchange information secretly. 
> The two of them agreed to use the Diffie-Hellman key exchange algorithm, using p = 13 and g = 5. 
> They both chose numbers secretly where Alice chose 7 and Bob chose 3. 
> Then, Alice sent Bob some encoded text (with both letters and digits) using the generated key as the shift amount for a Caesar cipher over the alphabet and the decimal digits. 
> Can you figure out the contents of the message? Wrap your decrypted message in the picoCTF flag format like: picoCTF{decrypted_message}

**Download the message here** : [message.txt](./message.txt)

## Hints

**1** : Diffie-Hellman key exchange is a well known algorithm for generating keys, try looking up how the secret key is generated
**2** : For your Caesar shift amount, try forwards and backwards.

## Solution

Solution of the challenge can be found [here](solution/).
