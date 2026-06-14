from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)  # userId -> [(timestamp, tweetId)]
        self.relations = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1 
        self.tweets[userId].append((self.time, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        # retrieve the 10 most recent tweet IDs 
        result = []
        heap = []
        user_list = []
        user_list.append(userId)

        relation_set = self.relations[userId]
        # add all users we need to deal with into one list
        for user in relation_set:
            if user != userId:
                user_list.append(user)
        
        # iterate through user list and add most recent tweet to heap
        for user in user_list:
            tweet_list = self.tweets[user]
            if tweet_list:
                timestamp, tweetId = tweet_list[-1][0], tweet_list[-1][1]
                index = len(tweet_list) - 1
                heapq.heappush(heap, (-timestamp, tweetId, user, index))
        # compare timestamps and add to result
        while len(heap) > 0 and len(result) < 10:
            new_timestamp, new_tweetId, new_user, index = heapq.heappop(heap)
            result.append(new_tweetId)
            if index -1 >= 0:
                next_timestamp, next_tweetId = self.tweets[new_user][index - 1]
                heapq.heappush(heap, (-next_timestamp, next_tweetId, new_user, index - 1))
        return result



        



    def follow(self, followerId: int, followeeId: int) -> None:
        self.relations[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.relations[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna