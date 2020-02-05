def get_my_stuff():
    return list(range(1, 5)) + list('hello') + [3.14]


def get_nums():
    return list(range(1, 100))


thats = {
        "Hanna" : "Hannah",
        "Geoffrey" : "Jeffrey",
        "aparna" : "Aparna",
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



def main():
    pass


if __name__ == "__main__":
    main()


