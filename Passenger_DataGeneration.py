import random
from collections import Counter
import pandas as pd


def generate_data():
	"""Generate ID's, Number of Standard Bags, and Number of Bulky Bags"""
	
	# random passengers ID's
	starting_id = id_n
	n_passengers = n
	passengers_id = list(range(starting_id, starting_id+n_passengers))

	# stadard bags with the probabilities of std_prop
	std_bags = list(range(1,m-1)) + list(range(m, 21))
	std_prop = [p1] + len(list(range(m,21)))*[p2]

	# generating standard bags
	standard_bags = []
	for i in range(n):
		s = random.choices(std_bags, std_prop)[0]
		standard_bags.append(s)

	print("Frequency of Standard Bags: ")
	print(Counter(standard_bags))
	print()

	# bulky bags with the probabilities of blk_prop
	blk_bags = list(range(0,6))
	combinations = [[1,1,1,1,1], [1,2,1,1], [1,2,2], [2,3], [5]]
	gen_combination = random.choice(combinations)
	random.shuffle(gen_combination)

	indicies = random.sample(range(1, 1+n_passengers), len(gen_combination))

	# generating bulky bags
	bulky_bags = n_passengers * [0]

	for i, n in enumerate(indicies):
		bulky_bags[n] = gen_combination[i]


	print("Frequency of Bulky Bags: ")
	print(Counter(bulky_bags))
	print()

	# storing the generated data into a dataframe
	data = pd.DataFrame()
	data["PID"] = passengers_id
	data["NumberOfBag"] = standard_bags
	data["NumberOfBulky"] = bulky_bags

	print(data)

	# saving the data to .csv file
	data.to_csv("Passenger_data.csv", index=False)

if __name__ == '__main__':
	generate_data()