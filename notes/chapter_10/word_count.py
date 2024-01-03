def count_words(path):
    """Count the approx number of words in a file"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"File '{path}' does not exist")
    else:
        # count number of words in file
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
