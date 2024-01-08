# m = {}
# print(type(m)) #check dictionary and not 

#student marks create a dictionary
marks = {"Naina": 45 , "Pankaj": 99 , "subham": 30 , "Suman": 80, "Ragni": 55, "Kajal": 100}
print(marks)
print( "Marks of ", marks["Pankaj"])
print( "Marks of ", marks["Naina"])
print( "Marks of ", marks["Kajal"])
print(marks.get("Payari")) # dictionary me not existing name (none output)
marks["sonam"] = 22 # add name dictionary
print(marks)

print(marks.values()) #number is a value
print(marks.keys()) # name is a key
print(marks.items()) 