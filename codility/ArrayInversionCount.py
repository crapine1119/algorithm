"""
time limit exceed for problem (60m)
정렬 후 index가 원래 index보다 클 경우, 더 큰 숫자라고 가정하고 문제를 해결하려함
그러나, 순차적으로 감소하는 배열에 대해서 처리하지 못함

merge sort라는 알고리즘으로 풀어야하는 문제 (내일 다시 확인)
"""


# def solution1(A: list[int]):
#     n = len(A)
#     if n == 1:
#         return -1
#
#     A_sort = sorted([(i, a) for i, a in zip(range(n), A)], key=lambda x: x[1])
#     count = 0
#     for enum, (i, _) in enumerate(A_sort):
#         if enum > i:
#             count += enum - i
#     if count == 0:
#         return -1
#     else:
#         return count

def solution(A: list[int]):
    pass



if __name__ == "__main__":
    A = [-1, 6, 3, 4, 7, 4]
    solution(A)