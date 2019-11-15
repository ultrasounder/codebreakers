# from itertools import zip_longest

# def anagram_sort_and_compare(s1, s2):
#     for a, b in zip_longest(sorted(s1), sorted(s2)):
#         if a != b:
#             return False
#     return True

# anagram_sort_and_compare('abcde', 'debca')
# anagram_sort_and_compare('abcde', 'dbcca')

from collections import Counter

def anagram_with_counter(s1, s2):
    return Counter(s1) == Counter(s2)

print(anagram_with_counter('apple', 'pleap'))
print(anagram_with_counter('apple', 'applf'))