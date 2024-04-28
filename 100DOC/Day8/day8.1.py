# Write your code below this line 👇
def prime_checker(number):
    is_prime = True

    for i in range(2,number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print('The number is prime')
    else:
        print('Number is not prime')

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input('Enter a two digit number'))  # Check this number
prime_checker(number=n)