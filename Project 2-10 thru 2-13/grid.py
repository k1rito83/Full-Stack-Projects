import tkinter as tk
   
root = tk.Tk()
 
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)






# root.geometry("400x300")
root.mainloop()