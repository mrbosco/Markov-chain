import sys
import random

def load_text(filename):
    f = open(filename, 'r', encoding="utf-8")
    content = ""
    for lines in f:
        content += lines

    f.close()
    return content


def build_ngrams(text, order=20):
    words = text.split()
    ngrams = {}
    for i in range(0, len(words) - order):
        word = words[i]
        if word not in ngrams:
            ngrams[word] = []
        for j in range(1, order + 1):
            ngrams[word].append(words[i + j])

    print(ngrams)
    walking_markov(ngrams)


def walking_markov(ngr):
    """
    :param ngr: is a dictionary of ngrams
    :return:
    """
    print("-----------------------------")
    print("Walking!")
    print("-----------------------------")

    gram = ngr['the']
    result = ""
    for x in range(100):
        next_ngram = gram[random.randint(0, len(gram)-1)]
        result += " " + next_ngram

    print(result)


if __name__ == "__main__":
    loadedText = load_text(sys.argv[1])
    build_ngrams(loadedText)
