fname=input("Enter name of the file")
no_of_words=0
no_of_lines=0
with open(fname ,'r') as f:
	for line in f:
		words = line.split()
		no_of_words += len(words)
		no_of_lines += 1   
print(" Number of words: " ,no_of_words)
print("Number of Lines: " ,no_of_lines)
