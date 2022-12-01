with open('advent_01.txt','r') as f:
	data = f.read().split('\n')

calories=0
tot_calories = []
for i in data:
	if i != "":
		calories += int(i)
	else:
		tot_calories.append(calories)
		calories = 0

tot_calories.sort()
print(sum(tot_calories[-3:]))
