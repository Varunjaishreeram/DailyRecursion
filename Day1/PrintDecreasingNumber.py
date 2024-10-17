# Given N print N to 1


def PrintDecreasing(n):
    if n==0:
        return

    print(n)
    PrintDecreasing(n-1)



PrintDecreasing(5)