# หาร3ลงตัว -> fizz , หาร5ลงตัว -> buzz ถ้าไม่ใช่ return ตัวเลข
# 3, 6, 9
# 5, 10, 15
# 1, 2, 4


def fizzbuzz(num):

    if num % 15 == 0:
        return "fizzbuzz"
    if num % 3 == 0:
        return "fizz"
    if num % 5 == 0:
        return "buzz"
    if num % 2 == 0:
        return "bang"
    return str(num)


for i in range(10):
    print(i, fizzbuzz(i))