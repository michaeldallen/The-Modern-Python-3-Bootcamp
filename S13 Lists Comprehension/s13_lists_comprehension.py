def bootstrap():
    return "bootstrap"


def firstLetter(l):
    return [i[0] for i in l]


def evens(l):
    return [i for i in l if not i % 2]


def intersection(l1, l2):
    return [i for i in l1 if i in l2]


def reversal(l):
    return [i.lower()[::-1] for i in l]


def divBy12(l):
    return [i for i in l if not i % 12]


def amaze(s):
    return [c for c in s if c not in "aeiou"]
