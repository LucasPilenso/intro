seqfqo = open("Python_06_uc.txt" , "w")
with open(" Python_06.txt", "r") as seqfh:
	for line in seqfh:
		line = line.rstrip().upper()
		seqfqo.write(f'{seqfh}\n')


