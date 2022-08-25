

#Task1


def concat():
#for i in range(2):
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    name = str(input("Put in a Game Name: "))
    name_leng = len(name)
    for word in name.split():
        if word[len(word)-1] in consonants:
            print(name + "inator" + " " + str(name_leng) + "000")
        else:
            print(name + "-inator" + " " + str(name_leng) + "000")
    name1 = str(input("Put in a Game Name: "))
    name_leng1 = len(name1)
    for word in name1.split():
        if word[len(word)-1] in consonants:
            print(name1 + "inator" + " " + str(name_leng1) + "000")
        else:
            print(name1 + "-inator" + " " + str(name_leng1) + "000")
    name2 = str(input("Put in a Game Name: "))
    name_leng2 = len(name2)
    for word in name2.split():
        if word[len(word)-1] in consonants:
            print(name2 + "inator" + " " + str(name_leng2) + "000")
        else:
            print(name2 + "-inator" + " " + str(name_leng2) + "000")
    
    # print(name + " " + str(name_leng) + "000")
    # print(name1 + " " + str(name_leng1) + "000")
    # print(name2 + " " + str(name_leng2) + "000")

concat()

# for word in a.split():
#     if word[0] in consonants and word[len(word)-1] in consonants:
#         all.append(word)

# print all