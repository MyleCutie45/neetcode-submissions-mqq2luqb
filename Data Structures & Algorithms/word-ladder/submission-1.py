class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordList:
            return 0
        beginSet = {beginWord}
        endSet = {endWord}
        steps = 1
        while beginSet:
            if len(beginSet) > len(endSet):
                beginSet,endSet = endSet,beginSet
            nextSet = set()
            for word in beginSet:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in endSet:
                            return steps + 1
                        if newWord in wordSet:
                            nextSet.add(newWord)
                            wordSet.remove(newWord)
            beginSet = nextSet
            steps+=1
        return 0
