#병합정렬의 예시
def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    mid = n // 2 # n을 2로 나눈 몫을 mid에 저장
    g1 = merge_sort(a[:mid]) # 재귀호출을 이용하여 반으로 나눈 리스트를 다시 merge_sort에 넣어 정렬
    g2 = merge_sort(a[mid:]) # 재귀호출을 이용하여 반으로 나눈 리스트를 다시 merge_sort에 넣어 정렬
    result = []
    while g1 and g2: # 두 리스트에 요소가 남아있는 동안 반복
        if g1[0] < g2[0]:
            result.append(g1.pop(0)) # pop(0)은 리스트의 맨 앞 요소를 빼내는 함수 pop을 이용해서 빼낸 수를 append로 result에 추가
                                     # pop은 del과 다르게 삭제한 값을 반환하는 것을 이용!
        else:
            result.append(g2.pop(0))
    while g1:
        result.append(g1.pop(0)) # g1에 남아있는 요소를 result에 추가
    while g2:
        result.append(g2.pop(0))
    return result

show_me = merge_sort([1, 3, 5, 72, 9, 11, 13, 12, 123, 4141, 342, 11, 9, 7, 5, 3, 1])
print(show_me)
