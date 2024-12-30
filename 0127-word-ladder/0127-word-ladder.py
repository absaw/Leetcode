class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        main trick is to figure out the neighbors of every word and adding it to the 
        adjList. the neighbors of a word are all the word which conform to the same pattern
        after replacing one of the characters with a star. Once that happens, you perform a bfs
        from the begin word until you find the end word. while traversing, a similar pattern to wordlist 
        process needs to be performed to find all the neighbors. Once that process is understood, the rest
        is similar to a normal level-based bfs where the path is increase by one after each level is 
        processed
        '''
        if endWord not in wordList:
            return 0
        adjList = collections.defaultdict(list)
        wordList.append(beginWord)
        # making the adjList based on the * pattern formed on replacing each word by a star at each location
        # eg. hot - *ot, h*t, ho*
        M = len(wordList[0])
        for word in wordList:
            #pattern
            for j in range(M):
                pattern = word[:j] + "*" + word[j+1:]
                adjList[pattern].append(word)
        
        visited = set(beginWord)
        queue = collections.deque()
        queue.append(beginWord)
        result = 1
        while queue:
            qLen = len(queue)
            for _ in range(qLen):
                word = queue.popleft()
                if word == endWord:
                    return result
                for j in range(M):
                    pattern = word[:j] + "*" + word[j+1:]
                    neighbors = adjList[pattern]

                    for neighbor in neighbors:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
            
            result += 1
        
        return 0


