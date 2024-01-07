from survey import AnonymousSurvey

question = 'What langauge do you speak? '
language_survey = AnonymousSurvey(question)


language_survey.show_question()
print("Enter 'q' at any time to quit")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

language_survey.show_results()