def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count
