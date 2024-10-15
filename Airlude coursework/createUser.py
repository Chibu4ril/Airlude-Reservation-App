print('Hi there! Seems you are new here. Create an account to manage your bookings. ')
fname = input('First name: ')
lname = input('Last name: ')
email = input('Enter your email address: ')


def newUser(fname, lname):
    fullName = fname + ' ' + lname
    print(fullName)


newUser(fname, lname)



