#ALBARAA-BAATIYYAH_1845646_5J

size = int(input('Enter number of input : '))
arr = []

print('enter your values : ')
for _ in range(0,size):
    arr.append(int(input('')))

pos = 0
neg = 0

print("values : ",end='')
for t in range(0, len(arr)):
    print(arr[t],end=' ')

print('')
for i in range(0,size):
    num = arr[i]
    if (num < 0):
        neg = neg +1
    elif (num == 0):
        continue
    else:
        pos = pos +1

print('positive numbers are : ' + str(pos))
print('negative numbers are : ' + str(neg))