
def factorial(n): # 함수는 return을 만날 때 마다 반환값을 stack에 담는다.
    number = 1
    while n > 0:
        number *= n
        n -= 1
    return number
h = int(input("number: "))
print(factorial(h))

def reculsion(n):
    if n == 0:
        return 1
    return n * reculsion(n - 1)
print(reculsion(h)) # 내부 스택에 n * reculsion(n - 1)를 계속 담아두고 있는다.
"""
내부 스택의 상황은
n * reculsion(n - 1) # n = 3                n * reculsion(n - 1) # n = 3                n * reculsion(n - 1) # n = 3    
n * reculsion(n - 1) # n = 2        ->      n * reculsion(n - 1) # n = 2        ->      2                               
n * reculsion(n - 1) # n = 1                1
1

final = 6

선입후출을 보여준다. 먼저 stack에 쌓인 것이 나중에 처리되는 것을 알 수 있다.
"""

# def reculsion_number(n):
#     if n == 0:
#         return 1
#     return n, reculsion_number(n-1)
# print(reculsion_number(10))
"""

내부 스택
n, reculsion_number(n-1) # 10
n, reculsion_number(n-1) #9
:
n, reculsion_number(n-1) #2
n, reculsion_number(n-1) #1
1

(2(1,1)) -> 튜플 형식으로 나온다.

그렇다면 내부스택을 어떻게 만들어야 하는가?

n만 나오도록 해야한다. 
"""

def reculsion_number(n):
    if n == 0:
        return 1
    else:
        reculsion_number(n-1)
        return print(n)
reculsion_number(10) # 1 -> 10의 순서대로 나온다. 왜냐하면 10이 먼저 스택이 쌓였기 때문이다.

# 반대의 경우
def reculsion_number_reverse(n):
    if n == 11:
        return 1 # 11이 되기 전까지는 계속 스택에 쌓인다.
    else:
        reculsion_number_reverse(n + 1)
        return print(n)
reculsion_number_reverse(1)
# 10 -> 1의 순서대로 나온다. 왜냐하면 1이 먼저 스택이 쌓였기 때문이다.
