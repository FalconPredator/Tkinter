from tkinter import *
from tkinter import ttk

root = Tk()



def key_press(event):
    print('types:{}'.format(event.type))
    print('widgets:{}'.format(event.widget))
    print('char:{}'.format(event.char))
    print('keysym:{}'.format(event.keysym))
    print('keycode:{}'.format(event.keycode))

def shortcut(action):
    print(action)
    
##root.bind('<KeyPress>', key_press)

root.bind('<Control-c>', lambda e: shortcut('Copy'))
root.bind('<Control-v>', lambda e: shortcut('Paste'))

root.mainloop()

# Note: unlike callbacks command when creating widgets, binding is passing the event object










# Tk Event Types:
# ButtonPress, ButtonRelease, Enter, Leave, Motion
# KeyPress, KeyRelease, FocusIn, FocusOut
# reference material: binding command


'''
>>> types:2  the type of event
widgets:.    top level window '.'
char:a       the charactor from the keyboard
keysym:a     
keycode:65   65 is the keycode for the 'a' key
'''
# Note: F1 does not have char

'''
Event Format        Event Description
<Key>, <KeyPress>   User pressed any key
<KeyPress-Delete>   User pressed Delete key
<KeyPress-Right>    User pressed Right Arrow key

<Event-keysym>
'''


'''
printable charactor the angle bracket not included:
a, b, c, 1, 2, 3, <space>, <less>      User pressed a "printable" key
<Shift_L>, <Control_R>, <F5>, <Up>     User pressed a "special" key
<Return>                               User pressed the Enter key (<Enter> is mouse event)
<Control-Alt-Next>                     User pressed Ctrl+Alt+Page Down keys
'''
