import math
import sys

def input():
    return sys.stdin.readline()



def isPalin(temp):
    length = len(temp)
    if length % 2 == 0:
        for i in range(length//2):
            if(temp[i] != temp[length-i-1]):
                return False
        return True
    else:
        for i in range(length//2):
            if(temp[i] != temp[length-i-1]):
                return False 
        return True   

while(True):
    temp = input().strip()
    if(temp == '0'):
        break
    if(isPalin(temp)):
        print('yes')
    else:
        print('no')