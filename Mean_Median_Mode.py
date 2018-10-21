

def mean(list):

    sum=0
    for item in list:
        sum += item

    mean=sum/len(list)
    return mean


def median(list):
    sortedlist=sorted(list)
    print("Sorted list = \n", sortedlist)
    mid=int(len(list)/2)

    return list[mid]

def mode(list):
    sortedlist=sorted(list)
    modes = []
    currentStreak = 0
    highestStreak = 0
    uniqueNums = set(sortedlist)
    for i, num in enumerate(uniqueNums):
        currentStreak = sortedlist.count(num)
        if (currentStreak > highestStreak):
            highestStreak = currentStreak
            modes.clear()
            modes.append(num)
        elif (currentStreak == highestStreak):
            modes.append(num)

    print("Mode:")
    for mode in modes:
        print(mode, end=' ')
    print("")


num=int(input("How many  numbers you want to input in the list?\n"))

list=[]

for i in range(1,num+1):
    list.append(int(input("input number {} here".format(i))))
print("your list of number is ready ", list)

print("Mean =",mean(list))
print("Median =",median(list))
mode(list)