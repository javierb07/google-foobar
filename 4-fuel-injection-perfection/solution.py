def solution(n):
    n = int(n)
    if n <= 1:
        return 0
    operations = 0
    while n != 1:
        if (n % 2 == 0):
            n /= 2
            operations += 1
        else:
            if n == 3:
                n -= 1
            else:
                binaryUp = bin(n + 1)
                binaryDown = bin(n - 1)
                upTrailingZeroes = 0
                downTrailingZeroes = 0
                indexUp = len(binaryUp) - 1
                indexDown = len(binaryDown) - 1
                while upTrailingZeroes == downTrailingZeroes:
                    if binaryUp[indexUp] == "0":
                        upTrailingZeroes += 1
                    if binaryDown[indexDown] == "0":
                        downTrailingZeroes += 1
                    indexUp -= 1
                    indexDown -= 1
                if upTrailingZeroes > downTrailingZeroes:
                    n += 1
                else:
                    n -= 1
            operations += 1
    return operations
