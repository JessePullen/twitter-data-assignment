#Reads file.
fhand = open('large-data-1/stream.txt')

print('enter n:')

#Dictionary for data, list for sorting, int for number of users.
n = int(input())
name_dict = {}
sort_li = []

for line in fhand:
    if ' RT ' in line:
        users = line.split()
        twitter_name = users[2]
        position = twitter_name.find('@')
        name = twitter_name[position + 1:]
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
#Write a program that prints the usernames of the top n quotables and how many times in total their
#tweets were retweeted. n is a number prompted for and entered by the user. The top quotables are those
#users whose tweets were retweeted the most often. Format the output in the same manner as for task 2.