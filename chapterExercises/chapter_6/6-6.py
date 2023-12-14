favorite_languages = {
    'david': 'python',
    'nicole': 'python',
    'robert': 'c',
    'dave': 'java',
    'robbie': 'rust',
}

people = [
    'david',
    'nicole',
    'robert',
    'quin',
    'robbie',
    'dave',
    'steve',
    'abbie',
    'shanna'
]

for x in favorite_languages.keys():
    print(f"Hi, {x.title()}.")

    if x in people:
        language = favorite_languages[x].title()
        print(f'{x.title()} thank you for taking the survey. Good to see that {language} is your favorite language\n')




