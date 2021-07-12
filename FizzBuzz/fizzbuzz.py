import random


def fizzbuzz(num):

    if (num / 15) - int(num / 15) == 0:
        return "fizzbuzz"
    if (num / 3) - int(num / 3) == 0:
        return "fizz"
    if (num / 5) - int(num / 5) == 0:
        return "buzz"
    return str(num)


def call_fizzbuzz():
    rand = int(random.random() * 100)
    return rand, fizzbuzz(rand)


# def random_number():
#     rand = int(random.random() * 100)
#     return rand, fizzbuzz(rand)


# print(random_number())