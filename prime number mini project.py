N = int(input("Please use a number greater than 2: "))
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
print(f"Prime numbers between 2 and {N}: ")
for num in range(2, N + 1):
    if is_prime(num):
        print(num)