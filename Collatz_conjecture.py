# Collatz conjecture

def collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    return number

try:
    number = int(input('Give me your number: '))
    while number != 1:
        number = collatz(number)
        print(number)

except ValueError:
    print('Only integers allowed!')
