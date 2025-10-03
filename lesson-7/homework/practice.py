# 1. is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.
def is_prime(n: int) -> bool:
    if n <= 1:  
        return False
    if n == 2:   
        return True
    if n % 2 == 0:  
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


print(is_prime(4))  # False
print(is_prime(7))  # True
print(is_prime(1))  # False
print(is_prime(2))  # True
print(is_prime(19)) # True


# 2. digit_sum(k) funksiyasi
def digit_sum(k: int) -> int:
    s = 0
    for digit in str(k):   
        s += int(digit)
    return s

print(digit_sum(24))   
print(digit_sum(502))  
print(digit_sum(12345))

# 3. Ikki sonning darajalari
def powers_of_two(N: int):
    k = 1
    while 2 ** k <= N:
        print(2 ** k, end=" ")
        k += 1


powers_of_two(10) 
