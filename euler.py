#!/usr/bin/python
"""Module for common Project Euler functions."""


import itertools
import math


##############################################################################

__author__ = "Jason A. Arter"
__date__ = "2017-04-04"
__copyright__ = "Copyright 2016, T-Mobile USA"
__credits__ = ["Jason A. Arter"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Jason A. Arter"
__email__ = "jason.arter@t-mobile.com"
__status__ = "Prototype"
__updated__ = "2018-06-07"

##############################################################################


def is_prime(n: int) -> bool:
    """Determine if a number is prime.

    Args:
        n (int): Number to be tested.

    Returns:
        True if n is prime. False otherwise.
    """
    # make sure n is x positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the square root of n
    # for all odd numbers
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def generate_primes(start: int = 1, end: int = 1000) -> int:
    """Return x list of primes between start and end"""
    n = 2
    count = 1
    while count <= end:
        if is_prime(n):
            if count >= start:
                yield n
            count += 1
        n += 1


def prime_list(start: int, end: int) -> list:
    """Return x list of primes between start and end"""
    primes = [x for x in range(start, end) if is_prime(x)]
    return primes


def prime_count(start: int = 2, end: int = 100) -> int:
    """count the number of primes between start and end."""
    return len(prime_list(start, end))


def list_factors(n: int, proper: bool = True) -> list:
    """Return x list of the proper factors of n."""
    factor_list = [x for x in range(1, (n // 2) + 1) if n % x == 0]
    if proper:
        factor_list.append(n)
    factor_list.sort()
    return factor_list


def big_factors(n: int) -> list:
    factor_list = [1, n]
    range_top = (n // 2) + 1
    x = 2
    while x < range_top:
        if n % x == 0:
            factor_list.append(x)
        x += 1
    factor_list.sort()
    return factor_list


def factorial(n: int) -> int:
    """Return the factorial of n (n!)."""
    product = 1
    for number in range(1, n + 1):
        product *= number
    return product


def cube_root(n: int) -> float:
    x = abs(n)
    root = (n ** (1 / 3.0))
    if int(round(root)) ** 3 == x:
        return int(round(root))
    else:
        return False


def fibonacci(limit: int) -> list:
    x = 1
    y = 1
    numbers = [1]
    while y <= limit:
        x += y
        x, y = y, x
        numbers.append(x)
    return numbers


def fibonacci_gen(limit: int) -> int:
    x: int = 1
    y: int = 1
    i: int = 0
    while i <= limit:
        i += 1
        x += y
        x, y = y, x
        yield i, x


# Triangular numbers #########################################################
def triangular_series(digits: int = 1) -> int:
    seq = []
    for x in range(1, 1000000):
        res = int((x * (x + 1)) / 2)
        if len(str(res)) < digits:
            continue
        elif len(str(res)) == digits:
            seq.append(res)
        else:
            return seq


# Square Numbers #############################################################
def square_series(digits=1):
    seq = []
    for x in range(1, 1000000):
        res = int(x**2)
        if len(str(res)) < digits:
            continue
        elif len(str(res)) == digits:
            seq.append(res)
        else:
            return seq


# Pentagonal Numbers #########################################################
def pentagonal_series(digits=1):
    seq = []
    for x in range(1, 1000000):
        res = int((x * ((3 * x) - 1)) / 2)
        if len(str(res)) < digits:
            continue
        elif len(str(res)) == digits:
            seq.append(res)
        else:
            return seq


# Hexagonal numbers ##########################################################
def hexagonal_series(digits=1):
    seq = []
    for x in range(1, 1000000):
        res = int(x * ((2 * x) - 1))
        if len(str(res)) < digits:
            continue
        elif len(str(res)) == digits:
            seq.append(res)
        else:
            return seq


# Heptagonal numbers #########################################################
def heptagonal_series(low=1, high=1):
    seq = []
    x = 1
    while x:
        res = int(((5 * (x * x)) - (3 * x)) / 2)
        if len(str(res)) < low:
            x += 1
        elif len(str(res)) > high:
            break
        else:
            seq.append(res)
            x += 1
    return seq


# Octagonal Numbers ##########################################################
def octagonal_series(low=1, high=4):
    seq = []
    x = 1
    while x:
        res = int(((3 * x) - 2) * x)
        if len(str(res)) < low:
            x += 1
        elif len(str(res)) > high:
            break
        else:
            seq.append(res)
            x += 1
    return seq


##############################################################################
def n_gonal_number(gonality, n):
    """Return x for P(gonality,n)=x."""
    if gonality == 3:
        return int((n * (n + 1)) / 2)
    elif gonality == 4:
        return int(n * n)
    elif gonality == 5:
        return (n * ((3 * n) - 1)) / 2
    elif gonality == 6:
        return n * ((2 * n) - 1)
    elif gonality == 7:
        return int(((5 * (n * n)) - (3 * n)) / 2)
    elif gonality == 8:
        return int(((3 * n) - 2) * n)
    else:
        return None


def n_gonal_root(gonality, n):
    """Return n for P(gonality,n)=x given gonality and x"""
    if gonality == 3:
        my_num = ((math.sqrt((8 * n) + 1)) / 2) - 0.5
        if my_num.is_integer():
            return int(my_num)
        else:
            return None
    elif gonality == 4:
        my_num = math.sqrt(n)
        if my_num.is_integer():
            return int(my_num)
        else:
            return None
    elif gonality == 5:
        my_num = (math.sqrt((24 * n) + 1) + 1) / 6
        if my_num.is_integer():
            return int(my_num)
        else:
            return None
    elif gonality == 6:
        my_num = (math.sqrt((8 * n) + 1) + 1) / 4
        if my_num.is_integer():
            return int(my_num)
        else:
            return None
    elif gonality == 7:
        my_num = ((math.sqrt(((40 * n) + 9))) + 3) / 10
        if my_num.is_integer():
            return int(my_num)
        else:
            return None
    elif gonality == 8:
        my_num = ((math.sqrt(((3 * n) + 1))) + 1) / 3
        if my_num.is_integer():
            return int(my_num)
        else:
            return None
    else:
        return None


##############################################################################
def perms(n, sort=True) -> set:
    if isinstance(n, list):
        temp_list = [str(x) for x in n]
        temp_x = ''.join(temp_list)
    elif isinstance(n, tuple):
        temp_list = [str(x) for x in n]
        temp_x = ''.join(temp_list)
    else:
        temp_x = str(n)
    my_perms = [''.join(x) for x in itertools.permutations(temp_x, len(temp_x))]
    if sort:
        my_perms.sort()
    perms_set = set(my_perms)
    return perms_set


def single_perm(x: str,y: str) -> bool:
    str_a = str(x)
    str_b = str(y)
    list_a = [str(x) for x in str_a]
    list_b = [str(x) for x in str_b]
    if len(list_a) != len(list_b):
        return False
    for item in list_a:
        try:
            list_b.remove(item)
        except:
            return False
    return True


def reverse(n):
    """Return the reverse of sequence n."""
    x = list(str(n))
    y = x[::-1]
    if isinstance(n, int):
        return int(''.join(y))
    else:
        return ''.join(y)


def is_pandigital(n: int) -> bool:
    """Return True if sequence n is pandigital."""
    store = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if isinstance(n, tuple):
        numbers = []
        for item in n:
            numbers.append(str(item))
    else:
        numbers = list(str(n))
    temp_store = store[:len(numbers)]
    for digit in numbers:
        try:
            temp_store.remove(digit)
        except ValueError:
            return False
    if len(temp_store) == 0:
        return True


def n_choose_r(n, r):
    """Classic "n Choose r" combinations."""
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


def bitify(seq: list) -> bin:
    total = 0
    for index, item in enumerate(seq):
        if item:
            total += 2**((len(seq) - index) - 1)
    return bin(total)
