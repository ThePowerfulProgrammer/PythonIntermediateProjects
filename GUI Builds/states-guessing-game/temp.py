import pandas as pd


df = pd.read_csv('GUI Builds/states-guessing-game/50_states.csv')

lat_lon_df = df[['x', 'y']]

xCor = 319  
yCor = 164
a = [xCor, yCor]
print(lat_lon_df[(lat_lon_df.x>100) & (lat_lon_df.y > 100)]  )

print((lat_lon_df==a).all(1).any())
                                                                  
print(lat_lon_df[lat_lon_df.ge([xCor-5,yCor-5]) &  lat_lon_df.le([xCor+5,yCor+5])  ])
