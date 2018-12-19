rom Tkinter import*

my_app = Tk(className= 'Simple Calculator')
L1 = Label(my_app, text= 'Geometry', font= ('Arial', 24))
L1.grid(row=0, column=0, columnspan=3, sticky= 'w')
L2 = Label(my_app, text= 'Calculate Area of a Cuboid, A brick for example, Formula : Length x Width x Height ')
L2.grid(row=1, column=0, columnspan=3, sticky= 'w')
L3 = Label(my_app, text= 'Length :')
L3.grid(row=3, column=0, columnspan=3, sticky= 'w')
E3 = Entry(my_app)
E3.grid(row=3, column=1, sticky='w')
L4 = Label(my_app, text= 'Width :')
L4.grid(row=4, column=0, columnspan=3, sticky= 'w')
E4 = Entry(my_app)
E4.grid(row=4, column=1, sticky='w')
L5 = Label(my_app, text= 'Height :')
L5.grid(row=5, column=0, columnspan=3, sticky= 'w')
E5 = Entry(my_app)
E5.grid(row=5, column=1, sticky='w')
L6 = Label(my_app, text='Area:')
L6.grid(row=7, column=1, sticky='w')
Area = StringVar()
L7 = Label(my_app, textvariable= Area)
L7.grid(row=7, column=2, sticky= 'w')

def calculate():
           Area.set((2*(int(E3.get())*int(E4.get())))+(2*(int(E3.get())*int(E5.get())))+(2*(int(E4.get())*int(E5.get()))))

B1= Button(my_app, text= 'calculate Area', command= calculate)
B1.grid(row=7, column=0, sticky= 'w')

my_app.mainloop()
