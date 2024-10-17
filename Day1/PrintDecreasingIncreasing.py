# Given N, so first Print n to 1 and then 1 to n


def printDecreasingIncreasing(n):
    if n==0:
        return




    print(n)
    printDecreasingIncreasing(n-1)
    print(n)



printDecreasingIncreasing(5)