import random

# print(random.random())

# for i in range(10):
#     print(random.randint(15, 25))

# for i in range(10):
#     print(random.randrange(10, 50, 5))  # randrange(start, stop, step)

myList = ['Mati', 'Sami', 'Ashoq', 'Mehr', 'Shoaibo', 'Hashmat', 'Hezb']
for i in range(10):
    print(random.choice(myList))
