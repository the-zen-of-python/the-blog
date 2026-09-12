from array import array


fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])
print(fruits[-1])

fruits[1] = "blueberry"
print(fruits)

fruits.append("date")
print(fruits)
print(len(fruits))

numbers = array("i", [1, 2, 3, 4, 5])
print(numbers[0])
print(numbers[3])
numbers[2] = 99
print(numbers)