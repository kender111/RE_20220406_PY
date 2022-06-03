import tkinter as tk

root = tk.Tk()
root1 = tk.Tk()
root2 = tk.Tk()
root3 = tk.Tk()
root4 = tk.Tk()

root.title("Йа перше платформочго")
root1.title("Йа друге платформочго")
root2.title("Йа третє платформочго")
root3.title("Йа четверте платформочго")
root4.title("Йа центр")

root.geometry("350x350+0+0") 
root1.geometry("350x350-0+0")
root2.geometry("350x350+0-0")
root3.geometry("350x350-0-0")

root4.update_idletasks()
w, h = root4.winfo_width(), root4.winfo_height()
root4.geometry(f"300x300+{(root4.winfo_screenwidth()-w)//2}+{(root4.winfo_screenheight()-h)//2}")

root.mainloop()
