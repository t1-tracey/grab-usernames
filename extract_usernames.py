import re
username_list = []

# Text is stored in forum_text.txt
with open('forumtext.txt') as text_file:
    for line in text_file:
        # Find all words in the line
        # that match the format of starting with @ and have 3+ characters (dodgy matching)
        matched_usernames = re.findall(r'@[\w|\.|-]{3,}', line)
        for match in matched_usernames:
             # Store name without @
            username_list.append(match[1:])

# Print out list of names to copy and paste
for username in username_list:
    print(username)
