from tkinter import *
root = Tk()
canvas = Canvas(root)
canvas.pack()
canvas.config(width=640, height=480)
line = canvas.create_line(160, 360, 480, 120, fill='blue', width=5)
# starting x, y. ending x, y pixels

canvas.itemconfigure(line, fill='green')
# change the item 'line' in canvas

print(canvas.coords(line))
# get the coordinates (positions) of line in canvas

canvas.coords(line, 0, 0, 320, 240, 640, 0 )
# change the coordinates of the line

canvas.itemconfigure(line, smooth=True)
# draw a smooth curved line


canvas.itemconfigure(line, splinesteps=5)
# spline steps property


canvas.delete(line)
canvas.delete('all') # delete all
# delete
