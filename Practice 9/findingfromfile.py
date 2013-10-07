import os
################This is my first try, but I believe it's a lot more simpler to do with lists? Nevertheless, here is a generalized example of this one.



def findfromfile(name, amount, file, tmp):
    found = False               #A flag to indicate if we have found what we are looking for
                                           #Lets specify the files we need for this operation, this could of course be user-inputted
    OldFile = open(file, 'r')
    NewFile = open(tmp, 'w')                                        #Lets specify the files we need for this operation
    CurrentCase = OldFile.readline() #This takes the string-part of the list
    while CurrentCase != '':    #Just checking if endline has been reached
        Amount = float(OldFile.readline()) #This one takes the float-part
        CurrentCase = CurrentCase.rstrip('\n') #Stripping the newline character
        if name == CurrentCase:
            NewFile.write(CurrentCase + '\n')
            NewFile.write(str(amount) + '\n')
            found = True
        else:
            NewFile.write(CurrentCase + '\n')
            NewFile.write(str(Amount) + '\n') #Need to typecast this into a string to make sure it goes with the newline argument
        CurrentCase = OldFile.readline()
    NewFile.close(),OldFile.close()
    os.remove(file)
    os.rename(tmp, file)
    if found:
        print("We found the instance and refreshed it according to your spesifications")
    else:
        print("The instance was not found")
findfromfile('saludo', 50, 'file.txt', 'tmp.txt')
