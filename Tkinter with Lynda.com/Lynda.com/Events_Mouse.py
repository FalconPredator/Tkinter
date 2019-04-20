from tkinter import *
from tkinter import ttk

root = Tk()

canvas = Canvas(root, width=640, height=480, background='white')
canvas.pack()

def mouse_press(event):
    global prev
    prev = event
    print(f'type: {event.type}')
    print(f'widgets: {event.widget}')
    print(f'num: {event.num}')
    print(f'x:{event.x}')
    print(f'y:{event.y}')
    print(f'x:{event.x_root}')
    print(f'y:{event.y_root}')

def draw(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width=5)
    prev=event

    
canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', draw)



root.mainloop()








'''
Mouse Events: Click-Related : leftclick=1, middle=2, right=3
Event Format                  Event Description
<Button>, <ButtonPress>       Any button was pressed
<Button-1>, <ButtonPress-1>   Left Click the mouse
<ButtonRelease-1>             Button 1 was released
<Double-Button-1>             Double-clicked Button 1
<Triple-Button-1>             Double-clicked Button 1



<Enter>                       Mouse entered widget area
<Leave>                       Mouse left widget area
<Motion>                      Mouse was moved
<B1-Motion>                   Mouse was moved with Button 1 held down


'''
