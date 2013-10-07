def eraserhead(name, file):
    found = False   #Lets set the flag to false to indicate state of 'found'
    NewFile=open(file, 'r')
    instances = []
    instances = NewFile.readlines()
    NewFile.close()
    for i in instances:
        x = i.rstrip('\n')
        if x == name:
            index = instances.index(i)
            instances.pop(index)
            instances.pop(index)
            NewFile=open(file, 'w')
            for z in instances:
                NewFile.write(z)
            NewFile.close()
            print("{0} was erased from file".format(name))

eraserhead('coffee', 'file.txt')
