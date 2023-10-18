doc_list=["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
keyword=["casino"]

# print((doc_list[0].lower()).split()[4].strip("."))
#變小寫，分割，去掉逗號


# print(len((doc_list[0].lower()).split()))
#一個句子裡面看有幾個單字

# print(len(doc_list)-1)

for n in range(len(doc_list)):
    sentence = doc_list[n].lower().strip(".").split()
    # print(sentence)
    for m in range(len(sentence)):
        word = sentence[m].split()
        # print(word)
        print(word == keyword)
