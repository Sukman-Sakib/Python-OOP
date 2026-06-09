import random

text = "absodyedk9123456780$#%^&*"
length = 16
password = "".join(random.choice(text) for _ in range(length))
print(password)