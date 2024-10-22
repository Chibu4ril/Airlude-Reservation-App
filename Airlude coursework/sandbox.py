import random

count = 0
def customer_id():
    c_id_range = range(0, 3)
    customerId = []


    while count <= 4:
        for i in c_id_range:
            random_range = random.randrange(10)
            customerId.append(i + random_range)
        break
    return customerId

print(customer_id())


