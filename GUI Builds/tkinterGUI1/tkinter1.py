import tkinter as tk

window = tk.Tk() # Create a window
greeting = tk.Label(text="Hello Window", 
                    foreground="white",
                    background="#34A2FE",
                    width=10,
                    height=10,
                    border=5
                    ) # Add a simple widget, can style it as if were html

greeting.pack() # add the widget to the window

button = tk.Button(text="Click me PLZ", 
                   width=25,
                   height=25,
                   bg="Blue",
                   fg="Yellow")
button.pack()

window.mainloop()