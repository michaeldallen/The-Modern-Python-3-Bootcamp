def thisForThat(l):

    rv = []

    for i in l:
        if i == "Hanna":
            rv.append("Hannah")
        elif i == "Geoffrey":
            rv.append("Jeffrey")
        elif i == "aparna":
            rv.append("Aparna")
        else:
            rv.append(i)
    return rv


def main():
    people = ["Hanna", "Louisa", "Claudia", "Angela", "Geoffrey", "aparna"]


if __name__ == "__main__":
    main()


