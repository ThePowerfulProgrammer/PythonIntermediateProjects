def getNameList(path):
    names = []
    with open(path, mode='r') as rFile:
        names = rFile.readlines() # A list of strings, each string correspond to a line in a txt file
    return names

names = getNameList("Names\invited_names.txt")

def writeInviteList(names):
    with open("Input\Letters\starting_letter.txt", mode='r') as rFile:
        lines = rFile.readlines()
        
        for name in names:
            name = name.strip()
            namePath = f'Output\ReadyToSend\{name}.txt'
            
            with open(namePath, mode='w') as wFile:
                for line in range(len(lines)):
                    if line == 0:
                        firstLine = lines[line].replace('[name]', f'{name}')  
                        wFile.write(f'{firstLine}')
                    else:
                        wFile.write(lines[line])
                        
writeInviteList(names)