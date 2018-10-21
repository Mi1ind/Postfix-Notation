# prob = raw_input("Display the problem in postfix notation? ")
# print ("The problem you displayed is"), prob

prob = raw_input("Enter first 3 coordinates (example: 102 36 74): ")

tokens = prob.split() # returns a list (ArrayList) of tokenized values
coords = []     # initialise empty list
for tkn in tokens:
    try:
        coords.append(tkn)     # convert token to string
    except ValueError:       # if the entered number was of invalid int format
        print("Invalid integer format: {}".format(tkn))
        raise
print(coords)   # coords is now a list of integers that were entered


if coords[1].isdigit():
    print("IT'S A NUMBER")
else:
    print("NOT A number")
     
