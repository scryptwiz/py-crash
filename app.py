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
