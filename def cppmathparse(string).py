def cppmathparse(string):
	if ")/(" in string:
		print(string.index(")/("))
	string = "\\" + string
	

	for c in string:
		if (c == "("):
			index = string.index(c)
			string = string[:index] + "{" + string[index:]
		elif (c == ")"):
			index = string.index(c)
			string = string[:index+1] + "}" + string[index+1:]

    

	print(string)



cppmathparse("(hello/(((this)")
            
