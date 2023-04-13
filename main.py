# Main File Setting up the GUI

import tkinter as tk

m = tk.Tk()

# close button
close = tk.Button(m, text='Close', width=25, command=m.destroy)

# canvas
view = tk.Canvas(m, width=40, height=60)
view.pack()
canvas_height = 20
canvas_width = 200

y = int(canvas_height/2)


close.pack()

m.mainloop()
