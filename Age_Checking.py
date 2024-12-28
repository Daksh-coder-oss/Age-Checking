try:
    age=int(input("Please enter your age"))
    if age%2==0:
        print("Your number was even")
    else:
        print("It was odd")




except ValueError as e:
    print("An exception was occured",e)

