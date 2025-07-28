'''
git add .
git commit -m "."
git push
'''



my_rhyme = [1, 2]
my_rhyme.append("buckle my shoe")
print(my_rhyme)

my_rhyme.extend([3, 4, "buckle some more"])
print(my_rhyme)

#

test = []
test.extend("Hello there")
print(test)

#

saying = ["The Myth", "The Legend"]
saying.insert(0, "The Man")
print(saying)

#

my_oops = [1, 2, 3, 4, 4, 5]
print(my_oops)
my_oops.remove(4)
print(my_oops)

#

my_example = ["1st", 2, "2nd", "3rd", 3]
my_example.pop(1)
print(my_example)

my_example.pop()
print(my_example)

#

unwanted_list = ["a", "b", "c", "d", "e"]
print(unwanted_list)
unwanted_list.clear()
print(unwanted_list)

#

albert_says = ["Hey", "Hey", "Hey", "It's Fat Albert"]
print(albert_says.count("Hey"))

#

my_list = [1, 2, 3, 4, 5]
my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

#

my_list = ["A", "B", "C"]
my_list.copy()
print(my_list)

#

wild = ["Lion", "Zebra", "Panther", "Antelope"]
print(wild)
wild.append("Elephant")
print(wild)
animals= []
print(animals)
animals.extend(wild)
print(animals)
animals.insert(2, "Cheetah")
print(animals)
animals.pop(1)
print(animals)
animals.insert(1, "Giraffe")
print(animals)
animals.sort()
print(animals)

#

squares = [num**2 for num in range(1, 11) if num % 2 == 0]
print(squares)

#

vehicle = ("Toyota", "BMW", "Benz")
print(type(vehicle))

#

my_loves = ("Alma", "Mom", "Aurora", "Goose")
print(my_loves[2])

#

my_tuple = (2, 4, 6, 8, 10, 1, 3, 5, 7, 9, 0)
print(my_tuple[2:7])
print(my_tuple[::-2])


#

numbers = tuple(range(1, 11))
print("numbers: ", numbers)

even = numbers[1::2]
print("even: ", even)
odd = numbers[::2]
print("odd: ", odd)

#

t1 = (0, 0, 5, 0)
print(any(t1))

t2 = ("", "", "hello")
print(any(t2))

t3 = (False, False, False, True)
print(any(t3))

t4 = (0, "", [], {}, None, 3.14)
print(any(t4))