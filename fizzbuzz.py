# หาร3ลงตัว -> fizz , หาร5ลงตัว -> buzz ถ้าไม่ใช่ return ตัวเลข
# 3, 6, 9 -> fizz
# 5, 10, 20 -> buzz
# 15, 30, 45 -> fizzbuzz
# 1, 2, 4 -> number


def fizzbuzz(num):

    result = str(num)
    if num % 3 == 0:
        result = "fizz"
    if num % 5 == 0:
        result = "buzz"
    if num % 3 == 0 and num % 5 == 0:
        result = "fizzbuzz"

    return result


#     if num % 15 == 0:
#         return "fizzbuzz"
#     if num % 3 == 0:
#         return "fizz"
#     if num % 5 == 0:
#         return "buzz"
#     if num % 2 == 0:
#         return "bang"
#     return str(num)


# for i in range(10):
#     print(i, fizzbuzz(i))