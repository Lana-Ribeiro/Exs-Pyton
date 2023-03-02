def palavras(l):

    return {
        "len_array": len(l),
        "len_words": [
            len(words)
            for words in l
        ],
        "sorted_array": sorted(l)
    }