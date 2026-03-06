"""Twitter module for managing tweets and hashtags."""


class Tweet:
    """Tweet class to represent a single tweet."""

    def __init__(self, user: str, content: str, time: float, retweets: int):
        """Initialize a new Tweet instance."""
        self.user = user
        self.content = content
        self.time = time
        self.retweets = retweets

    def __repr__(self):
        """Return a string representation of the tweet."""
        return f"{self.retweets, self.time, self.user}"


def find_fastest_growing(tweets: list) -> Tweet:
    """Find the fastest growing tweet based on retweets per time."""
    return max(tweets, key=lambda tweet: tweet.retweets / tweet.time)


def sort_by_popularity(tweets: list) -> list:
    """Sort tweets by popularity in descending order."""
    return sorted(tweets, key=lambda tweet: (-tweet.retweets, tweet.time))


def filter_by_hashtag(tweets: list, hashtag: str) -> list:
    """Filter tweets that contain a specific hashtag."""
    tweets_with_hash = filter(lambda tweet: hashtag in tweet.content, tweets)
    return list(tweets_with_hash)


def sort_hashtags_by_popularity(tweets: list) -> list:
    """Sort hashtags by popularity and then alphabetically."""
    counts = {}
    for tweet in tweets:
        words = tweet.content.split()
        seen = []
        for word in words:
            if word.startswith("#") and word not in seen:
                seen.append(word)
        for tag in seen:
            if tag not in counts:
                counts[tag] = 0
            counts[tag] += tweet.retweets
    return sorted(counts.keys(), key=lambda h: (-counts[h], h))


if __name__ == '__main__':
    tweet1 = Tweet("@realDonaldTrump", "Despite the negative press covfefe #bigsmart", 1249, 54303)
    tweet2 = Tweet("@elonmusk", "Technically, alcohol is a solution #bigsmart", 366.4, 166500)
    tweet3 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #heart", 2192, 284200)
    tweets = [tweet1, tweet2, tweet3]

    print(find_fastest_growing(tweets).user)
    filtered_by_popularity = sort_by_popularity(tweets)
    for t in filtered_by_popularity:
        print(t.user)
    filtered_by_hashtag = filter_by_hashtag(tweets, "#bigsmart")
    for t in filtered_by_hashtag:
        print(t.user)
    sorted_hashtags = sort_hashtags_by_popularity(tweets)
    print(sorted_hashtags[0])