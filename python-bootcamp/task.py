import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.my_favorite_number)

random_number_0_1 = random.random()*10
print(random_number_0_1)

random_float = random.uniform(1,10)
print(random_float)

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_friend_number = random.randint(0,4)
print(friends[random_friend_number])

print(random.choice(friends))