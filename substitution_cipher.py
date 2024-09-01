'''
Here we have an input file, it has some text i need to convert this text in such a way so that it is not recognise by the third person for that i will be using substitution cipher.
'''
import string
# print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

dict = {}
data = ""
file = open("op_file.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1] # we can use -1/-2/+2/+1; any number
print(dict)

with open("text.txt") as f:
    while(True):
        # i need to read this file character by character and i need to substitute the particular character according to the dictionary

        c = f.read(1)
        # if we are reading the file character by character, we need to apply a boolean value here else it will not give required output

        if not c:
            print("End of file")
            break
        if c in dict:
            data = dict[c]
        else:
            data = c
        file.write(data)
        print(data)
file.close()
