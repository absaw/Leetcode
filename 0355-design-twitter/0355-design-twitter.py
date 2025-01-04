class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.postMap = defaultdict(list)        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.followMap[userId].add(userId)
        self.postMap[userId].append([self.count,tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []
        # user: [1,2,4], userId: [followerId]
        #get followers
        # self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            #for this follower, get the last value in their post list and add it to
            # max heap
            nPosts = len(self.postMap[followeeId])
            if nPosts > 0:
                index = nPosts-1
                count, tweetId = self.postMap[followeeId][index]
                maxHeap.append([count, tweetId, index, followeeId])
            
        #heapify max heap
        heapq.heapify(maxHeap)
        while maxHeap and len(res)<10:
            count, tweetId, index, followeeId = heapq.heappop(maxHeap)
            res.append(tweetId)
            # add the next element back to the heap
            index-=1
            if index>=0:
                count, tweetId = self.postMap[followeeId][index]
                heapq.heappush(maxHeap, [count,tweetId,index,followeeId])
        
        return res
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)