def absodiff(inputArray):
	# declare an empty list to hold our results
	output = []
	for input in inputArray:
		# set the previous number to zero as given
		previous = 0
		# compute the absolute difference for each input
		diference = (input -(previous-1))
		currentOutput = abs(diference)
		# add absolute different to output list
		output.append(currentOutput)
		# set the current input number as the previous number before moving on
		previous = currentOutput
	# return the full output list
	return output

if __name__ == "__main__":
    input = [2, 4, 5, 6]
    print(absodiff(input))
