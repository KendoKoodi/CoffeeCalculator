from tkinter import *
from tkinter import ttk

def testCommand():
    print("testCommand runned")

root = Tk()
root.title("Coffee calculator")

mainframe = ttk.Frame ( root, padding="3 3 12 12" )
mainframe.grid ( column=0, row=0, sticky=( N, W, E, S ) )
root.columnconfigure ( 0, weight=1 )
root.rowconfigure ( 0, weight=1 )

userEntry = ttk.Entry ( mainframe, width=7, textvariable="userEntry" )
userEntry.grid ( column=2, row=1, sticky=( W, E) )

testVar="testVar"
ttk.Label ( mainframe, textvariable=testVar).grid ( column=2, row=2, sticky=( W, E) )

ttk.Button ( mainframe, text="testButton", command=testCommand ).grid ( column=3, row=3, sticky=W )

ttk.Label ( mainframe, text="userEntry1" ).grid( column=3, row=1, sticky=W )
ttk.Label ( mainframe, text="testVar1" ).grid( column=1, row=2, sticky=E )
ttk.Label ( mainframe, text="testVar2" ).grid( column=3, row=2, sticky=W )

for child in mainframe.winfo_children():
    child.grid_configure ( padx=5, pady=5 )

userEntry.focus()
root.bind("<Return>", testCommand)

root.mainloop()