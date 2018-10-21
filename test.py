# prob = raw_input("Display the problem in postfix notation? ")
# print ("The problem you displayed is"), prob

prob = raw_input("Display the problem in postfix notation (example: 102 36 74 65 + * /): ")
val = input("How many values did you input (include digits and symbols): ")
val1 = (val)/2

tokens = prob.split() # returns a list (ArrayList) of tokenized values
coords = []     # initialise empty list
for tkn in tokens:
    try:
        coords.append(tkn)     # convert token to string
    except ValueError:       # if the input was of invalid format
        print("Invalid format: {}".format(tkn))
        raise
print(coords)   # coords is now a list of integers that were entered

el = coords
i = 0
while i < val:
    if coords[i].isdigit():
        pass
    else:
        el[:i]
#        for val1 in coords[i]
#        print(coords[i])
    i += 1

#print(coords[0])
#print(coords[1])
#print(coords[2])
print(el)