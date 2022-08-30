
import os
import sys
import re

def teste():

    teste  = 'g5Bt5t54yvtz3v4A5wrGt537Bvr96v995r99v9z4Ar358xB2y59r9dBzA5t54yvtz3v4A57Bv9v9z4Ar3yB3z2uv9. Vy r99z3 7Bv r9 v96zxr9 9v3 x8r59 v8xBv3uv9uv4y59r3v4Av r trsvtr 6r8r 5 tvB, v47Br4A5 r9tyvzr9 r9 srzEr3 6r8r r Av88r, 9Br 3rv.cv54r8u5 Ur mz4tz.'



vowels = re.findall('[abcdefghijklmnopqrstuvwxyz]',teste)

print("occurrences of vowels:", vowels)



teste()