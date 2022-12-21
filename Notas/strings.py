# Strings are plain text and a basic type os data for python

print("Rolax\Academy")
print("Rolax\"Academy")
print("Rolax\nAcademy")

phrase= "The new shark Academy"
        #0123456789 
print(phrase + " is cool")
print(phrase.isupper()) #true or false answer
print(phrase.upper()) #convert the entire string to UPPPER CASE
print(phrase.upper().isupper()) #converts the entire string to UPPER CASE and returns a True/False answer
print(phrase.lower().isupper()) #converts the entire string to lower case and returns a True/False answer
print(len(phrase)) #returns the lenght of the string
print(phrase[12]) #returns a specific index of the container starting with "0"
print(phrase.index("T")) #number of index
print(phrase.index("shark")) #number of the first letter
print(phrase.replace("shark", "wolf")) #replace words or letters in the strings
print(phrase)
