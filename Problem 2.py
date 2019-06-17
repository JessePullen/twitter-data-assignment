#Reads file.
fhand = open('large-data-1/stream.txt')

print('enter n:')

#Dictionary for data, list for sorting, int for number of users.
n = int(input())
name_dict = {}
sort_li = []

#Counts all non-retweeted tweets.
for line in fhand:
    if ' RT ' not in line:
        users = line.split()
        name = users[0]
        name_dict[name] = name_dict.get(name, 0) + 1

#Stops program crashing if n is longer than the number of users.
if n > len(name_dict):
    n = len(name_dict)

#Places the dict data into a list for sorting.
for k,v in name_dict.items():
    sort_li.append((v,k))

#Sorts the list in numerical order and reverses for highest number first.
sort_li = sorted(sort_li, reverse=True)

for i in range(n):
    print(*sort_li[i])


########################################################################################################################
#Write a program that prints the usernames of the top n tweeters and how many tweets they authored. n
#is a number prompted for and entered by the user. The top tweeters authored the most original tweets
#(not retweets).
