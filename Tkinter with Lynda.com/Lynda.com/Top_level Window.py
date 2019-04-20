from tkinter import *
from tkinter import ttk
root = Tk()

window = Toplevel(root)
window.title('New Window')


window.lower() # set the windows stack
window.lift(root) # lift the window above the root window
window.state('zoomed') # zoom the window to its maximum allowed size
window.state('withdrawn') # hidden
window.state('iconic') # shrink to an icon in the task bar

window.state('normal')
print(window.state()) # check what the current window state

window.state('normal')



window.iconify()
window.deiconify()
# switch between iconified window or normal window programely


window.geometry('640x480+300+100') # width x height + x + y(location of screen)
# by default, a window is 200x200 pixels

window.resizable(False, True)
# whether or not the window is resized by the user, x direction and y direction

window.maxsize(640, 480)
window.minsize(200, 200)
window.resizable(True, True)
# set the window its resized min and max size


root.destroy()
# the destroy method is callable to all kinds of widgets to delete them
# when parent widget is destroyed, it will destroy the child widgets as well
