from random import randint,choice
i=0
code=0
for i in range(5):
 code=str(code)
 holder=choice([randint(48,57),randint(65,90),randint(97,122)])
 holder=chr(holder)
 code=code + holder
print(code)




