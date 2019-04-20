from tkinter import *
from tkinter import ttk
root = Tk()

treeview = ttk.Treeview(root)
treeview.pack()

treeview.insert('', '0', 'item1', text='First Item')
treeview.insert('', '1', 'item2', text='Second Item')

# .insert(parent node, position, itemId(name), text property)

treeview.insert('', 'end', 'item3', text='Third Item')

# 'end' means the last position


logo = PhotoImage(file='python.gif').subsample(10, 10)
treeview.insert('item2', 'end', 'python', text='Python', image=logo)

treeview.config(height=5)

# if move an item into its own children, it will create an infinite loop

treeview.move('item2', 'item1', 'end' )
# .move(item, parent, index) : move item2 under item1 and put it in the end index

treeview.item('item1', open=True)
# item() is like a config method, but its configuring the items itself rather than the treeview object property itself
# set the treeview item open
treeview.item('item2', open=False)

print(treeview.item('item1', 'open'))
print(treeview.item('item2', 'open'))
# check if the item is open, 1 represents True, 0 False

treeview.detach('item3')
# remove the node item3, but not actually deleted

treeview.move('item3', 'item2', '0')

treeview.delete('item3')
# Truely delete the node item3, and can not be moved again

treeview.config(columns=('version'))
# create a column
treeview.column('version', width=50, anchor='center' )
treeview.column('#0', width=150)
# Set the main treeview column to 150, '#0' is the first column

treeview.heading('version', text='Version')
# Set the version title(heading)

treeview.set('python', 'version', '3.6.1')
# Set python item displaying text of 3.6.1 in version column

treeview.item('python', tags=('software'))
# create a tag in python item, soecify the tag name

treeview.tag_configure('software', background='yellow')

def callback(event):
    print(treeview.selection())

treeview.bind('<<TreeviewSelect>>', callback)
# bind the virtual event to the function
# by default treeview uses the mode called 'extended mode', ctrl+leftClick to choose multiple items

treeview.config(selectmode='browse')
# change the selectmode one item for a time
treeview.config(selectmode='none')

treeview.selection_add('python')
treeview.selection_remove('python')
# programmatically select and unselect the item

treeview.selection_toggle('python')
# select python item
