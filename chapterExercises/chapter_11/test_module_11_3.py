from module_11_3 import Employee


def test_give_default_raise():
    """Test the default raise function"""
    name = 'David'
    position = 'FinOps'
    pay = 110_000
    test_profile = Employee(name, position, pay)
    test_profile.give_raise()
    assert test_profile.details['pay'] == 115000


def test_give_custom_raise():
    """Test the default raise function"""
    name = 'David'
    position = 'FinOps'
    pay = 110_000
    test_profile = Employee(name, position, pay)
    test_profile.give_raise(10000)
    assert test_profile.details['pay'] == 120000
