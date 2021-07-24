import tkinter as tk
import numpy as np
# Modules required

root = tk.Tk()
# Making root command

canvas1 = tk.Canvas(root, width=400, height=300,  relief='raised')
canvas1.pack()
# Making and running the canvas

label1 = tk.Label(root, text='Calculate the Square Root')
# Creating label
label1.config(font=('helvetica', 14))
# Configuring label
canvas1.create_window(200, 25, window=label1)
# Creating window of label in canvas

ask_your_number = tk.Label(root, text='Type your Number:')
# Aonther text label
ask_your_number.config(font=('helvetica', 10))
# Configuring label
canvas1.create_window(200, 100, window=ask_your_number)
# Creating window of label in canvas

entry1 = tk.Entry(root) 
# Creating input box
canvas1.create_window(200, 140, window=entry1)
# Calling input boox in canvas

def getSquareRoot():
    inp_by_user = entry1.get()
    # Converting user entry data into inp_by_user 
    
    output = tk.Label(root, text='The Square Root of ' + inp_by_user + ' is:',font=('helvetica', 10))
    # Creating output label
    canvas1.create_window(200, 210, window=output)
    # Creating output window
    
    float_out = tk.Label(root, text= np.sqrt(inp_by_user),font=('helvetica', 10, 'bold'))
    # Creating output float
    canvas1.create_window(200, 230, window=float_out)
    # Creating output window on canvas
    
button_to_find_sqrt = tk.Button(text='Get the Square Root', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
# Creating button to find square root
canvas1.create_window(200, 180, window=button_to_find_sqrt)
# Calling the button

root.mainloop()
# Starting the program
# If root.mainloop() is not there program will not run
