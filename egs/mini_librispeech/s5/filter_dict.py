import os

ref = dict()
phones = dict()

with open("data/local/dict/lexicon.txt") as f:
    for line in f:
        line = line.strip()
        columns = line.split(" ", 1)
        word = columns[0]
        pron = columns[1]
        try:
            ref[word].append(pron)
        except:
            ref[word] = list()
            ref[word].append(pron)

#print ref

not_in_lex = open("data/local/dict/not_in_lexicon.txt", "a")

with open("data/dev_teamlab/words.txt") as f:
    for line in f:
        line = line.strip()
        if line in ref.keys():
            pass
        else:
            not_in_lex.write(line + "\n")
