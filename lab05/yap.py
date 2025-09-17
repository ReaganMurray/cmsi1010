import random

words = {
    "noun": ["dog", "carrot", "chair", "toy", "rice cake", "cat"],
    "verb": ["ran", "barked", "squeaked", "flew", "fell", "whistled", "meowed"],
    "adjective": ["small", "great", "fuzzy", "funny", "light", "heavy"],
    "preposition": ["through", "over", "under", "beyond", "across", "besides"],
    "adverb": ["barely", "mostly", "easily", "already", "just", "simply"],
    "color": ["pink", "blue", "mauve", "red", "transparent", "orange"],
    "time": ["Yesterday", "Last week", "Last month", "Last year", "Last fortnight", "Last decade"]
}

template = """
    time the color noun
    verb preposition the coach’s
    adjective color noun that was
    adverb adjective before
    """


def random_sentence():
    sentence = []
    for token in template.split():
        if token in words:
            sentence.append(random.choice(words[token]))
        else:
            sentence.append(token)
    return " ".join(sentence) + "."


for _ in range(6):
    print(random_sentence())