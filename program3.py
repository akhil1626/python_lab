file_name = input("Enter the file name:")
lines,words,characters = 0,0,0
with open(file_name,'r') as f:
	for i in f:
		lines+=1
		words+=len(i.split())
		characters += len(i.strip("\n"))
print("there are",lines,"lines")
print("there are ",words,"words")
print("there are ",characters,"characters")