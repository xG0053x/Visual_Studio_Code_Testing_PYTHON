numList = list(range(1, 51))

for num in numList:
    if num % 3 == 0 and num % 5 == 0:
        print(num, "FizzBuzz")
    if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
        print(num, "FizzBuzzBoom")
    elif num % 2 == 0:
        print(num, "Boom")
    elif num % 3 == 0:
        print(num, "Fizz")
    elif num % 5 == 0:
        print(num, "Buzz")
    else:
        print(num, "No Fizz, Buzz, nor Boom")

print("Finished!")