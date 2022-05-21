def solution(n):
    # Convert the input to integer and return 0 if it's 1 or less
    n = int(n)
    if n <= 1:
        return 0
    operations = 0
    # Keep adding operations until the number of pellets is 1
    while n != 1:
        # If the number of pellets is even divide by 2 and add one operation 
        if (n % 2 == 0):
            n /= 2
            operations += 1
        else:
            # If number is 3 remove one pellet (special case)
            if n == 3:
                n -= 1
            # If number is odd and different to 3, convert the 
            # number + 1 and - 1 to binary. The number of zeroes in 
            # the binary representation will determine how many times
            # the number will be odd after it's divided by 2 (preferred operation) 
            else:
                binaryUp = bin(n + 1)
                binaryDown = bin(n - 1)
                upTrailingZeroes = 0
                downTrailingZeroes = 0
                indexUp = len(binaryUp) - 1
                indexDown = len(binaryDown) - 1
                # Determine if the number + 1 or number - 1 has more trailing zeroes
                while upTrailingZeroes == downTrailingZeroes:
                    if binaryUp[indexUp] == "0":
                        upTrailingZeroes += 1
                    if binaryDown[indexDown] == "0":
                        downTrailingZeroes += 1
                    indexUp -= 1
                    indexDown -= 1
                # Whichever number has more trailing zeroes will require less overall
                # operation in the algorithm
                if upTrailingZeroes > downTrailingZeroes:
                    n += 1
                else:
                    n -= 1
            operations += 1
    return operations
