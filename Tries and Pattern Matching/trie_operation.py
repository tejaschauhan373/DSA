from trie import Trie

obj = Trie()

all_words = [
    "news",
    "new",
    "apple",
    "is",
    "computer"
]

for word in all_words:
    obj.insert(word)

for word in all_words:
    print(word, obj.search(word))

print("trie", obj.search("trie"))
print("app", obj.search("app"))
print("comp", obj.search("comp"))
print("news", obj.search("news"))
print("new", obj.search("new"))
