import pytest
from main import *


def test_number_less_7():
    assert is_number_greater_7(5) == "Number less 7"


def test_number_equal_7():
    assert is_number_greater_7(7) == "Number less 7"


def test_number_greater_7():
    assert is_number_greater_7(9) == "Hello"


def test_is_john_success():
    assert is_john("John") == "Hello John"


def test_is_john_error():
    assert is_john("Mary") == "There is no such name"


def test_is_multiple_3_success_all():
    assert is_multiples_3([3, 9, 12, 6, 33, 27]) == 'Результат: [3, 9, 12, 6, 33, 27]'


def test_is_multiple_3_negative_all():
    assert is_multiples_3([4, 19, 22, 16, 32, 25]) == 'Результат: []'


def test_is_multiple_3_different_args():
    assert is_multiples_3([33, 19, 'i', 6, 27]) == 'Результат: [33, 6, 27]'

