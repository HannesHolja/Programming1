def stringtomorse(kirjainmerkitmorset,morsecodes):
        kirjainmerkit = {}
        i = 0
        for x in kirjainmerkitmorset:
                kirjainmerkit.update({x:morsecodes[i]})
                i+=1
        return kirjainmerkit
def morsetostring(kirjainmerkitmorset,morsecodes):
        morsemerkit = {}
        y = 0
        for z in morsecodes:
            morsemerkit.update({z:kirjainmerkitmorset[y]})
            y+=1
        return morsemerkit
def encrypt(name,kirjainmerkit):
    message = []
    for i in name:
        for x in kirjainmerkit:
            if i == x:
                message.append(kirjainmerkit[x])
                break
    return message
def decode(name,morsemerkit):
    name = name.rsplit(' ')
    message = []
    for i in name:
        for x in morsemerkit:
            if i == x:
                message.append(morsemerkit[x])
                break
    return message
