command = input()
followers = {}

while command != "Log out":
    current_command = command.split(": ")
    action, username = current_command[0], current_command[1]
    if action == "New follower":
        if username not in followers:
            followers[username] = {}
            followers[username]['likes'] = 0
            followers[username]['comments'] = 0
    elif action == "Like":
        count = int(current_command[2])
        if username not in followers:
            followers[username] = {}
            followers[username]['likes'] = count
            followers[username]['comments'] = 0
        else:
            followers[username]['likes'] += count
    elif action == "Comment":
        if username not in followers:
            followers[username] = {}
            followers[username]['likes'] = 0
            followers[username]['comments'] = 1
        else:
            followers[username]['comments'] += 1
    elif action == "Blocked":
        if username in followers:
            del followers[username]
        else:
            print(f"{username} doesn't exist.")

    command = input()

print(f"{len(followers)} followers")
for username in followers:
    print(f"{username}: {followers[username]['likes']+followers[username]['comments']}")