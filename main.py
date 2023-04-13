# Main File Setting up the GUI

import tkinter as tk
from tkinter import filedialog

# Function to browse your json files


def getFile():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("JSON Files", "*.json* *.geojson*"), ("all files", "*.*")))
    # Show the name of the file selected
    file_name_label.configure(text="File Opened: "+filename)


# Set up the main window with a title and size and background color
m = tk.Tk()
m.title('GeoJSON Visualizer')
m.geometry('600x800')
m.config(background='white')

# selected file area
file_name_label = tk.Label(m, text='File Explorer',
                           width=100, height=4, fg='blue')


# exit button
button_exit = tk.Button(m, text='Exit', width=25, command=m.destroy)

# button to get a file
button_file = tk.Button(m, text='Choose File', width=30, command=getFile)

# canvas
view = tk.Canvas(m, width=40, height=60)

canvas_height = 20
canvas_width = 200

y = int(canvas_height/2)


# initalize all our widgets into the window
file_name_label.pack()
view.pack()
button_file.pack()
button_exit.pack()


# Main windo wait for events
m.mainloop()
