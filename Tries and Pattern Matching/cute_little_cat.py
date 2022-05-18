from trie import Trie


def search_helper(t: Trie, document: str, i: int, m):
    temp = t.root
    for j in range(i, len(document)):
        ch = document[j]
        if ch not in temp.child:
            return
        temp = temp.child[ch]
        if temp.is_terminal:
            out = document[i:j + 1]
            m[out] = True

    return


def document_search(document: str, words: list):
    t = Trie()

    for word in words:
        t.insert(word)

    m = {}
    for i in range(len(document)):
        search_helper(t, document, i, m)

    for word in words:
        if word in m:
            print(word, "is present")
        else:
            print(word, "is not present")
    return


document = "little cute cat loves to code in c++, java & python"
words = ["cute cat", "ttle", "cat", "quick", "big"]

document_search(document, words)
