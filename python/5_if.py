current_users = ['XmK', 'Xsh', 'yxR', 'zZW']
new_users = ['xMk', 'ZZl', 'YjK']

for new_user in new_users:
    flag = False
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            flag = True
    if flag:
        print("Hi, " + new_user.title() + '. Please input the password.')
    else:
        print("Hi, " + new_user.title() + '. You haven\'t registered now.')

nums = list(range(1, 10))
rank = []
for num in nums:
    if num == 1:
        rank.append('1st')
    elif num == 2:
        rank.append('2nd')
    elif num == 3:
        rank.append('3rd')
    else:
        rank.append(str(num) + 'th')
print(rank)