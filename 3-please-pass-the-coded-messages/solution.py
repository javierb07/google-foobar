def solution(l):
    def remove_elements(a, b):
        found = False
        for index, number in enumerate(reversed(sortedNumbers)):
            if number % 3 == a:
                sortedNumbers.pop(len(sortedNumbers) - index - 1)
                found = True
                break          
        if not found:
            count = 0
            for index, number in enumerate(reversed(sortedNumbers)):
                if number % 3 == b and count != 2:
                    sortedNumbers.pop(len(sortedNumbers) - index - 1 + count)   
                    count += 1
                elif count == 2:
                    break
    
    sortedNumbers = sorted(l, reverse = True)

    while sortedNumbers:
        # Apply divisibility rule of 3
        sumNumbers = sum(sortedNumbers)
        remainder = sumNumbers % 3

        if remainder == 0:
            sortedNumbers = list(map(str, sortedNumbers))
            return int("".join(sortedNumbers))

        elif remainder == 1:
            # Need to remove one element with remainder equal to 1
            # or two elements whose remainders are equal to 2
            remove_elements(1, 2)
            
        else:
            # Remainder is 2, then:
            # Need to remove one element with remainder equal to 2
            # or two elements whose remainders are equal to 1 
            remove_elements(2, 1)

    return 0