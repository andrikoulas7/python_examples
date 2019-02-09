testFile = open("test.txt") #one parameter, the name of your file
testFile.read()#read your file

import os
os.rename("test.txt","test2.txt")#first parameter is the name of our file,second parameter is the new name
testFile.close()
fileName = input("Enter your file name: ")#prompt the user to give a new name
print(fileName)

testFile = open(fileName)
newFile = open("Copied_data.txt","w")#first parameter is the name of the new file, second parameter is only for write
newFile.write(testFile.read)#write to the new file whatever the content of the  other file
testFile.close()
newFile.close()#close both files so we can read them later

newFile = open("Copied_data.txt")
newFile.read()
