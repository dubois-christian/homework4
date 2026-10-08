
# Question 5: Unique Word Count
# Count how many distinct words are in the collection.
# Input: "one fish two fish red fish blue fish"
# Output: 5


def unique_word_count(words):
    if type(words) != str:
        return 0

    stuff = words.split()
    different = set()
    for word in stuff:
        different.add(word)
    return len(different)


# some tests
if __name__ == "__main__":
    print(unique_word_count("one fish two fish red fish blue fish"))
    print(unique_word_count(""))
    print(unique_word_count("dog dog dog"))
    print(unique_word_count("cat dog bird"))
    print(unique_word_count(None))
    print(unique_word_count("   hi    hi   bye  "))


# Reflection
# For my timed challenge I picked the unique word count question. I chose to use
# a set because we went over sets and I remembered that they don't allow
# duplicate values. The question was asking for the number of different words,
# not how many words there were total, so I thought it made sense to use one.
# I split the sentence into words first and then added them to the set. At the
# end I just returned the length of the set. This seemed easier than making a
# list and checking every word against all the other words in the list.
#
# The 30 minute time limit made me want to pick a question that I understood
# right away. I didn't want to spend most of the time trying to figure out a
# harder problem and then have nothing that worked. I also kept the code pretty
# basic instead of trying to make it shorter or use anything new. I tested a
# few things like repeated words, no words, and passing in None instead of a
# string. I made it return zero for something that isn't a string.
#
# One trade off is that my solution treats uppercase and lowercase words as
# different words. It also doesn't remove punctuation, so a word with a period
# could be counted separately from the same word without a period. I could fix
# those issues if there was more time, but the example didn't require that.
# Overall I think the set was a good choice for this problem because it made
# counting unique words simple without needing a lot of extra code.
