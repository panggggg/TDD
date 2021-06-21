# หาร3ลงตัว -> fizz , หาร5ลงตัว -> buzz ถ้าไม่ใช่ return ตัวเลข
# 3, 6, 9 -> fizz
# 5, 10, 20 -> buzz
# 15, 30, 45 -> fizzbuzz
# 1, 2, 4 -> number


def fizzbuzz(num):

    result = get_result_buzz(num, str(num))
    if is_divide_by_three(num):
        result = "fizz"
        result += get_result_buzz(num, "")

    return result


def is_divide_by_three(num):
    return num % 3 == 0


def get_result_buzz(num, default):

    result = ["buzz", default, default, default, default]

    return result[num % 5]

    # result = [
    #     "buzz",
    #     default,
    #     default,
    #     default,
    #     default,
    # ]
    # return result[num % 5]


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
