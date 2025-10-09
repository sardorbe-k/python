import threading

# 1. Tub sonni tekshiruvchi funksiya
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 2. Thread orqali tekshirish uchun funksiya
def check_primes_in_range(start, end, result_list):
    for num in range(start, end):
        if is_prime(num):
            result_list.append(num)

# 3. Asosiy dastur
def main():
    start_range = int(input("Boshlanish sonini kiriting: "))
    end_range = int(input("Tugash sonini kiriting: "))

    # Bo‘lish uchun thread soni
    thread_count = 4
    step = (end_range - start_range) // thread_count

    threads = []
    results = []

    # 4. Threadlarni yaratish
    for i in range(thread_count):
        start = start_range + i * step
        end = start_range + (i + 1) * step if i != thread_count - 1 else end_range + 1
        thread = threading.Thread(target=check_primes_in_range, args=(start, end, results))
        threads.append(thread)
        thread.start()

    # 5. Threadlarni tugaguncha kutish
    for thread in threads:
        thread.join()

    # 6. Natijani chiqarish
    results.sort()
    print(f"\nTub sonlar ({start_range} dan {end_range} gacha):")
    print(results)

if __name__ == "__main__":
    main()
