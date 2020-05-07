m = 100

nums = [i for i in range(1, m)]
lst = [None for i in range(1, m)]

for num in nums:
    for i in range(2, num-1):
        if num % i == 0:
            lst[num-1] = i
            break
        
for i, lcf in enumerate(lst):
    if lcf is not None:
        print(i+1, lcf)
        #print(lcf, end = ' ')
#print(lst)
#print(nums)
