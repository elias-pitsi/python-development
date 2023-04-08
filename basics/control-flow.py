# words = ["shandu", "banana", "apple", "microsoft"]


# for word in words:
#     print(word, len(word))

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

for user, status in users.copy().items():
    print(f"{user} is {status}")