class TrieNode:
    def __init__(self):
        # map character -> TrieNode
        # a dictionary to store child nodes: {char: TrieNode}
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            # If the character isn't already a child node, create a new node
            if char not in curr.children:
                curr.children[char] = TrieNode()
            # Move the pointer to the child node
            curr = curr.children[char]
        # After the loop, mark the last node as the end of the word
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        # return true only if the loop ends at a node marked end of word
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        # in this case we're just checking for prefix, so dont care if loop ends at a word marked end of word or not
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
