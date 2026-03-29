class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:

        def dfs(i, curr):
            if i == len(word):
                return curr.end
            if word[i] == ".":
                for ch in curr.children.values():
                    if dfs(i+1, ch):
                        return True
                return False
            else:
                if word[i] not in curr.children:
                    return False
                return dfs(i+1, curr.children[word[i]])
        return dfs(0, self.root)
        
