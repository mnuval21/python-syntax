def print_upper_words(words):
    """Print words in upper case.
    - words: list of strings
    For example:
        print_upper_words(["hello", "goodbye"])
    should print:
        HELLO
        GOODBYE
    """
    
    for word in words:
        print(word.upper())

print_upper_words(["hello", "goodbye"])



def print_upper_words_starting_with_h(words):
    """Print words that start with 'h'.   
    - words: list of strings
    For example:
        print_upper_words_starting_with_h(["hello", "goodbye"])
    should print:
        HELLO
    """

    # YOUR CODE HERE
    for word in words:
        if word.startswith("h") or word.startswith("H"):
            print(word.upper())

print_upper_words_starting_with_h(["hippo", "google", "happy", "jump"])




def print_upper_words_starting_with_h_or_g(words):
    """Print words that start with 'h' or 'g'.
    - words: list of strings
    For example:
        print_upper_words_starting_with_h_or_g(["hello", "goodbye"])
    should print:
        HELLO
        GOODBYE
    """
    # YOUR CODE HERE
    for word in words:
        if word.startswith("h") or word.startswith("H") or word.startswith("g") or word.startswith("G"):
            print(word.upper())

print_upper_words_starting_with_h_or_g(["hullabaloo", "gobble", "static"])