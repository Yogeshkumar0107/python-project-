 function to create acronym
def fxn(string):
 # add first letter
 output =
string[0]
 
 # iterate over string
 for i in range(1, len(string)):
 if string[i-1] == '
':
 
 # add letter next to space
 output += string[i]
 
 # uppercase
output
 output = output.upper()
 return output
# input string
input1 = "Computer
Science Engineering"
# output acronym
print(fxn(input1))
# input string
input1 =
"geeks for geeks"
# output acronym
print(fxn(input1))
# input string
input1 =
" Rewari "
# output acronym
print(fxn(input1))
