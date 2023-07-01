import csv
from operator import itemgetter, attrgetter

user_list = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']
user_highest_score_chart = []
users_in_tuples = []
user_line = {}

user_name = 'Player name'
user_score = 'Highest Score'
store = 'users_score.csv'
store_of_highest = 'users_highest_score.csv'


with open(f'{store}', mode='r') as file:
    reader = csv.DictReader(file)
    reader = list(reader)
    # for row in reader:
    #     print(row)
for user_line in reader:
    users_in_tuples.append(tuple(user_line.values()))

for index, user_line in enumerate(users_in_tuples):
    user_line = user_line[0], int(user_line[1])
    users_in_tuples[index] = user_line
    
user_highest_score_char = sorted(users_in_tuples, key=itemgetter(1), reverse=True)
sorted(user_highest_score_char, key=itemgetter(0))
# print(user_highest_score_char)

user_line = {}

counter = 0
for index, elem in enumerate(user_highest_score_char):
    if len(user_highest_score_chart) == len(user_list):
        break
    elif user_highest_score_char[index][0] != user_highest_score_char[index+1][0]:
        user_line[user_name] = user_highest_score_char[index - counter][0]
        user_line[user_score] = user_highest_score_char[index - counter][1]
        user_highest_score_chart.append(dict(user_line))
        counter = 0
    else:
        counter += 1


header = [user_name, user_score]
with open(f'{store_of_highest}', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=header, lineterminator='\r')
    writer.writeheader()
    writer.writerows(user_highest_score_chart)
 