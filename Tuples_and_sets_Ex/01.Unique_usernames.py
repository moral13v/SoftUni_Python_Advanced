n = int(input())
unique_usernames = set()

for i in range(n):
    username = input()
    unique_usernames.add(username)

print("\n".join(unique_usernames))
