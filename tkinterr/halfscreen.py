import tkinter as tk

root = tk.Tk()
root1 = tk.Tk()

x = root.winfo_screenwidth() // 2
y = root.winfo_screenheight()
root.wm_geometry(f"{x}x{y}+0+0")
root1.wm_geometry(f"{x}x{y}-0+0")
root.mainloop()
