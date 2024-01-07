from module_11_3 import Employee
import pytest


@pytest.fixture
def test_employee():
    """Fixture employee"""
    name = 'David'
    position = 'FinOps'
    pay = 110_000
    test_profile = Employee(name, position, pay)
    return test_profile


def test_give_default_raise(test_employee):
    """Test the default raise function"""
    test_employee.give_raise()
    assert test_employee.details['pay'] == 115000


def test_give_custom_raise(test_employee):
    """Test the default raise function"""
    test_employee.give_raise(10000)
    assert test_employee.details['pay'] == 120000
