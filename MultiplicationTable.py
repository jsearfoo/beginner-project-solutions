def printMultiples(n, high):
    i = 1
    while i <= high:
        print (n*i, "\t")
        i = i + 1
    print()


def printMultTable(high):
    i = 1
    while i <= high:
        printMultiples(i, high)
        i = i + 1

multiples=int(input("Please input value for table "))

printMultTable(multiples)