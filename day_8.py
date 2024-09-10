#write your code below this line
def prime_checker(number):
    num_divisor = 0
    for i in range(2, number+1):
        if number % i == 0:
            num_divisor = num_divisor + 1
    if num_divisor >= 2:
        message = print("This number is not a prime  number")
    else:
        message = print("This number is a prime number")
            
    return (message)

#write your code above this line

#Do NOT change any of the code below this line
n = int(input("Check this number: "))
prime_checker(number=n)