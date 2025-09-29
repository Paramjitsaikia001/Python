# random password generator

import random
import string

pass_len=8

CharValues=string.ascii_letters + string.digits +string.punctuation

# password = "".join([random.choice(CharValues) for i in range(pass_len)])
password=""
for i in range(pass_len):
    password+=random.choice(CharValues)

print("Your very strong password is:",password)