def get_my_stuff():
    return list(range(1, 5)) + list('hello') + [3.14]


def get_nums():
    return list(range(1, 100))


thats = {
    "Hanna": "Hannah",
    "Geoffrey": "Jeffrey",
    "aparna": "Aparna",
}


def thisForThat(l):
    for i in range(0, len(l)):
        if l[i] in thats:
            l[i] = thats[l[i]]
    return l


def mashUC(l):
    rv = ""
    for i in l:
        rv += i.upper()
    return rv


def embiggenList(l, i):
    l.append(i)
    return l


def listRemoveFirst(l):
    if len(l) > 0:
        l.pop(0)
        return l
    else:
        return None


def listRemoveLast(l):
    if len(l) > 0:
        l.pop()
        return l
    else:
        return None


def listAddLast(l, i):
    l.append(i)
    return l


def listAddFirst(l, i):
    l.insert(0, i)
    return l




