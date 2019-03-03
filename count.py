

def count_char(text):
    # TODO count the number of times each character occurs in the text
    # and print out each character along with its count

    dic = {}
    #for i in text:
    #    if i in dic:continue
    #    else:
    #         dic[i] = text.count(i) + '\n'

    #print(dic)
    for i in text:
        keys = dic.keys()
        if i in keys:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic:
        print(i, dic[i])
    pass

def count_char_insensitive(text):
    # TODO do the same as `count_char` but in a case-insensitive manner
    dic = {}
    for i in text:
        i = i.lower()
        keys = dic.keys()
        if i in keys:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic:
        print(i, dic[i])
    pass


def count_char_ordered(text):
    # TODO print the characters in the descending order of the count
    # HINT: lookup `sorted()` in the Python documentation

    # This task is quite difficult, so please feel free to make use of
    # resources online (Python docs, Stack Overflow, etc.)

    dic = {}
    for i in text:
        i = i.lower()
        keys = dic.keys()
        if i in keys:
            dic[i] += 1
        else:
            dic[i] = 1
    for key,value in sorted(dic.items(),key = lambda x : x[1],reverse = True):
        print(key,value)
    pass
