from name_function import get_formatted_name


def test_first_last_name():
    """Do names like 'David Owens' work?"""
    formatted_name = get_formatted_name('david', 'owens')
    assert formatted_name == 'David Owens'


def test_first_last_middle_name():
    """Do names like 'David Gerald Owens' work?"""
    formatted_name = get_formatted_name('david', 'owens', 'gerald')
    assert formatted_name == 'David Gerald Owens'
