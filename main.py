user_name = input("Username :")
password = input("password :")

#length=replace(password,"*")



print('hi {0}, your password {1} is {2} letters long'.format(user_name,password.replace(password,"*" * len(password)),
len(password)))