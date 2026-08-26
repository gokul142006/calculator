def check_number(num):
    
    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")

    if num < 2:
        print("The number is Not Prime")
    else:
        for i in range(2, num):
            if num % i == 0:
                print("The number is Not Prime")
                break
        else:
            print("The number is Prime")


number = int(input("Enter a number: "))

check_number(number)