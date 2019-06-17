#Reads file.
fhand = open('large-data-1/follows.txt')

#Dictionary for data and list for sorting.
follows_dict = {}
sort_li = []

#Maps the data into a dictionary for keys and values.
for line in fhand:
    users = line.split()
    name = users[0]
    follows = users[1:]
    follows_dict[name] = len(follows)

#Places the dict data into a list for sorting.
for key, value in follows_dict.items():
    sort_li.append((value,key))

#Sorts the list in numerical order and reverses for highest number first.
sort_li = sorted(sort_li, reverse=True)

print(*sort_li[0])


########################################################################################################################
#The more social a user is, the more other users the user follows. Write a program that prints the user
#name of the most social user. In the case of a tie, print the user names of all the most social users, one
#per line, in lexicographic order.
