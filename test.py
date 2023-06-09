import unittest

from main import count_vowels, factorial, get_average, is_prime


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120
        assert factorial(10) == 3628800


class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        assert is_prime(2) == True
        assert is_prime(7) == True
        assert is_prime(10) == False
        assert is_prime(31) == True
        assert is_prime(100) == False


class TestGetAverage(unittest.TestCase):
    def test_get_average(self):
        assert get_average([1, 2, 3, 4, 5]) == 3
        assert get_average([10, 20, 30, 40, 50]) == 30
        assert get_average([]) == 0
        assert get_average([5]) == 5


class TestCountVowels(unittest.TestCase):
    def test_count_vowels(self):
        assert count_vowels("Hello") == 2
        assert count_vowels("Python") == 1
        assert count_vowels("OpenAI") == 4
        assert count_vowels("Artificial Intelligence") == 9
        assert count_vowels("xyz") == 0
