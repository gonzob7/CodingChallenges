
"""Problem: Given a list of n numbers, determine if it contains any duplicate numbers.

Restate: We’re taking in a list of integers, and figuring out it there's any duplicates, if there is return True, otherwise return False.

Clarifying Questions: Are we returning a boolean or a list of numbers? Is the list always going to be relatively small? Or really big. Is it sorted?

Input: [1,2,3,4,5,6,1]
Output: False"""

#method that takes in array
#create a loop that loops through every element in the array
#start at first element, check every other element to see if theres any duplicates
#if there is, return True

def checkForDuplicates(array):
	for i in range(len(array)):
		for x in range(i+1, len(array)):
			if array[x] == array[i]: #theres a duplicate
				return True
	return False



def main():
    numbers = [1,3,4,6,7,8,3]
    print(checkForDuplicates(numbers))

    numbers2 = [1,3,4,6,7,8]
    print(checkForDuplicates(numbers2))

if __name__ == '__main__':
    main()
