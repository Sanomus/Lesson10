import csv
import random
user_list = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']
game_score_range = (0, 1000)
games_quantity = 100
store = 'users_score.csv'
user_name = 'Player name'
user_score = 'Score'

user_score_chart = []
user_line = {}
# for user in user_list:
#     user_line[user_name] = user
#     user_score_chart.append(dict(user_line))
for i in range(games_quantity):
    for user in user_list:
        user_line[user_name] = user
        user_line[user_score] = random.randint(*game_score_range)
        user_score_chart.append(dict(user_line))



header = [user_name, user_score]
with open(f'{store}', 'w') as file:
    writer = csv.DictWriter(file, fieldnames = header, lineterminator='\r')
    writer.writeheader()
    writer.writerows(user_score_chart)