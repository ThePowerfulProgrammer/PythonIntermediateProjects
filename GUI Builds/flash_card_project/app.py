import pandas as pd
import tkinter as tk


try:
    dataframe = pd.read_csv("./data/Af_Eng_Top_100 - Sheet1.csv")
except FileNotFoundError:
    print("File not found, check current directory of operation")
    
    
print(dataframe['English'].sample(n=1).values)