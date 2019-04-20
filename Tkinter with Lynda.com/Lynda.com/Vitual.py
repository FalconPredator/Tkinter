from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root)
entry.pack()

entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))

entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
# create an event to bind
entry.bind('<<OddNumber>>', lambda e: print('This is Odd Number'))


print(entry.event_info('<<OddNumber>>'))
# to show which keys to triger the event


entry.event_generate('<<OddNumber>>')
entry.event_generate('<<Paste>>')
# envent_generate: to programetically triger the virtual event
# paste event just paste the last piece of information in buffer into entry

entry.event_delete('<<OddNumber>>')

root.mainloop()



# For virtual events: <<virtual-event>>
