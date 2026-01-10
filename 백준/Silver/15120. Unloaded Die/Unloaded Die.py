P = list(map(float, input().split()))
expected = 0

for index, possibility in enumerate(P):
    expected += (index+1) * possibility
    
if expected == 3.5: 
    print("{:.3f}".format(expected))
else:
    largest_possibility = max(P)
    difference = 3.5 - expected
    answer = abs(difference/largest_possibility)
    print("{:.3f}".format(answer))