'''
primes = next_prime()
[next(primes) for i in range(25)]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''


def next_prime():
    num = 1
    while True:
        num += 1
        isPrime = True
        for count in range(1, num + 1):
            if num % count == 0 and count != 1 and num != count:
                isPrime = False
                continue
        if isPrime:
            yield num


primes = next_prime()
print([next(primes) for i in range(25)])
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
