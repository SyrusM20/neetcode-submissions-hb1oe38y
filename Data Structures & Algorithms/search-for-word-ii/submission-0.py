class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()   # initialize our root
        for w in words:     # add words, so after we're all done, 
                            #we should have our entire trie set up
            root.addWord(w)
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] not in node.children or 
                (r,c) in visit):
                return 

            visit.add((r,c))        # say we start, now add the current visited node
            node = node.children[board[r][c]] # we set our node pointer (like tracing the trie with out finger?) -> to the current value from children, where we happend to have the board value, so we are looking at the baord value in the trie, and everything below it right?
            word += board[r][c]           # add our board value to word    
            if node.isWord:             # if we are at the end of a word, we can add it
                res.add(word)
            
            # do the above on the current cells neighbours
            dfs(r+1, c, node, word)     
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word) 
            dfs(r, c-1, node, word)
            visit.remove((r,c)) # remove our inital path after traversing it?
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, root, "")
        return list(res)


            


