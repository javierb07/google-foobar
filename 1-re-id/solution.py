def solution(i):
    def gen_primes(x):
        D = {}
        q = 2
        c = 0
        while True:
            if q not in D:
                yield q
                c += len(str(prime))
                D[q * q] = [q]
            else:
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]
            q += 1
            if (x+5) <= c :
                return 
    primes = ""
    for prime in gen_primes(i):
        primes += str(prime)
    return primes[i:i+5]

print(solution(10000))