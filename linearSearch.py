def search_linear(xs, target):
    for (i,v) in enumerate(xs):
        if v == target:
            return i
        else:
            return -1

def find_unknown_words(vocab, wds):
    result = []
    for w in wds:
        if(search_linear(vocab, w) < 0):
            result.append(w)
    return result
vocab = ["apple", "boy", "dog", "down",
                          "fell", "girl", "grass", "the", "tree"]
book_words = "the apple fell from the tree to the grass".split()
print(find_unknown_words(vocab, book_words))


def load_words_from_file(filename):
    """read words from filename, return a list of words/."""
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds

bigger_vocab = load_words_from_file("vocab.txt")
print("There are {0} words in the vocab, starting with \n {1}"
                .format(len(bigger_vocab), bigger_vocab[:6]))


def remove_adjacent_dups(xs):
    """return a new list in which all adjacent duplicates from XS have been removed."""

    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e
    return result

print(remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9]))
