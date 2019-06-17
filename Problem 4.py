#Reads file.
follow_file = open('large-data-1/follows.txt')
stream_file = open('large-data-1/stream.txt')

print('enter n:')

#Dictionaries for data, list for sorting, int for number of users.
n = int(input())
seen_tweets = {}
sort_li = []
authored_tweets = {}
follows_dict = {}

#Find number of followed users.
for line in follow_file:
    users = line.split()
    name = users[0]
    follows = users[1:]
    follows_dict[name] = len(follows)

for line in stream_file:
    users = line.split()
#   Find if user mentioned in tweet/RT/DM.
    if '@' in line:
        for i in range(len(users)):
            twitter_name = users[i]
            position = twitter_name.find('@')
            if position != -1:
                name = twitter_name[position + 1:]
                seen_tweets[name] = seen_tweets.get(name, 0) + 1
#   Find if user authored retweet.
    if ' RT ' in line:
        name = users[0]
        seen_tweets[name] = seen_tweets.get(name, 0) + 1
#   Number of authored tweets.
    if line:
        name = users[0]
        authored_tweets[name] = authored_tweets.get(name, 0) + 1

#Checks if followed users are authors of tweets and places in seen_tweets.
for users, numbers in follows_dict.items():
    if users in authored_tweets:
        seen_tweets[name] = seen_tweets.get(name, 0) + 1

#Stops program crashing if n is longer than the number of users.
if n > len(seen_tweets):
    n = len(seen_tweets)

#Followed users into list for sorting.
for key, value in seen_tweets.items():
    sort_li.append((value,key))
sort_li = sorted(sort_li, reverse=True)

for i in range(n):
    print(*sort_li[i])


########################################################################################################################
#Write a program that prints the usernames of the top n users that would have seen the most tweets and
#how many tweets they would have seen. A user will see a tweet if it comes from a user they follow, or they
#are mentioned in the tweet, including as addressees in direct messages and as the authors of retweeted
#tweets. Format the output in the same manner as for task 2.

