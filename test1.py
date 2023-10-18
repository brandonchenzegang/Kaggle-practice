def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    pass
#關鍵字字數要完全精準 ＝>判斷字串長度
#不區分大小寫 ＝>全部轉小寫
#不理會標點符號

# 1.句子先分割成單字 > 用空格分開，並去掉句號就好
# 2.list分割出來的單字，所有字母轉成小寫，包括要輸入的關鍵字
# 3.先用一個for迴圈，確認每一個單字
# 4.回傳是第幾個資料符合 

