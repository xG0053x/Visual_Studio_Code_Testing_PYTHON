string = input("String to be converted: ")
n = int(input("Number of ending letters to convert: "))

first_half = string[:-n]
second_half = string[-n:]

print(first_half + second_half.upper())