print("*" * 10)
age = 20
eligibility = "Eligible" if age >= 18 else "Not eligible"
print(eligibility)


def original_age(age: int, by: int = 2) -> tuple:
    return (age, age + by)


print(original_age(20, 5))


def multiplyFunc(*args):
    total = 1
    for arg in args:
        total *= arg
    return total


def mulArgs(*args):
    return multiplyFunc(*args)


print(mulArgs(2, 3, 4, 5))


# Accept multiple arguments
def save_user(**user):
    print(user)


save_user(id=1, name="John", age=22)


def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(15))
print(fizz_buzz(7))


# List in ascending order
numbers = [3, 6, 2, 8, 4, 10]
print(numbers[::-1])


# unpacking list
numbers = [1, 2, 3, 20, 50]
first, second, *other, last = numbers
print(first)
print(second)
print(other)
print(last)

# using enumerate to get index and value in a list
letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(index, letter)

# using items to get key and value in a dictionary
letters_dict = {"name": "kelvin", "age": 22}
for key, value in letters_dict.items():
    print(key, value)

# Sort list
sort_nums = [3, 4, 5, 6, 2, 3, 4, 1, 9, 10]
# sort_nums.sort()
# print(sort_nums)
print(sorted(sort_nums, reverse=True))

items = [
    ("Product3", 12),
    ("Product1", 10),
    ("Product2", 9),
]

items.sort(key=lambda item: item[1])
print(items)

# map function
prices = list(map(lambda item: item[1], items))
print(prices)
x = map(lambda item: item[1] >= 10, items)
print(list(x))

# filter function
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

# list comprehension
# [expression for item in items]
new_prices = [item[1] for item in items]
print(new_prices)

# filter using list comprehension
# [expression for item in items if condition]
filtered_prices = [item for item in items if item[1] >= 10]
print(filtered_prices)


# zip function: Combime two or more lists
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip(list1, list2)))
