NATOAlphabets = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima',
                'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']

word = input("Enter a word: ").upper()

clearComms = [ w for c in word for w in NATOAlphabets for fc in range(1) if c == w[fc] ]

print(clearComms)
    