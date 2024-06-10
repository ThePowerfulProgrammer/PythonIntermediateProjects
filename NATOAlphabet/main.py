NATOAlphabets = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima',
                'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']

NATOAlphabetsDict = {word[0]:word for word in NATOAlphabets}
print(NATOAlphabetsDict)

word = input("Enter a word: ").upper()

clearComms = [ w for c in word for w in NATOAlphabets for fc in range(1) if c == w[fc] ]

print(clearComms)
    