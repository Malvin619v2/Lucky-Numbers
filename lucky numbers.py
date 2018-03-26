import sys

data = raw_input()
nums = data.split()
num = nums[1]

res = 0

for i in range(1, int(num)+1):
    i = set(str(i))
    if "6" in i or "8" in i:
        res +=1
    if "68" in i or "86" in i:
        res = res

print res
