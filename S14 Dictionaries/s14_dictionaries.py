
def createDict3():
    return {"a": None, "b": None, "c": None}


def fullName(artist):
    full_name = ' '.join([artist["first"], artist["last"]])
    return full_name


def totalDonations(donations):
    total_donations = sum(i for i in donations.values())
    return total_donations
