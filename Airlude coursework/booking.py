first_name = input('Enter First Name: ')
last_name = input('Enter Last Name: ')
t_type1 = 'Economy'
t_type2 = 'Business Class'


def bookingDetails():
    userDetails = f'{first_name} {last_name}'
    return userDetails


print(bookingDetails())