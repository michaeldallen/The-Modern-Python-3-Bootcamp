def abbreviations_for(list1, list2):
    assert len(list1) == len(list2)
    answer = { list1[i]:list2[i] for i in range(len(list1)) }
    return answer


def list_to_dict(person):
    answer = { key:value for key,value in person }
    return answer


def vowels():
    answer = { k:0 for k in "aeiou" }
    return answer

def ascii():
    answer = { i:chr(i) for i in range(65, 91) }
    return answer
