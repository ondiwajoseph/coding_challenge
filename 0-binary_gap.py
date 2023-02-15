#!/user/bin/python3
"""
This funtion displays string of zeros in a binary number, Binary gap
"""
def solution(N):
    binaryN = bin(N)[2:]
    maxGap = 0
    minGap = 0
    for i in binaryN:
        if i == '1':
            if minGap > maxGap:
                maxGap = minGap
            minGap = 0
        else:
            minGap += 1
    return maxGap

'''An example'''
print("Binary gap of {}: ".format(529),solution(529))
print("Binary gap of {}: ".format(221),solution(221))
print("Binary gap of {}: ".format(80),solution(80))

