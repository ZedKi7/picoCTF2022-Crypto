# basic-mod2

## Write-up

```python
from Crypto.Util.number import inverse
import string

enc = [268,413,110,190,426,419,108,229,310,379,323,373,385,236,92,96,169,321,284,185,154,137,186]
inverted_enc = [inverse(i, 41) for i in enc ]
uppercase = string.ascii_uppercase
flag = [] 

for i in inverted_enc:
    if i in range(1,27):
        flag.append(uppercase[i-1])
    elif i == 37:
        flag.append('_')
    elif i in range(26,37):
        flag.append(str(i-27))

print(''.join(flag)) # 1NV3R53LY_H4RD_C680BDC1
```

## Flag

`picoCTF{1NV3R53LY_H4RD_C680BDC1}`
