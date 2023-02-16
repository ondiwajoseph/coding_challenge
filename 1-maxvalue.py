'''Get the maximum value in the array given'''
def solution(A): 
    max_a = max(A)
    if max_a + 1 <= 0:
        return 1
    elif max_a + 1 >= 0 and (max_a - 1) not in A:
        return max_a - 1
    else:
        return (max_a + 1)

'''Test cases'''
A = [-2, -3]
print(solution(A))
B = [1, 2, 3, 4, 6]
print(solution(B))
C = [1, 2, 3, 4, 5, 6, 7]
print(solution(C))