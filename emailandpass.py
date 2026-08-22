email = input('enter the email')
password = input('enter the pass')

if email =='siddharth@gmail.com' and password == '12345':
    print('welcome')

elif email =='siddharth@gmail.com' and password !='12345':
    password = input('enter password again')

    if password == '12345':
        print('welcome')

    else:
        print('sorry incorrect')

else:
    print('oops!! error occured')