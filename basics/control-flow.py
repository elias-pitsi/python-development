# words = ["shandu", "banana", "apple", "microsoft"]


# for word in words:
#     print(word, len(word))

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy: copy the dictionary, then iterate over the copy
for user, status in users.copy().items():
    print(f"{user} is {status}")

    if status == 'inactive':
        del users[user]

print("\nnew strategy\n")

# Strategy: Create a new collection of active users
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        print(f"{user} is {status}")