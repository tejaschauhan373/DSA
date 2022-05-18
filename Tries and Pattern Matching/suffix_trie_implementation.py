from trie import Trie


class SuffixTrie(Trie):

    def insert_suffix(self, word: str):
        """
        Time Complexity to insert = O(N*N) ; N = length of word
        """
        for i in range(len(word)):
            self.insert(word[i:])


obj = SuffixTrie()
input = "hello"
suffixes = ["lo", "ell", "hello"]
obj.insert_suffix(input)

for word in suffixes:
    if obj.search(word):
        print(word, "Found")
    else:
        print(word, "Not found")
