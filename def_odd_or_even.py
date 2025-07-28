def odd_or_even(number):
    """Determine if a number is ODD or EVEN"""

    if number % 2 == 0:
        return "EVEN"
    else:
        return "ODD"
    

print(odd_or_even(int(input("Enter a number: "))))