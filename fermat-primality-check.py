# given an integer n, check whether it is prime number or not
# fermat's little theorem, for a prime integer p, an integer a which is not multiple of p, a ^ p mod p = a
# special case: if a is not divisible by p, a^(p-1) mod p = 1
# e.g. a = 2, p = 17, 2 ^ (17-1) mod 17 = 2 ^ 16 mod 17 = 1
# 
# if p is a prime number, for every a where 1 < a < p - 1,
# a ^ (p-1) mod p = 1 or a ^ (p-1) % p = 1

def fermat(n: int) -> bool:
    if n in [1, 4]: return False
    if n in [2, 3]: return True
    for a in range(2, n):
        if modular_power(a, n-1, n) != 1:
            return False
    return True


def modular_power(a, n, p):
    result = 1
    a = a % p
    while n > 0:
        if n % 2 == 0:
            a = (a ** 2) % p
            n = n // 2
        else:
            result = (result * a) % p
            n = n - 1
    return result

if __name__ == '__main__':
    integer_to_test = 18
    print(f"Primality check for {integer_to_test} is {fermat(integer_to_test)}")