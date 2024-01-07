import pytest
from survey import AnonymousSurvey


@pytest.fixture
def test_survey():
    """A survey to test functionality"""
    question = "Test question"
    test_survey = AnonymousSurvey(question)
    return test_survey


def test_single_response(test_survey):
    """Test a single response"""
    test_survey.store_response('test answer')
    assert 'test answer' in test_survey.responses()


def test_multiple_responses(test_survey):
    """Test multiple responses"""
    responses = ['test 1', 'test 2', 'test 3']
    for x in responses:
        test_survey.store_response(x)

    for x in responses:
        assert x in test_survey.responses
