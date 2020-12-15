"""
link:https://app.codesignal.com/interview-practice/task/uX5iLwhc6L5ckSyNC/description

"""


def firstNotRepeatingCharacter(string):

    for letter in string:
        if string.count(letter) == 1:
            return letter
    return '_'


# or

def firstNotRepeatingCharacter2(s):
    res = "_"
    d = {}
    for i,c in enumerate(s):
        if c in d.keys():
            d[c] = -1
        else:
            d[c] = i
    min_key = len(s)+1
    for k in d.keys():
        if d[k]>=0:
            min_key = min(min_key,d[k])
            res = s[min_key]
    return res
