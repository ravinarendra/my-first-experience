number = int(input("Please input a number: "))

is_prime = True   # assume prime unless proven otherwise

if number < 2:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print("Number is PRIME")
else:
    print("Number is NOT PRIME")
