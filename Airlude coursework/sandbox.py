import random

count = 0
def customer_id():
    c_id_range = range(0, 3)
    customerId = []


    while count <= 3:
        for i in c_id_range:
            random_range = random.randrange(5)
            customerId.append(i + random_range)
        break
    uniq = ''.join(str(item) for item in customerId )
    return uniq

print(customer_id())


