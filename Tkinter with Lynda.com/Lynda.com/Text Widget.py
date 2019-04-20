# Text Widget is like Entry Widget but more than 40 charecters can be input

from tkinter import *
root = Tk()
text = Text(root, width=40, height=10)
text.pack()

text.config(wrap='word')
# the word will not break into two parts when hit the edge of screen
# default: text.config(wrap='char')  others: wrap='none'



print(text.get('1.0', 'end'))
# get the whole text from the text widget

print(text.get('1.0', '1.end'))
# get the first line(logical line)

# Common Base Formats: line.char(line starts from 1, char starts from 0)
# 1.0 is the first character of the box
# end: 


text.insert('1.0', 'Hello world, I am terminator\nOk, yes')
text.insert('1.0 + 2 lines', 'Inserted Message')

# in this case, lines modifier doesn't work ..

text.delete('1.0')
text.delete('1.0', '1.0 lineend')
# from line 1 first char, to line 1 last char (the \n charactor )
# this is an none-inclusive delete: the last index not included

text.replace('1.0', '1.0 lineend', 'This is a replacement text')



text.config(state='disabled')

# theme widget has a state and instate method, but Text widget is not
# when the state set to diabled, it can not be delete: see below

text.delete('1.0', 'end')
text.config(state='normal')  # background can change here


text.tag_add('my_tag', '1.0', '1.0 wordend')
text.tag_configure('my_tag', foreground='red', background='yellow', underline=True)
# configure the tag's color
# other configuration: font foreground underline and more others


##text.tag_remove('my_tag', '1.1', '1.4')
# remove the tag from the 2 charactor in line one to the third char in line 1


print(text.tag_ranges('my_tag'))
# returns a indices of the tag in the text

print(text.tag_names())
# return all names of the tag: ('sel', 'my_tag'), sel is the default seleciton tag

print(text.tag_names('1.0'))
# returns the 1.0 char's tag


text.replace('my_tag.first', 'my_tag.last', 'ReplaceTxt')
# replace the first to last chars by replacing ReplaceTxt

text.tag_delete('my_tag')
# delete

text.mark_names()
text.insert('insert', '__')
# the mouse position will vary with the mark changed
# add string of '__' to the mark named 'insert'


text.mark_set('my_mark', 'end')
# set the mark named my_mark in the end of text widget

text.mark_gravity('my_mark', 'right')
# define the mark gravity

text.mark_unset('my_mark')
# unset the setting




image = PhotoImage(file='python.gif')
# photo image constructor method

text.image_create('insert', image=image)
# create aN image inside text widget, 'insert' is a mark


button = Button(text, text='Click Me')
text.window_create('1.0', window=button)
# create a button
# create a window of button inside text widget
# params: (position, window = object)


