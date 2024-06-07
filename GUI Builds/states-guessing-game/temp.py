import pandas as pd


# Create df
df = pd.read_csv('GUI Builds/states-guessing-game/50_states.csv')

# Simulate user clicking a location
xCor = 319  
yCor = 164

# Find the lat,lon 
filtered = df[(df.x >= (xCor-5)) & (df.y >= (yCor-5))]

# Find the first row
first_match = df.loc[(df.x == filtered.x.values[0]) & (df.y == filtered.y.values[0]) ].iloc[0]

print(first_match)
print(first_match.state)
print(first_match.x)
print(first_match.y)


# turtle.goto(x=x, y=y)
# turtle.write(f"{state}")



print("\n"*10)
try:
    filtered_states = df[(df.state=='Alabama')].iloc[0]
    print(filtered_states)
except IndexError:
    print("Opp")
    
print(len(df.index))