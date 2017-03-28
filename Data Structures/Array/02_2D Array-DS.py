import sys



arr = []
for arr_i in xrange(6):
    MINOR= raw_input('give a sequence of 6:')
    arr_temp = map(int, MINOR.strip().split(' '))
    arr.append(arr_temp)

print arr



hour_sum=[]

for i in range(4):
    for j in range(4):
        hour_sum.append(sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3]))


print max(hour_sum)
