'''
group_anagrams(words: list[str]) -> list[list[str]]

Example 1
Input:  words = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Example 2
Input:  words = [""]
Output: [[""]]

Example 3
Input:  words = ["a"]
Output: [["a"]]

'''

def group_anagrams(words: list[str]) -> list[list[str]]:
    group = {}
    for word in words:
        tmp_word = "".join(sorted(word))
        if tmp_word in group:
            group[tmp_word].append(word)
        else:
            group[tmp_word] = [word]

    return group.values()

from collections import defaultdict

def group_anagrams_default(words:list[str]):
    groups = defaultdict(list)
    for word in words:
        groups["".join(sorted(word))].append(word)
    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(words))
print(group_anagrams_default(words))