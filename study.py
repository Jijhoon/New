ss = "1. Something and 2. something else"
ln = [i for i in ss if i.isdigit()][-1] # i.isdigit() returns True if i is a digit
print(ln)

def filter(n):
    flter = [i for i in n if len(i) >= 5]
    return flter
test = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
print(filter(test))

#FizzBuzz
def generate_number():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
generate_number()

# GCF(greatest common factor) & LCM(least common multiple)
def gcf(n, m) -> int: # n과 m의 최대공약수를 구하는 함수.
    while m: # m이 0이 아닐 때까지 반복한다.
        n, m = m, n % m # n에 m을, m에 n % m을 대입한다.
    return print(n)
gcf(100, 84)

def get_lcm(a, b):
    # 두 수 중 큰 수를 구합니다.
    max_num = max(a, b)

    while True:
        # 큰 수부터 시작하여 공배수를 찾습니다.
        if max_num % a == 0 and max_num % b == 0:
            lcm = max_num
            break
        max_num += 1

    return lcm
print(get_lcm(3, 5))