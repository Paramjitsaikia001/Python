''' 

# import random

from random import choice 

#coin=random.choice(["heads","tails"])

coin=choice(["heads","tails"])

print(coin)

'''

import random
import statistics

number = random.randint(1,10)
mean = statistics.mean([1,2,3,4,5,6,7,8,9,10])

print(f"mean of 1 to 10 : {mean:.2f}")
print(f"random number between 1 to 10 :{number}")