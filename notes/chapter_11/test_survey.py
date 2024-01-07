from survey import AnonymousSurvey


def test_single_store_response():
    """Test anonymous survey class"""
    question = "Test question"
    test_survey = AnonymousSurvey(question)
    test_survey.store_response('Test answer')
    assert 'Test answer' in test_survey.responses


def test_multiple_response():
    """Test anonymous survey class"""
    question = "Test question"
    test_survey = AnonymousSurvey(question)
    responses = ['test 1', 'test 2', 'test 3']
    for x in responses:
        test_survey.store_response(x)
    for x in responses:
        assert x in test_survey.responses

