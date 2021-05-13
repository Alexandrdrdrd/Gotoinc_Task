def the_most_common_words(string):
    l = []
    words = string.lower().split()
    if len(words)<3:
        return l
    for j in range(3):
        word_count = {word: words.count(word) for word in set(words)}
        top = max(word_count, key=word_count.get)
        l.append(top)
        for i in words:
            if i == top:
                words.remove(i)
    if len(list(set(l))) < 3:
        return list()

    return l