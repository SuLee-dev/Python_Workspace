import re

# 리트코드 125번

def isPalindrome(self, s: str) -> bool:

    s.lower()
    s = re.sub('[^a-z0-9]', ' ', s)

    return s == s[::-1]


# 리트코드 344번

def reverseString(self, s: List[str]) -> None:

    s.reverse()


# 리트코드 937번

def reorderLogFiles(self, logs: List[str]) -> List[str]:

    letters = []
    digits = []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))

    return letters + digits


# 리트코드 819번

def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
            if word not in banned]

    counts = collections.Counter(words)

    return counts.most_common(1)[0][0]


# 리트코드 49번

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())


# 리트코드 5번

def longestPalindrome(self, s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key = len)

    return result