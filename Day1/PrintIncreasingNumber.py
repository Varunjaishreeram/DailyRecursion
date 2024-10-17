# Given N print 1 to N


def PrintIncreasing(n):
    if n==0:
        return

    PrintIncreasing(n-1)
    print(n)



PrintIncreasing(5)