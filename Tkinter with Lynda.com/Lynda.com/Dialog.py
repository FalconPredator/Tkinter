from tkinter import messagebox
messagebox.showinfo(title='A Friendly Message', message='Hello, Tkinter')

# Messagebox Types: Informational:
# showinfo()
# showwarning()
# showerror()





messagebox.askyesno(title='Hungry?', message='Do you want Ham?')

# Messagebox Types: Questions:
# askyesno()
# askokcancel()
# askretrycancel()
# askyesnocancel()
# askquestion()



from tkinter import filedialog
filename = filedialog.askopenfile()
print(filename.name)

# Filedialog Types: Just ask the user the dir or filename, not actually saving file
# askdirectory()
# asksaveasfile(mode)
# asksaveasfilename()

# askopenfile(mode)
# askopenfiles(mode)
# askopenfilename()
# askopenfilenames()

from tkinter import colorchooser
colorchooser.askcolor(initialcolor='#FFFFFF')
# return a tuple(RGB value, hex color)


