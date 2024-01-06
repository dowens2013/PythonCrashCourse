from module_11_1 import city_country


def test_city_country():
    """Test city country"""
    full_city_country = city_country('raleigh', 'united states', 500_000)
    assert full_city_country == 'Raleigh, United States - 500000'

