release_year = "1991"
correct = False

while not correct:
    answer = input("What year was Python released? ")

    if answer == release_year:
        print("Congratulations! That is correct.")
        correct = True
    else:
        print("Sorry, that is incorrect. Please try again.")

print("Thank you for playing!")