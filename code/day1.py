import pdb
import numpy as np

def main():

	sums = []
	with open("../data/day1.txt") as f:
		lines = f.readlines()
		
		sum = 0	
		for line in lines:	
			if not line.strip():
				sums.append(sum)
				sum = 0
			else:
				sum += int(line)
		max_num = max(sums)
		sums = np.array(sums)
		mask = np.array(sums == max_num)
		sums_idxs = np.nonzero(mask)[0] + 1
		print("The elf with the largest calorie meal is: ", sums_idxs, " He is carrying this many calories: ", max_num)

		########## Part 2:
		top = 3

		top_sum = 0
		for i in range(top):
			max_val = np.max(sums)
			top_sum += max_val
			
			mask = np.array(sums == max_val)
			sums_idxs = np.nonzero(mask)[0]
			sums = np.delete(sums, sums_idxs[0])

		print("The top three elves have this many calories: ", top_sum)

if __name__ == "__main__":
	main()
