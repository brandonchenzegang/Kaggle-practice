doc_list=["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
keyword=["casino"]  #這邊可能回去要轉個符號


for n in range(len(doc_list)):
    sentence = doc_list[n].lower().strip(".").split()
    # print(sentence)
    for m in range(len(sentence)):
        word = sentence[m].split()
        # print(word)
        #如何印出找到的單字的號碼
