# Given number n, so find its factorial


def FindFactorial(n):
    if n==1:
        return 1



    return n*FindFactorial(n-1)



print(FindFactorial(5))