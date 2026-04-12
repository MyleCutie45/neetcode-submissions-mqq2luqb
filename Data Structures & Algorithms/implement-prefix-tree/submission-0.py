class TreeNode:
    def __init__(self):
        self.child = [None]*26
        self.end= False
class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            i = ord(c) - ord('a')
            if curr.child[i] == None:
                curr.child[i] = TreeNode()
            curr = curr.child[i]
        curr.end = True

    def search(self, word: str) -> bool:
        curr=self.root
        for c in word:
            i = ord(c) - ord('a')
            if curr.child[i] == None:
                return False
            curr=curr.child[i]
        return curr.end


    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if curr.child[i] == None:
                return False
            curr=curr.child[i]
        return True
        