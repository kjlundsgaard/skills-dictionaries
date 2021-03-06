"""Skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different::

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    # add items of list into set
    # turn set back into list
    # return list

    duplicates = set()

    for word in words:

        duplicates.add(word)

    duplicates = list(duplicates)

    return duplicates


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """

    # put items 1 and 2 into sets
    # make list of intersection of sets
    # return list

    shared_items = list(set(items1) & set(items2))

    return shared_items


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    word_count = {}
    split_phrase = phrase.split()

    for word in split_phrase:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    pirate_speak = {"sir": "matey",
                    "hotel": "fleabag inn",
                    "student": "swabbie",
                    "man": "matey",
                    "professor": "foul blaggart",
                    "restaurant": "galley",
                    "your": "yer",
                    "excuse": "arr",
                    "students": "swabbies",
                    "are": "be",
                    "restroom": "head",
                    "my": "me",
                    "is": "be"}

    split_phrase = phrase.split()
    pirate_phrase = []

    for word in split_phrase:
        if word in pirate_speak:
            pirate_phrase.append(pirate_speak[word])
        else:
            pirate_phrase.append(word)

    return (' ').join(pirate_phrase)


def sort_by_word_length(words):
    """Given list of words, return list of ascending (len, [words]).

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- the length
    of the words for that word-length, and the list of words of
    that word length.

    For example::

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

        >>> sort_by_word_length(["hello", "katie", "test", "balloonicorn"])
        [(4, ['test']), (5, ['hello', 'katie']), (12, ['balloonicorn'])]
    """

    # create a dictionary with length as key and words as values of dict
    # create a list of sorted dictionary keys
    # go through sorted keys and reference dictionary to add lengths and words to new list

    word_length = {}

    # adds length as keys and corresponding words as values in dictionary
    for word in words:
        if len(word) in word_length:
            word_length[len(word)].append(word)
        else:
            word_length[len(word)] = [word]

    # gets and sorts dictionary keys
    keys = sorted(word_length.keys())
    # new list that returns keys and values as tuples
    words_by_length = [(key, word_length[key]) for key in keys]

    return words_by_length


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

    # two for loops
    # go through each possible addition and add the tuple pairs as keys in a dictionary with sum as values
    # go through the tuples in dictionary and check if the value is 0
    # add to list

    # struggling with finding a way to remove duplicates
    # am able to get a list of pairs that add to 0, but getting duplicates...

    sums = {}

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if (numbers[i] + numbers[j]) in sums:
                sums[numbers[i] + numbers[j]].append([numbers[i], numbers[j]])
            else:
                sums[numbers[i] + numbers[j]] = [[numbers[i], numbers[j]]]

    zeros = sums[0]
    unique_pairs = []

    for pair in zeros:
        if pair not in unique_pairs:
            unique_pairs.append(pair)

    return unique_pairs


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # use dictionaries
    # look up last index of word and search dictionary for first index of word
    # remove word from dictionary after it has been used?
    # push to list

    # initialize dictionary to store the first letters with list of words
    words_by_letter = {}
    # establish first word as first item in names list
    current_word = names[0]
    # start the phrase list that will store the words in order with first item as first word in names
    phrase = [current_word]
    # establish a lookup_letter that will change as current_word changes
    # it's the last letter of the word, so we can use this as a key in the dictionary to find the next word
    lookup_letter = current_word[-1]

    # create dictionary
    for name in names:
        if name[0] in words_by_letter:
            words_by_letter[name[0]].append(name)
        else:
            words_by_letter[name[0]] = [name]

    # cycling through the dictionary until a first letter has no corresponding words
    while words_by_letter[lookup_letter] != []:
        # store first value associated with the letter key as the next_word
        next_word = words_by_letter[lookup_letter][0]
        # add the next_word to the phrase list
        phrase.append(next_word)
        # delete the word we were using as current word from the dictionary
        del words_by_letter[current_word[0]][0]
        # re-bind current word to the next_word
        current_word = next_word
        # rebind look_up letter to last letter of current_word
        lookup_letter = current_word[-1]

    return phrase




#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
