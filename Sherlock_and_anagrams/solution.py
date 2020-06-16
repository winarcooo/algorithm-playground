import math

def sherlock_and_anagram(strings):

    string_length = len(strings)
    
    hashTable = {}
    for i in range(string_length):
        for j in range(i+1, string_length+1):
            key = ''.join(sorted(strings[i:j]))
            if key in hashTable:
                hashTable[key] += 1
            else:
                hashTable[key] = 1

    subsets = dict((k, v) for k, v in hashTable.items() if v > 1)

    if not subsets:
        return 0

    sum = 0;
    for subset in subsets:
        sum += int(nCr(subsets[subset], 2))

    return sum


def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

if __name__ == "__main__":

    testcase = [
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "bbcaadacaacbdddcdbddaddabcccdaaadcadcbddadababdaaabcccdcdaacadcababbabbdbacabbdcbbbbbddacdbbcdddbaaa",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "cacccbbcaaccbaacbbbcaaaababcacbbababbaacabccccaaaacbcababcbaaaaaacbacbccabcabbaaacabccbabccabbabcbba",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "bbcbacaabacacaaacbbcaabccacbaaaabbcaaaaaaaccaccabcacabbbbabbbbacaaccbabbccccaacccccabcabaacaabbcbaca",
        "cbaacdbaadbabbdbbaabddbdabbbccbdaccdbbdacdcabdbacbcadbbbbacbdabddcaccbbacbcadcdcabaabdbaacdccbbabbbc",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "babacaccaaabaaaaaaaccaaaccaaccabcbbbabccbbabababccaabcccacccaaabaccbccccbaacbcaacbcaaaaaaabacbcbbbcc",
        "bcbabbaccacbacaacbbaccbcbccbaaaabbbcaccaacaccbabcbabccacbaabbaaaabbbcbbbbbaababacacbcaabbcbcbcabbaba"
    ]

    result = sherlock_and_anagram("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print(result)

    # for test in testcase:
    #     result = sherlock_and_anagram(test)
    #     print(result)

# result    expected
# 166638    166650  wrong
# 4832      4832
# 166638    166650  wrong
# 13022     13022
# 166638    166650  wrong
# 9643      9644    wrong
# 6346      6346
# 166638    166650  wrong
# 8640      8640
# 11576     11577   wrong
