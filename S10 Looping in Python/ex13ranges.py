def oddFromTenToTwentyInclusive():
    start = 10
    stop = 20
    return [x for x in range(start, stop + 1) if x % 2]


def sumOfList(l):
    r = 0
    for v in l:
        r += v
    return r


if __name__ == "__main__":
    print(sumOfList(oddFromTenToTwentyInclusive()))


