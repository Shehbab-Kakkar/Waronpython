random = [10,11,23,34,56,67,89,36]
def searching(random):
     return random%2 != 0
#print([x for x in random if searching(x)])
list = []
for x in random:
    if searching(x):
        list.append(x)
print(list)
