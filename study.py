free_book = False
customers = ["first", "second", "third", "fourth", "fifth"]
for i in customers:
    for y in customers:
        for z in customers:
            x = i + " " + y + " " + z # z가 먼저 for를 진행한 다음에 y를 진행, 다음에 i에 진행.
            print(x)
            # f(n): 알고리즘의 필요한 단계(시간 복잡도). 위 경우에는 1 + n * n * n * (1 + 1) = 1 + 2 * n**3
            # O(n): n**3 [위 알고리즘에서 가장 중요한 부분은 n**3이므로 그 외는 버린 값이다.]
