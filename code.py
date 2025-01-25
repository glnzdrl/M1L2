import random
symbol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
result = symbol.split(',')
length = int(input("şifrenizin uzunluğu kaç karakter olacak?"))
password = ""
if length < 8:
    print("Şifren minimum 8 karakter uzunluğunda olmalı!")
else:
    for i in range(length):
        x = random.randint(0,71)
        password = password + symbol[x]
print(password)
